from typing import Sequence, Tuple, List

import numpy
from scipy.interpolate import griddata


def scan_mesh_coordinates(positions: Sequence[numpy.ndarray]) -> List[numpy.ndarray]:
    """Regular grid positions encapsulating a non-regular grid.

    :param positions: `shape = (nD, n0, n1, ...)` irregular grid positions
    :returns: nD arrays of sizes `n0`, `n1`, ...
    """
    return [
        numpy.linspace(coord.min(), coord.max(), n)
        for coord, n in zip(positions, positions[0].shape)
    ]


def scan_meshgrid_coordinates(
    positions: Sequence[numpy.ndarray],
) -> Tuple[numpy.ndarray]:
    """Expand regular grid positions.

    :param positions: nD arrays of sizes `n0`, `n1`, ...
    :returns: `shape = (nD, n0, n1, ...)`
    """
    return tuple(numpy.meshgrid(*positions, indexing="ij"))


def interpolate(
    scatter_coordinates: Tuple[numpy.ndarray],
    meshgrid_coordinates: Tuple[numpy.ndarray],
    data: numpy.ndarray,
    method="linear",
    fill_value=numpy.nan,
) -> numpy.ndarray:
    """Interpolate C-order flattened data.

    :param scatter_coordinates: `shape = (nD, nPoints)` with `nPoints = n0*n1*...`
    :param meshgrid_coordinates: `shape = (nD, n0, n1, ...)`
    :param data: `shape = (nPoints,)`
    :param method: interpolate method
    :param fill_value: value outside interpolation range
    :returns: `shape = (n0, n1, ...)`
    """
    return griddata(
        scatter_coordinates,
        data,
        meshgrid_coordinates,
        method=method,
        fill_value=fill_value,
    )
