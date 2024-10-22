from typing import Sequence, Tuple, List

import numpy


def scan_scatter_coordinates(
    positions: Sequence[numpy.ndarray],
) -> Tuple[Sequence[numpy.ndarray], List[int]]:
    """Re-shape C-order flattened motor positions and sort from slow axis to fast axis.

    The provided positions are the actual motor positions of an nD-dimensional scan
    of shape `(n0, n1, ...)`, flattened in C-order to a shape of `(nPoints,).`

    This algorithm works as long as the deviations of the motor positions from a
    regular grid are smaller than 30% of the step size of the scan.

    :param positions: `shape = (nD, nPoints)` where `nPoints` is a C-order
                      flattened form of `(n0, n1, ...)`
    :returns: array of `shape = (nD, n0, n1, ...)`, axes indices from slow to fast
    """
    ndim = len(positions)
    if ndim <= 1:
        return positions, list(range(ndim))

    for threshold in numpy.linspace(0.5, 0.8, 10):
        lst = sorted(
            _motor_reset_size(values, threshold=threshold) for values in positions
        )
        ncumprod, _ = zip(*lst)
        # For example 4 dimensions: ncumprod = [n0, n0*n1, n0*n1*n2, n0*n1*n2]
        ncumprod = list(ncumprod)
        ntotal = positions[0].size
        ncumprod[-1] = ntotal
        # For example 4 dimensions: ncumprod = [n0, n0*n1, n0*n1*n2, n0*n1*n2*n3]
        denom = [1] + ncumprod[:-1]

        shape_forder = [numi // denomi for numi, denomi in zip(ncumprod, denom)]
        ntotal2 = int(numpy.prod(shape_forder))
        if ntotal == ntotal2:
            break
    if ntotal != ntotal2:
        raise RuntimeError("Could not determine scan shape from motor positions")
    shape_forder = tuple(shape_forder)

    indices_forder = [None] * ndim
    remaining_indices = list(range(ndim))
    for faxis, n in enumerate(ncumprod):
        lst = sorted(
            (_smooth_motion_metric(positions[i][:n]), i) for i in remaining_indices
        )
        metric, index = lst[0]
        if not numpy.isfinite(metric):
            continue
        indices_forder[faxis] = index
        remaining_indices.remove(index)
        if len(remaining_indices) == 1:
            break
    if len(remaining_indices) != 1:
        raise RuntimeError("Could not determine motor order")
    indices_forder[indices_forder.index(None)] = remaining_indices[0]

    shape_corder = shape_forder[::-1]
    indices_corder = indices_forder[::-1]
    positions = [arr.reshape(shape_corder) for arr in positions]
    return positions, indices_corder


def _motor_reset_size(
    values: numpy.ndarray, threshold: float = 0.5
) -> Tuple[int, float]:
    """Get the median and relative stddev of the number of points between motor resets.

    :returns: median, stdev
    """
    nvalues = len(values)
    if nvalues == 0:
        # No motor positions
        return 0, numpy.inf
    if nvalues == 1:
        # Only one motor position
        return 1, numpy.inf

    steps = numpy.abs(numpy.diff(values))
    stepmin = steps.min()
    stepmax = steps.max()
    if stepmin == stepmax:
        # All motor positions are equal
        return 1, numpy.inf

    mid = (stepmax - stepmin) * threshold
    resets = numpy.where(steps > mid)[0]
    if resets.size == 1:
        # Only one motor reset
        return resets[0] + 1, numpy.inf

    resetdiff = numpy.diff(resets)
    resetsize = int(numpy.median(resetdiff))
    resetstdev = numpy.std(resetdiff)
    return resetsize, resetstdev / nvalues


def _smooth_motion_metric(values: numpy.ndarray) -> float:
    """Calculate a value which is smaller when the values represent a smooth motion"""
    vmin = values.min()
    vmax = values.max()
    if vmin == vmax:
        # All motor positions are equal
        return numpy.inf
    return numpy.std(values - numpy.linspace(vmin, vmax, values.size)) / abs(
        vmax - vmin
    )
