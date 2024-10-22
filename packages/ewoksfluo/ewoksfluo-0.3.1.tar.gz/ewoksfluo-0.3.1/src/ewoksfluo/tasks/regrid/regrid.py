from typing import List, Dict, Callable, Sequence, Tuple

import h5py
import numpy
from ewokscore import Task

from . import regrid_utils
from .. import nexus_utils
from ...io.hdf5 import ReadHdf5File
from ...io.hdf5 import split_h5uri
from ..xrf_results import get_xrf_result_groups


class RegridXrfResults(
    Task,
    input_names=["xrf_results_uri", "bliss_scan_uri", "output_root_uri"],
    optional_input_names=[
        "positioners",
        "positioner_uri_template",
        "interpolate",
        "flatten",
    ],
    output_names=["xrf_results_uri", "bliss_scan_uri", "output_root_uri"],
):
    """Regrid single-scan XRF results on a regular grid by interpolation or reshaping."""

    def run(self):
        start_time = nexus_utils.now()
        bliss_scan_uri: str = self.inputs.bliss_scan_uri
        xrf_results_uri: str = self.inputs.xrf_results_uri
        output_root_uri: str = self.inputs.output_root_uri
        position_suburis = self._get_position_suburis(bliss_scan_uri)
        interpolate: str = self.get_input_value("interpolate", "linear")

        with nexus_utils.save_in_ewoks_subprocess(
            output_root_uri, start_time, {}, default_levels=("results", "regrid")
        ) as (regrid_results, already_existed):
            if not already_existed:
                if interpolate:
                    # NXdata groups will be regular grid plots
                    grid = regrid_utils.ScanGrid(method=interpolate)
                    grid.init_grid(bliss_scan_uri, position_suburis)
                    scan_size = grid.meshgrid_coordinates[0].size
                    axes_names = grid.names
                else:
                    # NXdata groups will be scatter plots
                    flatten: bool = self.get_input_value("flatten", True)
                    positions, axes_names = (
                        regrid_utils.scan_scatter_coordinates_from_uris(
                            bliss_scan_uri, position_suburis
                        )
                    )
                    if flatten:
                        # Option exists because not all NXdata viewers can properly
                        # handle scatter data.
                        positions = [data.flatten() for data in positions]
                    scan_shape = positions[0].shape
                    scan_size = positions[0].size

                xrf_results_filename, xrf_results_h5path = split_h5uri(xrf_results_uri)

                with ReadHdf5File(xrf_results_filename) as xrf_results_file:
                    xrf_results_grp = xrf_results_file[xrf_results_h5path]
                    if not isinstance(xrf_results_grp, h5py.Group):
                        raise TypeError(f"'{xrf_results_uri}' must be a group")

                    nxdata_groups = get_xrf_result_groups(xrf_results_grp)

                    for group_name in reversed(list(nxdata_groups)):
                        input_grp = xrf_results_grp[group_name]
                        input_datasets = {
                            dset_name: dset
                            for dset_name, dset in input_grp.items()
                            if isinstance(dset, h5py.Dataset)
                            and dset.size == scan_size
                            and dset_name not in axes_names
                        }
                        if not input_datasets:
                            # NXdata group which does not plot scan data
                            continue

                        # NXdata signals
                        output_grp = nexus_utils.create_nxdata(
                            regrid_results, group_name
                        )
                        if interpolate:
                            self._save_grid_data(
                                input_datasets, grid.interpolate, output_grp
                            )
                        else:
                            self._save_scatter_data(
                                input_datasets, scan_shape, output_grp
                            )
                        nexus_utils.set_nxdata_signals(
                            output_grp, signals=tuple(input_datasets.keys())
                        )

                        # NXdata axes
                        if interpolate:
                            self._save_grid_axes(grid, output_grp)
                        elif flatten:
                            self._save_flat_scatter_axes(
                                positions, axes_names, output_grp
                            )
                        else:
                            self._save_scatter_axes(positions, axes_names, output_grp)

            self.outputs.xrf_results_uri = (
                f"{regrid_results.file.filename}::{regrid_results.name}"
            )
        self.outputs.bliss_scan_uri = bliss_scan_uri
        self.outputs.output_root_uri = output_root_uri

    def _get_position_suburis(self, bliss_scan_uri: str) -> List[str]:
        positioners = self.get_input_value("positioners", None)
        if not positioners:
            return regrid_utils.get_scan_position_suburis(bliss_scan_uri)
        if isinstance(positioners, str):
            positioners = [positioners]
        template = self.get_input_value("positioner_uri_template", "measurement/{}")
        return [template.format(s) for s in positioners]

    def _save_scatter_axes(
        self,
        positions: Sequence[numpy.ndarray],
        names: Sequence[str],
        output_grp: h5py.Group,
    ) -> None:
        axes = list()  # Order: slow to fast axis
        spanned = list(range(len(positions)))
        for axisname, arr in zip(names, positions):
            axes.append(axisname)
            output_grp.create_dataset(axisname, data=arr)
            output_grp.create_dataset(f"{axisname}_indices", data=spanned)
        output_grp.attrs["axes"] = axes

    def _save_flat_scatter_axes(
        self,
        positions: Sequence[numpy.ndarray],
        names: Sequence[str],
        output_grp: h5py.Group,
    ) -> None:
        axes = list()  # Order: slow to fast axis
        for axisname, arr in zip(names, positions):
            axes.append(axisname)
            output_grp.create_dataset(axisname, data=arr)
        output_grp.attrs["axes"] = axes[::-1]  # Order: fast to slow axis

    def _save_grid_axes(
        self, grid: regrid_utils.ScanGrid, output_grp: h5py.Group
    ) -> None:
        axes = list()  # Order: slow to fast axis
        for i, (axisname, arr) in enumerate(zip(grid.names, grid.mesh_coordinates)):
            axes.append(axisname)
            output_grp.create_dataset(axisname, data=arr)
            output_grp.create_dataset(f"{axisname}_indices", data=i)
        output_grp.attrs["axes"] = axes

    def _save_grid_data(
        self,
        input_datasets: Dict[str, h5py.Dataset],
        interpolator: Callable[[numpy.ndarray], numpy.ndarray],
        output_grp: h5py.Group,
    ) -> None:
        for dset_name, dset in input_datasets.items():
            output_grp.create_dataset(dset_name, data=interpolator(dset[()]))

    def _save_scatter_data(
        self,
        input_datasets: Dict[str, h5py.Dataset],
        scan_shape: Tuple[int],
        output_grp: h5py.Group,
    ) -> None:
        for dset_name, dset in input_datasets.items():
            regrid_utils.save_dataset_link(
                dset, output_grp, dset_name, destination_shape=scan_shape
            )
