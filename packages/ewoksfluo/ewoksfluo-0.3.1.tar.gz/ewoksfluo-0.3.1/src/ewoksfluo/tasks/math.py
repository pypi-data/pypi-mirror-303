import re
from typing import Dict, Any

import numpy

from ..io.hdf5 import split_h5uri
from ..io.hdf5 import ReadHdf5File


def format_expression_template(template: str, name: str) -> str:
    n = len(re.findall(r"\{\}", template))
    return template.format(*[name] * n)


def eval_hdf5_expression(
    data_uri: str, expression: str, start_var: str = "<", end_var: str = ">"
) -> Any:
    """Evaluate an arithmetic expression with python and numpy arithmetic
    on HDF5 datasets.

    :param data_uri: HDF5 root URI
    :param expression: arithmetic expression where datasets are define as
                       :code:`"<subgroup/data>"` where :code:`"subgroup/data"`
                       is relative to :code:`data_uri`.
    :param start_var: marks the start of a variable name
    :param start_var: marks the end of a variable name
    """
    data_file, data_h5path = split_h5uri(data_uri)
    pattern = rf"{re.escape(start_var)}([^{re.escape(end_var)}]+){re.escape(end_var)}"

    with ReadHdf5File(data_file) as h5file:
        if not data_h5path:
            data_h5path = "/"
        data_root = h5file[data_h5path]

        dataset_paths = re.findall(pattern, expression)
        variables = {}
        for i, path in enumerate(dataset_paths):
            variable_name = f"data{i}"
            variables[variable_name] = data_root[path][()]
            expression = expression.replace(
                f"{start_var}{path}{end_var}", variable_name
            )

    return eval_expression(expression, variables)


def eval_expression(expression: str, variables: Dict[str, Any]) -> Any:
    """Evaluate an arithmetic expression with python and numpy arithmetic.

    :param expression: arithmetic expression where datasets are define as
                       :code:`"name1"` where :code:`"name1"`
                       must be a key in :code:`variables`.
    :param variables: variables to be used in the expression
    """
    globals = {"__builtins__": {"len": len, "sum": sum}, "np": numpy, "numpy": numpy}
    return eval(expression, globals, variables)
