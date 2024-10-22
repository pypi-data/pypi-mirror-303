import os
from typing import Iterator, Tuple, Optional, List, Sequence, Dict

import h5py
import numpy
from silx.io import h5py_utils

try:
    from imageio.v3 import imread
except ImportError:
    try:
        from imageio.v2 import imread
    except ImportError:
        from imageio import imread

from scipy import ndimage

from . import xrf_spectra
from .monitor import monitor_signal
from .deadtime import apply_dualchannel_signal_processing
from .. import nexus_utils


def save_2d_xrf_scans(
    filename: str,
    emission_line_groups: List[str],
    scan_number: int,
    shape: Tuple[int, int],
    energy: float = 12,
    flux: float = 1e7,
    expo_time: float = 0.1,
    counting_noise: bool = True,
    integral_type: bool = True,
    rois: Sequence = tuple(),
    ndetectors: int = 1,
    max_deviation: float = 0,
    seed: Optional[int] = None,
) -> None:
    if len(shape) != 2:
        raise ValueError("Only 2D scans are supported")
    npoints = shape[0] * shape[1]

    emission_line_groups = [s.split("-") for s in emission_line_groups]

    I0_target = int(flux * expo_time)
    I0 = (I0_target * monitor_signal(expo_time, npoints)).reshape(shape, order="F")

    info = dict()
    I0fractions = list()  # random images with values between 0 and 1
    for (samz, samy), I0fraction in _iter_2dscan_data(
        shape,
        info,
        nmaps=len(emission_line_groups) + 2,
        max_deviation=max_deviation,
        seed=seed,
    ):
        I0fractions.append(I0fraction)
    scatterI0fractions = I0fractions[:2]
    fluoI0fractions = I0fractions[2:]

    # Peak area counts within expo_time seconds
    scattergroups = [
        xrf_spectra.ScatterLineGroup(
            "Compton000", (I0 * scatterI0fractions[0]).astype(numpy.uint32)
        ),
        xrf_spectra.ScatterLineGroup(
            "Peak000", (I0 * scatterI0fractions[1]).astype(numpy.uint32)
        ),
    ]
    linegroups = [
        xrf_spectra.EmissionLineGroup(
            element, group, (I0 * I0fraction).astype(numpy.uint32)
        )
        for I0fraction, (element, group) in zip(fluoI0fractions, emission_line_groups)
    ]

    theoretical_spectra, config = xrf_spectra.xrf_spectra(
        linegroups,
        scattergroups,
        energy=energy,
        flux=flux,
        elapsed_time=expo_time,
    )

    if integral_type:
        integral_type = numpy.uint32
    else:
        integral_type = None
    measured_data = apply_dualchannel_signal_processing(
        theoretical_spectra,
        elapsed_time=expo_time,
        counting_noise=counting_noise,
        integral_type=integral_type,
    )

    roi_data_theory = dict()
    roi_data_cor = dict()  # I0 and LT corrected
    for i, roi in enumerate(rois, 1):
        roi_name = f"roi{i}"
        idx = Ellipsis, slice(*roi)
        roi_theory = theoretical_spectra[idx].sum(axis=-1) / I0 * I0_target
        roi_meas = measured_data["spectrum"][idx].sum(axis=-1)
        roi_cor = I0_target * roi_meas / I0 * expo_time / measured_data["live_time"]
        roi_data_theory[roi_name] = roi_theory
        roi_data_cor[roi_name] = roi_cor
        measured_data[roi_name] = roi_meas

    with h5py_utils.File(filename, mode="a") as nxroot:
        scan_name = f"{scan_number}.1"
        nxroot.attrs["NX_class"] = "NXroot"
        nxroot.attrs["creator"] = "ewoksfluo"

        nxentry = nxroot.require_group(scan_name)
        nxentry.attrs["NX_class"] = "NXentry"
        title = f"{info['title']} {expo_time}"
        if "title" in nxentry:
            del nxentry["title"]
        nxentry["title"] = title

        nxinstrument = nxentry.require_group("instrument")
        nxinstrument.attrs["NX_class"] = "NXinstrument"

        measurement = nxentry.require_group("measurement")
        measurement.attrs["NX_class"] = "NXcollection"

        for name in ("positioners_start", "positioners"):
            positioners = nxinstrument.require_group(name)
            positioners.attrs["NX_class"] = "NXcollection"

            if "energy" in positioners:
                del positioners["energy"]
            positioners["energy"] = energy
            positioners["energy"].attrs["units"] = "keV"

            if name == "positioners":
                continue

            if "samz" in positioners:
                del positioners["samz"]
            positioners["samz"] = samz[0][0]
            positioners["samz"].attrs["units"] = "um"

            if "samy" in positioners:
                del positioners["samy"]
            positioners["samy"] = samy[0][0]
            positioners["samy"].attrs["units"] = "um"

        nxdetector = nxinstrument.require_group("I0")
        nxdetector.attrs["NX_class"] = "NXdetector"
        if "data" in nxdetector:
            del nxdetector["data"]
        nxdetector["data"] = I0.flatten(order="F")
        if "I0" not in measurement:
            measurement["I0"] = h5py.SoftLink(nxdetector["data"].name)

        positioners = nxinstrument["positioners"]

        nxpositioner = nxinstrument.require_group("samz")
        nxpositioner.attrs["NX_class"] = "NXpositioner"
        if "value" in nxpositioner:
            del nxpositioner["value"]
        nxpositioner["value"] = samz.flatten(order="F")
        nxpositioner["value"].attrs["units"] = "um"
        if "samz" not in measurement:
            measurement["samz"] = h5py.SoftLink(nxpositioner["value"].name)
        if "samz" not in positioners:
            positioners["samz"] = h5py.SoftLink(nxpositioner["value"].name)

        nxpositioner = nxinstrument.require_group("samy")
        nxpositioner.attrs["NX_class"] = "NXpositioner"
        if "value" in nxpositioner:
            del nxpositioner["value"]
        nxpositioner["value"] = samy.flatten(order="F")
        nxpositioner["value"].attrs["units"] = "um"
        if "samy" not in measurement:
            measurement["samy"] = h5py.SoftLink(nxpositioner["value"].name)
        if "samy" not in positioners:
            positioners["samy"] = h5py.SoftLink(nxpositioner["value"].name)

        for i in range(ndetectors):
            det_name = f"mca{i}"
            nxdetector = nxinstrument.require_group(det_name)
            nxdetector.attrs["NX_class"] = "NXdetector"
            for signal_name, signal_values in measured_data.items():
                if signal_name in nxdetector:
                    del nxdetector[signal_name]
                if signal_name == "spectrum":
                    mca_shape = (shape[0] * shape[1], signal_values.shape[-1])
                    nxdetector[signal_name] = signal_values.reshape(
                        mca_shape, order="F"
                    )
                    if "data" not in nxdetector:
                        nxdetector["data"] = h5py.SoftLink("spectrum")
                    meas_name = det_name
                else:
                    nxdetector[signal_name] = signal_values.flatten(order="F")
                    meas_name = f"{det_name}_{signal_name}"
                if meas_name not in measurement:
                    measurement[meas_name] = h5py.SoftLink(nxdetector[signal_name].name)

        nxprocess = nxentry.require_group("theory")
        nxprocess.attrs["NX_class"] = "NXprocess"

        nxnote = nxprocess.require_group("configuration")
        nxnote.attrs["NX_class"] = "NXnote"
        if "data" in nxnote:
            del nxnote["data"]
        if "type" in nxnote:
            del nxnote["type"]
        nxnote["type"] = "application/pymca"
        nxnote["data"] = config.tostring()

        nxnote = nxprocess.require_group("description")
        nxnote.attrs["NX_class"] = "NXnote"
        if "data" in nxnote:
            del nxnote["data"]
        if "type" in nxnote:
            del nxnote["type"]
        nxnote["type"] = "text/plain"
        description = [
            "- parameters: peak areas without dead-time",
            "- parameters_norm: peak areas without dead-time and I0 normalized",
            "- rois: MCA ROI's without dead-time and I0 normalized (theoretical)",
            "- rois_norm: MCA ROI's without dead-time and I0 normalized (calculated)",
        ]
        nxnote["data"] = "\n".join(description)

        signals = {f"{g.element}-{g.name}": g.counts for g in linegroups}
        signals.update({g.name: g.counts for g in scattergroups})
        _save_nxdata(nxprocess, "parameters", signals, positioners)

        signals = {
            f"{g.element}-{g.name}": g.counts / I0 * I0_target for g in linegroups
        }
        signals.update({g.name: g.counts / I0 * I0_target for g in scattergroups})
        _save_nxdata(nxprocess, "parameters_norm", signals, positioners)

        if roi_data_theory:
            _save_nxdata(nxprocess, "rois", roi_data_theory, positioners)

        if roi_data_cor:
            _save_nxdata(nxprocess, "rois_norm", roi_data_cor, positioners)

        if "end_time" in nxentry:
            del nxentry["end_time"]
        nxentry["end_time"] = nexus_utils.now()


def _save_nxdata(
    parent: h5py.Group,
    name: str,
    signals: Dict[str, numpy.ndarray],
    positioners: h5py.Group,
) -> None:
    nxdata = parent.require_group(name)
    nxdata.attrs["NX_class"] = "NXdata"
    # nxdata.attrs["interpretation"] = "image"
    names = list(signals.keys())
    nxdata.attrs["signal"] = names[0]
    if len(names) > 1:
        nxdata.attrs["auxiliary_signals"] = names[1:]
    for signal_name, signal_values in signals.items():
        if signal_name in nxdata:
            del nxdata[signal_name]
        nxdata[signal_name] = signal_values.flatten(order="F")
    nxdata.attrs["axes"] = ["samz", "samy"]  # Order: fast to slow
    if "samz" not in nxdata:
        nxdata["samz"] = h5py.SoftLink(positioners["samz"].name)
    if "samy" not in nxdata:
        nxdata["samy"] = h5py.SoftLink(positioners["samy"].name)


def _iter_2dscan_data(
    shape: Tuple[int, int],
    info: dict,
    nmaps: int = 1,
    max_deviation: float = 0,
    seed: Optional[int] = None,
) -> Iterator[Tuple[List[numpy.ndarray], numpy.ndarray]]:
    """Yield random samples of an image scanned in F-order (row is the fast axis).

    :returns: list of axes positions (F-order matrices, from fast to slow axis), signal (F-order matrix)
    """
    # RGB image
    filename = os.path.join(os.path.dirname(__file__), "ihc.png")
    channels = numpy.transpose(imread(filename), [2, 0, 1])  # nimages, nfast, nslow
    _mark_scan_direction(channels)
    image_shape = channels[0].shape

    # Coordinate grid on which to interpolate the RGB image
    d = abs(max_deviation)
    pmin = [2 * d, 2 * d]
    pmax = [n - 1 - 2 * d for n in image_shape]
    rstate = numpy.random.RandomState(seed=seed)
    coordinates = _regular_scan_positions(pmin, pmax, shape, rstate, max_deviation)

    title = f"amesh samz {pmin[0]} {pmax[0]} {shape[0]-1} samy {pmin[1]} {pmax[1]} {shape[1]-1}"
    info["title"] = title

    flat_coordinates = [x.flatten(order="F") for x in coordinates]
    for _ in range(nmaps):
        # Random linear combination of the RGB channels which
        # results in an image with values between 0 and 1
        fractions = rstate.uniform(low=0, high=1, size=3)
        fractions /= 255 * fractions.sum()
        image = sum(fractions[:, numpy.newaxis, numpy.newaxis] * channels)

        # Interpolate the image on the coordinate grid
        iimage = ndimage.map_coordinates(
            image, flat_coordinates, order=1, cval=0, mode="nearest"
        )
        yield coordinates, iimage.reshape(shape, order="F")


def _mark_scan_direction(channels: numpy.ndarray) -> None:
    """Modify the image intensities to mark the scan start point and direction."""
    image_shape = channels[0].shape

    dstart = image_shape[0] // 10, image_shape[1] // 10
    dtick = dstart[0] // 4, dstart[1] // 4

    p0 = dstart[0] - dtick[0], dstart[1] - dtick[1]
    p1 = dstart[0] + dtick[0], dstart[1] + dtick[1]
    channels[:, p0[0] : p1[0], p0[1] : p1[1]] = 255

    dtick = dtick[0] // 2, dtick[1] // 2
    dend = image_shape[0] // 2, image_shape[1] // 10

    p0 = dstart[0] - dtick[0], dstart[1] - dtick[1]
    p1 = dend[0] + dtick[0], dend[1] + dtick[1]
    channels[:, p0[0] : p1[0], p0[1] : p1[1]] = 255


def _regular_scan_positions(
    pmin: Sequence[float],
    pmax: Sequence[float],
    shape: Sequence[int],
    rstate: numpy.random.RandomState,
    max_deviation: float = 0,
) -> List[numpy.ndarray]:
    """Generate motor positions of a regular nD scan. Positions are F-order arrays (fast
    axis first), ordered from fast to slow motor. The deviation is given as a fraction of
    the step size.
    """
    positions = [
        numpy.linspace(start, stop, num) for start, stop, num in zip(pmin, pmax, shape)
    ]
    positions = numpy.meshgrid(*positions, indexing="ij")
    if not max_deviation:
        return positions
    deviations = [
        abs(max_deviation if num <= 1 else (stop - start) / (num - 1) * max_deviation)
        for start, stop, num in zip(pmin, pmax, shape)
    ]
    positions = [
        values + rstate.uniform(low=-d, high=d, size=shape)
        for values, d in zip(positions, deviations)
    ]
    return positions
