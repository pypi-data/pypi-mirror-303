import itertools

import numpy
import pytest

from ..tasks.example_data import scan_data
from ..tasks.regrid import scatter_utils
from ..tasks.regrid import mesh_utils


@pytest.mark.parametrize("ndim", [0, 1, 2, 3, 4, 5])
@pytest.mark.parametrize("max_deviation", [0, 1e-6, 0.1, 0.2, 0.3, 0.4])
def test_scan_shape(ndim, max_deviation):
    rstate = numpy.random.RandomState(seed=200)
    pmin = rstate.randint(10, 30, ndim)
    pmax = rstate.randint(60, 80, ndim)
    shape_forder = tuple(rstate.randint(10, 30, ndim).tolist())
    positions = scan_data._regular_scan_positions(
        pmin, pmax, shape_forder, rstate, max_deviation=max_deviation
    )
    _assert_reshape(positions, rstate)


@pytest.mark.parametrize(
    "shape",
    [(1,), (2,), (1, 2), (2, 2), (3,), (1, 3), (1, 10), (2, 10), (1, 2, 3), (2, 2, 4)],
)
@pytest.mark.parametrize("max_deviation", [0])
@pytest.mark.xfail(reason="fix regular grid extraction")
def test_scan_shape_corner_cases(shape, max_deviation):
    rstate = numpy.random.RandomState(seed=200)
    ndim = len(shape)
    pmin = [0] * ndim
    pmax = [1] * ndim
    for shape_forder in itertools.permutations(shape):
        positions = scan_data._regular_scan_positions(
            pmin, pmax, shape_forder, rstate, max_deviation=max_deviation
        )
        _assert_reshape(positions, rstate)


def _assert_reshape(positions_forder_org, rstate: numpy.random.RandomState) -> None:
    """Positions are F-order arrays, ordered from fast to slow."""
    # Flatten the F-order arrays
    ndim = len(positions_forder_org)
    if ndim:
        shape_forder = positions_forder_org[0].shape
    else:
        shape_forder = tuple()
    print()
    print("shape_forder0", shape_forder)
    positions_flat = [arr.flatten(order="F") for arr in positions_forder_org]

    # Fast to slow order -> random order
    indices_random = list(range(ndim))
    rstate.shuffle(indices_random)
    positions_random_flat = [positions_flat[i] for i in indices_random]
    indices_forder = [indices_random.index(i) for i in range(ndim)]

    print("indices_forder0", indices_forder)
    numpy.testing.assert_array_equal(
        positions_flat, [positions_random_flat[i] for i in indices_forder]
    )

    # C-order reshape of arrays and detect order
    positions_random, indices_corder = scatter_utils.scan_scatter_coordinates(
        positions_random_flat
    )

    # Check detected order
    assert indices_corder[::-1] == indices_forder

    # Random -> Fast to slow order
    positions_forder = [positions_random[i] for i in indices_forder]

    # C-order -> F-order
    positions_forder = [
        arr_corder.flatten(order="C").reshape(shape_forder, order="F")
        for arr_corder in positions_forder
    ]

    # Check whether the original F-order arrays are
    # equal to the calculated ones
    numpy.testing.assert_array_equal(positions_forder, positions_forder_org)


def test_interpolate():
    # X is the fast axis
    x_grid = numpy.linspace(0, 10, 10)
    y_grid = numpy.linspace(0, 20, 20)
    x, y = numpy.meshgrid(x_grid, y_grid, indexing="xy")
    z = numpy.hypot(x, y)
    positions = [y, x]

    regular_positions = mesh_utils.scan_meshgrid_coordinates(
        mesh_utils.scan_mesh_coordinates(positions)
    )
    irregular_positions = tuple(pos.flatten() for pos in positions)
    numpy.testing.assert_array_equal(positions, regular_positions)

    for method in ("nearest", "linear"):
        data = mesh_utils.interpolate(
            irregular_positions, regular_positions, z.flatten(), method=method
        )
        numpy.testing.assert_array_equal(data, z)
