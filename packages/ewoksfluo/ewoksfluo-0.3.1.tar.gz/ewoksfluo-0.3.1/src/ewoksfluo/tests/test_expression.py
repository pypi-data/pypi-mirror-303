import h5py

from ewoksfluo.tasks import math


def test_eval_expression():
    expression = "np.mean([1,a,3,b])"
    variables = {"a": 2, "b": 4}
    math.eval_expression(expression, variables) == 2.5


def test_eval_hdf5_expression(tmp_path):
    filename = str(tmp_path / "data.h5")
    with h5py.File(filename, mode="w") as f:
        f["group/a"] = 2
        f["b"] = 4

    expression = "np.mean([1,<group/a>,3,<b>])"

    math.eval_hdf5_expression(filename, expression) == 2.5

    filename = str(tmp_path / "data.h5")
    with h5py.File(filename, mode="w") as f:
        f["root/group/a"] = 2
        f["root/b"] = 4

    expression = "np.mean([1,<group/a>,3,<b>])"

    math.eval_hdf5_expression(filename + "::/root", expression) == 2.5
