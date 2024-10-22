from typing import Sequence, Tuple, List, Optional

import numpy
import h5py

from ...io.hdf5 import split_h5uri
from ...io.hdf5 import retry_external_link
from ...io.hdf5 import ReadHdf5File
from . import scatter_utils
from . import mesh_utils


def scan_scatter_coordinates_from_uris(
    bliss_scan_uri: str, position_suburis: Sequence[str]
) -> Tuple[Tuple[numpy.ndarray], Tuple[str]]:
    """Re-shape C-order flattened motor positions and sort from slow axis to fast axis.

    :returns: 1D arrays of scatter coordinates for each dimension (order: slow axis to fast),
              corresponding names of each dimension
    """
    positions, names = _read_position_suburis(bliss_scan_uri, position_suburis)
    reshaped_positions, slow_to_fast = scatter_utils.scan_scatter_coordinates(positions)
    ordered_reshaped_positions = tuple(reshaped_positions[i] for i in slow_to_fast)
    ordered_names = tuple(names[i] for i in slow_to_fast)
    return ordered_reshaped_positions, ordered_names


class ScanGrid:
    def __init__(self, method="linear", fill_value=numpy.nan) -> None:
        self._method = method
        self._fill_value = fill_value
        self._names = None
        self._meshgrid_coordinates = None
        self._scatter_coordinates = None

    def init_grid(self, bliss_scan_uri: str, position_suburis: Sequence[str]):
        """Initialize the grid on which to regrid data"""
        positions, names = _read_position_suburis(bliss_scan_uri, position_suburis)

        reshaped_positions, slow_to_fast = scatter_utils.scan_scatter_coordinates(
            positions
        )
        scatter_coordinates = tuple(positions[i] for i in slow_to_fast)
        reshaped_positions = tuple(reshaped_positions[i] for i in slow_to_fast)
        mesh_coordinates = mesh_utils.scan_mesh_coordinates(reshaped_positions)
        meshgrid_coordinates = mesh_utils.scan_meshgrid_coordinates(mesh_coordinates)

        self._names = tuple(names[i] for i in slow_to_fast)
        self._mesh_coordinates = mesh_coordinates
        self._meshgrid_coordinates = meshgrid_coordinates
        self._scatter_coordinates = scatter_coordinates

    def interpolate(self, data: numpy.ndarray) -> numpy.ndarray:
        """Regrid data on the current grid"""
        return mesh_utils.interpolate(
            self._scatter_coordinates,
            self._meshgrid_coordinates,
            data,
            method=self._method,
            fill_value=self._fill_value,
        )

    @property
    def mesh_coordinates(self) -> Optional[List[numpy.ndarray]]:
        """1D arrays of coordinates along each grid dimension (order: slow axis to fast)"""
        return self._mesh_coordinates

    @property
    def meshgrid_coordinates(self) -> Optional[List[numpy.ndarray]]:
        """nD arrays of coordinates along each grid dimension (order: slow axis to fast)"""
        return self._meshgrid_coordinates

    @property
    def names(self) -> Optional[List[numpy.ndarray]]:
        """Name for each grid dimension (order: slow axis to fast)"""
        return self._names


def _read_position_suburis(
    bliss_scan_uri: str, position_suburis: Sequence[str]
) -> Tuple[List[numpy.ndarray], Tuple[str]]:
    positions = [
        get_position_data(bliss_scan_uri, position_suburi)
        for position_suburi in position_suburis
    ]
    names = [[s for s in name.split("/") if s][-1] for name in position_suburis]
    return positions, names


def get_position_data(bliss_scan_uri: str, position_suburi: str) -> numpy.ndarray:
    """Get position data from HDF5"""
    scan_filename, scan_h5path = split_h5uri(bliss_scan_uri)

    with ReadHdf5File(scan_filename) as scan_file:
        scan_grp = scan_file[scan_h5path]
        assert isinstance(scan_grp, h5py.Group)
        with retry_external_link(scan_grp, position_suburi) as pos_dataset:
            assert isinstance(pos_dataset, h5py.Dataset)
            return pos_dataset[()]


def get_scan_position_suburis(bliss_scan_uri: str) -> List[str]:
    """Get all scan sub-URI's for positioners which were scanned."""
    scan_filename, scan_h5path = split_h5uri(bliss_scan_uri)

    with ReadHdf5File(scan_filename) as scan_file:
        scan_grp = scan_file[scan_h5path]
        positioners = set(scan_grp["instrument/positioners_start"])
        counters = set(scan_grp["measurement"])
        positioners &= counters
        return [f"measurement/{s}" for s in positioners]


def save_stack_positions(
    parent: h5py.Group,
    dset_name: str,
    shape: Tuple[int, ...],
    bliss_scan_uris: Sequence[str],
    position_suburi: str,
) -> h5py.Dataset:
    """Save in C-order"""
    dataset = None
    for i_scan, bliss_scan_uri in enumerate(bliss_scan_uris):
        pos_data = get_position_data(bliss_scan_uri, position_suburi)
        if dataset is None:
            dataset = parent.create_dataset(
                dset_name,
                shape=shape,
                dtype=pos_data.dtype,
            )
        dataset[i_scan, ...] = pos_data.reshape(shape[1:])
    return dataset


def save_dataset_link(
    original_dset: h5py.Dataset,
    destination_parent: h5py.Group,
    destination_name: str,
    destination_shape: tuple,
) -> None:
    """Save link to dataset, reshaped when needed (C-order reshape because VDS only supports that)."""
    original_filename = original_dset.file.filename
    original_dset_name = original_dset.name
    original_shape = original_dset.shape
    if original_shape == destination_shape:
        if original_filename == destination_parent.file.filename:
            link = h5py.SoftLink(original_dset_name)
        else:
            link = h5py.ExternalLink(original_filename, original_dset_name)
        destination_parent[destination_name] = link
    else:
        layout = h5py.VirtualLayout(shape=destination_shape, dtype=original_dset.dtype)
        vsource = h5py.VirtualSource(
            original_filename, original_dset_name, shape=original_shape
        )
        layout[...] = vsource
        destination_parent.create_virtual_dataset(
            destination_name, layout, fillvalue=numpy.nan
        )
