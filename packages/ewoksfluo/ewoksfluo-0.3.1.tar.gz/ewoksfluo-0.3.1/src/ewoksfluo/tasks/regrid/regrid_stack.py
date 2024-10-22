from typing import Sequence, List

import h5py
import numpy
from ewokscore import Task

from . import regrid_utils
from .. import nexus_utils
from ...io.hdf5 import ReadHdf5File
from ...io.hdf5 import split_h5uri
from ..xrf_results import get_xrf_result_groups
from ..positioner_utils import get_energy_suburi


class RegridXrfResultsStack(
    Task,
    input_names=["xrf_results_uri", "bliss_scan_uris", "output_root_uri"],
    optional_input_names=[
        "stack_positioner",
        "positioners",
        "positioner_uri_template",
        "interpolate",
    ],
    output_names=["xrf_results_uri", "bliss_scan_uris", "output_root_uri"],
):
    """Regrid multi-scan XRF results on a regular grid by interpolation or reshaping."""

    def run(self):
        start_time = nexus_utils.now()
        bliss_scan_uris: Sequence[str] = self.inputs.bliss_scan_uris
        xrf_results_uri: str = self.inputs.xrf_results_uri
        output_root_uri: str = self.inputs.output_root_uri
        position_suburis = self._get_position_suburis(bliss_scan_uris)
        stack_suburi = self._get_stack_suburi(bliss_scan_uris, position_suburis)
        interpolate: str = self.get_input_value("interpolate", "linear")

        with nexus_utils.save_in_ewoks_subprocess(
            output_root_uri, start_time, {}, default_levels=("results", "regrid")
        ) as (regrid_results, already_existed):
            if not already_existed:
                grid = regrid_utils.ScanGrid(method=interpolate)

                xrf_results_filename, xrf_results_h5path = split_h5uri(xrf_results_uri)

                with ReadHdf5File(xrf_results_filename) as xrf_results_file:
                    xrf_results_grp = xrf_results_file[xrf_results_h5path]
                    if not isinstance(xrf_results_grp, h5py.Group):
                        raise TypeError(f"'{xrf_results_h5path}' must be a group")

                    nxdata_groups = get_xrf_result_groups(xrf_results_grp)

                    grid.init_grid(bliss_scan_uris[0], position_suburis)
                    scan_size = grid.meshgrid_coordinates[0].size
                    axes_names = (
                        stack_suburi.split("/")[-1],
                    ) + grid.names  # Order: slow to fast axis

                    # Get fit result datasets (inputs) and output dataset information
                    input_datasets = list()
                    output_info = list()
                    output_grps = list()
                    for group_name in reversed(list(nxdata_groups)):
                        input_grp = xrf_results_grp[group_name]

                        output_grp = nexus_utils.create_nxdata(
                            regrid_results, group_name
                        )
                        output_grps.append(output_grp)

                        signals = list()
                        for dset_name, dset in input_grp.items():
                            if (
                                not isinstance(dset, h5py.Dataset)
                                or dset_name in axes_names
                            ):
                                continue
                            dset_scan_size = numpy.prod(dset.shape[1:], dtype=int)
                            if dset_scan_size != scan_size:
                                continue
                            key = group_name, dset_name
                            input_datasets.append(dset)
                            output_info.append((output_grp, group_name, dset_name))
                            signals.append(dset_name)

                        nexus_utils.set_nxdata_signals(output_grp, signals=signals)

                    # NXdata signals
                    nscans = len(bliss_scan_uris)
                    output_datasets = dict()
                    stack_axis = list()
                    for scan_index, (bliss_scan_uri, *input_data) in enumerate(
                        zip(bliss_scan_uris, *input_datasets)
                    ):
                        stack_axis.append(
                            regrid_utils.get_position_data(bliss_scan_uri, stack_suburi)
                        )
                        for (output_grp, group_name, dset_name), data in zip(
                            output_info, input_data
                        ):
                            data = grid.interpolate(data)
                            key = group_name, dset_name
                            dset = output_datasets.get(key)
                            if dset is None:
                                stack_shape = (nscans,) + data.shape
                                dset = output_grp.create_dataset(
                                    dset_name, shape=stack_shape, dtype=data.dtype
                                )
                                output_datasets[key] = dset
                            dset[scan_index] = data

                    # NXdata axes
                    axes_data = [stack_axis] + grid.mesh_coordinates
                    for output_grp in output_grps:
                        for i, (axisname, arr) in enumerate(zip(axes_names, axes_data)):
                            output_grp.create_dataset(axisname, data=arr)
                            output_grp.create_dataset(f"{axisname}_indices", data=i)
                        output_grp.attrs["axes"] = axes_names

            self.outputs.xrf_results_uri = (
                f"{regrid_results.file.filename}::{regrid_results.name}"
            )
        self.outputs.bliss_scan_uris = bliss_scan_uris
        self.outputs.output_root_uri = output_root_uri

    def _get_position_suburis(self, bliss_scan_uris: Sequence[str]) -> List[str]:
        positioners = self.get_input_value("positioners", None)
        if positioners:
            if isinstance(positioners, str):
                positioners = [positioners]
            template = self._get_positioner_uri_template()
            return [template.format(s) for s in positioners]
        return regrid_utils.get_scan_position_suburis(bliss_scan_uris[0])

    def _get_stack_suburi(
        self, bliss_scan_uris: Sequence[str], position_suburis: List[str]
    ) -> str:
        stack_positioner = self.get_input_value("stack_positioner", None)
        if stack_positioner:
            template = self._get_positioner_uri_template()
            return template.format(stack_positioner)
        suburi = get_energy_suburi(bliss_scan_uris[0])
        if not suburi:
            raise RuntimeError("Cannot find energy positioner")
        return suburi

    def _get_positioner_uri_template(self) -> str:
        return self.get_input_value("positioner_uri_template", "measurement/{}")
