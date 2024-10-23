"""Module for finding the difference between two iris cubes."""

import logging
from typing import Any

import dask.array as da
import iris.coords
import iris.cube
import numpy as np
import numpy.ma as ma
import pandas as pd
from numpy.typing import NDArray

logger = logging.getLogger(__name__)

MISSING_VALUE: Any = "---------"
MAX_COL_WIDTH: int = 30
MAX_COL_NUMBER: int = 5


def _attr_to_dict(
    obj: iris.cube.Cube | iris.coords.AuxCoord | iris.coords.DimCoord,
    attr_list: list[str],
) -> dict[str, Any]:
    """Extract object attributes and their values into a dictionary."""
    attr_dict = {}
    for attr in attr_list:
        if isinstance(obj, iris.cube.Cube) and attr == "data":
            attr_dict["masked_data"] = _compare_cube_data(obj)
        else:
            attr_dict[attr] = getattr(obj, attr, MISSING_VALUE)
    return attr_dict


def _compare_dicts(dict_list: list[dict[str, Any]]) -> dict[str, Any]:
    """Return differences in a list of dictionaries."""
    all_keys = set()
    for d in dict_list:
        all_keys.update(set(d.keys()))
    diff_dict = {}
    for k in list(all_keys):
        vals = []
        for d in dict_list:
            vals.append(str(d.get(k, MISSING_VALUE)))  # ###
        if len(set(vals)) > 1:  # ###
            diff_dict[k] = vals
    return diff_dict


def _compare_cell_methods(cube_list: iris.cube.CubeList) -> dict[str, list[str]]:
    """Return differences in cell_methods in a list of iris cubes."""

    def _reformat_cell_method(cm: iris.coords.CellMethod) -> str | Any:
        """Return a CF-like string representation of the cell_method object."""
        method = getattr(cm, "method", MISSING_VALUE)
        if method == MISSING_VALUE:
            return MISSING_VALUE
        coord_names = "".join("{}: ".format(t) for t in tuple(cm.coord_names))
        intervals = tuple(getattr(cm, "intervals", ""))
        comments = getattr(cm, "comments", "")
        if len(comments) == 0:
            cm_text = "{}{}".format(coord_names, method)
        else:
            cm_text = "{}{} ({})".format(coord_names, method, comments)
            if len(intervals) > 0:
                interval = "".join("interval: {} ".format(t) for t in intervals)
                cm_text += " ({})".format(interval)
        return cm_text

    def _get_cell_method(cm: tuple[iris.coords.CellMethod], i: int) -> str | Any:
        """Return the i:th cell_method string or the MISSING_VALUE string."""
        try:
            return _reformat_cell_method(cm[i])
        except IndexError:
            return MISSING_VALUE

    ncm = 0
    cm_list = []
    cm_set = set()
    cm_dict = {}
    for cube in cube_list:
        cm_tuple = cube.cell_methods
        ncm = max(ncm, len(cm_tuple))
        cm_list.append(cm_tuple)
        cm_set.add(cm_tuple)
    if len(cm_set) > 1:
        for i in range(ncm):
            cm_dict["cell_method_#{}".format(i)] = [
                _get_cell_method(cm, i) for cm in cm_list
            ]
    return cm_dict


def _compare_variable_attrs(
    cube_list: iris.cube.CubeList,
) -> dict[str, bool | str | list[str]]:
    """Return differences in variable attributes in a list of iris cubes."""
    variable_attr = [
        "standard_name",
        "long_name",
        "var_name",
        "units",
        "shape",
        "dtype",
        "location",
        "mesh",
        "data",
    ]
    var_list = []
    var_dict = {}
    for cube in cube_list:
        var_list.append(_attr_to_dict(cube, variable_attr))
    var_dict.update(_compare_dicts(var_list))
    var_dict.update(_compare_cell_methods(cube_list))
    return var_dict


def _compare_time_start_end(
    coord_list: list[iris.coords.AuxCoord | iris.coords.DimCoord],
) -> list[tuple[str, Any]]:
    """Return difference in time from a list of iris cubes.

    Checks difference between calendar information and start- and end date.
    """
    date_list = []
    for time in coord_list:
        date_dict = {}
        date_dict["start_date"] = time.cell(0).point
        date_dict["end_date"] = time.cell(-1).point
        date_dict["calendar"] = time.units.calendar
        date_list.append(date_dict)
    date_diff = _compare_dicts(date_list)
    sorted_date_diff = sorted(date_diff.items(), reverse=True)
    return sorted_date_diff


def _compare_global_attrs(cube_list: iris.cube.CubeList) -> dict[str, Any]:
    """Return differences in 'global' attributes in a list of iris cubes."""
    glob_list = []
    for cube in cube_list:
        glob_list.append(cube.attributes)
    return _compare_dicts(glob_list)


def _compare_coordinate_attrs(
    coord_list: list[iris.coords.AuxCoord | iris.coords.DimCoord], name: str
) -> dict[str, list[Any]]:
    """Return differences in attributes in a list of iris cube coordinates."""
    coordinate_attr = [
        "circular",
        "coord_system",
        "long_name",
        "standard_name",
        "units",
        "var_name",
    ]
    coord_attr_list = []
    array_dict: dict[str, list[Any]] = {"points": [], "bounds": []}
    for coord in coord_list:
        attr_dict = _attr_to_dict(coord, coordinate_attr)
        for attr in ["points", "bounds"]:
            array = getattr(coord, attr, None)
            attr_dict[f"{attr}.shape"] = MISSING_VALUE
            attr_dict[f"{attr}.dtype"] = MISSING_VALUE
            attr_dict[f"{attr}.masked"] = MISSING_VALUE
            attr_dict[f"len({attr})"] = MISSING_VALUE
            attr_dict[f"type({attr})"] = MISSING_VALUE
            if isinstance(array, (np.ndarray, np.generic)):
                attr_dict[f"{attr}.shape"] = array.shape
                attr_dict[f"{attr}.dtype"] = array.dtype
                attr_dict[f"{attr}.masked"] = ma.is_masked(array)
            elif array is None:
                attr_dict[f"type({attr})"] = type(array)
            else:
                attr_dict[f"len({attr})"] = len(array)
                attr_dict[f"type({attr})"] = type(array)
            array_dict[attr].append(array)
        coord_attr_list.append(attr_dict)
    coord_attr_dict = _compare_dicts(coord_attr_list)
    for attr in ["points", "bounds"]:
        result = _compare_coordinate_values(array_dict, attr)
        if result:
            coord_attr_dict.update(result)
    if name == "time":
        datetime = _compare_time_start_end(coord_list)
        coord_attr_dict.update(datetime)
    return coord_attr_dict


def _compare_coordinate_values(array_dict: dict[str, Any], attr: str) -> dict[str, Any]:
    array_list = array_dict[attr]
    coord_val_list = []
    try:
        same = (
            np.diff(np.vstack(array_list).reshape(len(array_list), -1), axis=0) == 0
        ).all()
    except (ValueError, TypeError):
        same = False
    if same:
        attr_list = {}
    else:
        for array in array_list:
            val_dict: dict[str, Any] = {}
            if array is not None and array.size > 0 and not np.all(array == None):  # noqa
                val_dict[f"{attr}.diff"] = True
                val_dict[f"{attr}.min"] = np.min(array)
                val_dict[f"{attr}.max"] = np.max(array)
                val_dict[f"{attr}.mean"] = np.mean(array)
            else:
                val_dict[f"{attr}.min"] = None
                val_dict[f"{attr}.max"] = None
                val_dict[f"{attr}.mean"] = None
            coord_val_list.append(val_dict)
        attr_list = _compare_dicts(coord_val_list)
        if not attr_list and not np.all(array == None):  # noqa
            attr_list = {f"{attr}.differ": [True] * len(array_list)}
    return attr_list


def _compare_cube_coords(cube_list: iris.cube.CubeList) -> dict[str, NDArray]:  # noqa C901 (complex function needs to be rewritten)
    """Return differences in coordinates in a list of iris cubes."""
    all_coord_dict = {}
    all_coord_names = set()
    coord_name_list = []

    for cube in cube_list:
        names = [c.name() for c in cube.coords()]
        coord_name_list.append(names)
        all_coord_names.update(set(names))

    for name in all_coord_names:
        result = np.array(["Missing"] * len(cube_list), dtype=object)
        mask = np.array([name in coord_names for coord_names in coord_name_list])
        imask = np.arange(len(mask))
        coord_list = [cube_list[i].coord(name) for i in imask[mask]]
        coord_dict = _compare_coordinate_attrs(coord_list, name)
        if sum(mask) == 1:
            result[mask] = "Present"
            if len(set(result)) > 1:
                all_coord_dict[name] = result
        elif len(coord_dict) == 0:
            result[mask] = "Equal"
            if len(set(result)) > 1:
                all_coord_dict[name] = result
        else:
            for k, v in coord_dict.items():
                result = np.array(["Missing"] * len(cube_list), dtype=object)
                if (name == "time") and (k == "units"):
                    result[mask] = np.array(
                        [repr(v[i])[6:-1] for i in range(len(imask[mask]))]
                    )
                else:
                    result[mask] = np.array(
                        [repr(v[i]) for i in range(len(imask[mask]))]
                    )
                if len(set(result)) > 1:
                    all_coord_dict["{}:{}".format(name, k)] = result

    if "time" not in all_coord_names:
        result = np.array(["Missing"] * len(cube_list), dtype=object)
        all_coord_dict["time"] = result
    return all_coord_dict


def _compare_cube_data(cube: iris.cube.Cube) -> bool:
    data = da.moveaxis(cube.core_data(), 0, -1)
    data = data.rechunk(("auto",) * (data.ndim - 1) + (-1,))
    mask = da.ma.getmaskarray(data)
    boolean: bool = mask.any().compute()
    return boolean


def _cube_differences_to_dicts(
    cube_list: iris.cube.CubeList, oper: str
) -> dict[str, dict[str, Any]]:
    """Return selected aspects/attributes differing in a list of iris cubes."""
    dicts_dict = {}
    if len(cube_list) < 2:
        return {}
    if "V" in oper:
        dicts_dict["VARIABLES"] = _compare_variable_attrs(cube_list)
    if "G" in oper:
        dicts_dict["GLOBALS"] = _compare_global_attrs(cube_list)
    if "C" in oper:
        dicts_dict["COORDINATES"] = _compare_cube_coords(cube_list)
    return dicts_dict


def _merge_dicts(
    dicts_dict: dict[str, dict[str, Any]], labels: dict[str, Any]
) -> dict[str, Any]:
    """Return a merged dict with some 'table delimiters' and labels."""
    all_dict: dict[str, Any] = {}
    if sum(len(d) for d in dicts_dict) == 0:
        return all_dict
    ncubes = len(list(labels.values())[0])
    all_dict.update(labels)
    for d in ["VARIABLES", "GLOBALS", "COORDINATES"]:
        if d in dicts_dict and len(dicts_dict[d]) > 0:
            deli = "-" * (MAX_COL_WIDTH - 6 - len(d))
            all_dict.update(
                {
                    "-- {} {}".format(d, deli): np.array(
                        ["-" * (MAX_COL_WIDTH - 2)] * ncubes
                    )
                }
            )
            all_dict.update(dicts_dict[d])
    all_dict.update(
        {"=" * (MAX_COL_WIDTH - 2): np.array(["=" * (MAX_COL_WIDTH - 2)] * ncubes)}
    )
    return all_dict


def _print_dataframe(dataframe: pd.DataFrame, cube_list: iris.cube.CubeList) -> None:
    var_name = cube_list[0].var_name
    length = len(cube_list)
    with pd.option_context(
        "display.max_colwidth", MAX_COL_WIDTH, "display.max_rows", None
    ):
        logger.error(f"Failed to concatenate cubes for variable <{var_name}>.")
        msg = (
            "The following differences were found when comparing the "
            "resulting cubes:\n"
        )
        for i in np.arange(0, length, MAX_COL_NUMBER):
            msg += (
                dataframe.iloc[:, i : min(i + MAX_COL_NUMBER, length + 1)].to_string()
                + "\n"
            )
        logger.error(msg)


def find_cube_differences(
    cube_list: iris.cube.CubeList,
    oper: str = "VGC",
    return_type: str = "logging",
    cube_labels: list[str] | str | None = None,
) -> dict[Any, Any] | pd.DataFrame | None:
    """Expose most differences between iris cubes in a list.

    This includes differences between `variables`, `global attributes` and
    `coordinates`.

    `return_type` specifies how to present the differences, allowed values are:

    - 'dict': A dict is returned, with differing attributes as keys.

    - 'DataFrame': A pandas.DataFrame is returned.

    - 'logging': A logged message,

    Parameters
    ----------
    cube_list: iris.cube.CubeList
        A list of cubes.
    oper: str
       A string that specifies which cube components to check, any combination of the
       following letters: 'V' (variables), 'G' (global attributes),
       'C' (coordinates).
    return_type: str
        A string that specifies how to present the differences. Default is 'logging'.
    cube_labels: list[str] | str
        A list of strings with labels for the cubes. If a string is given it will be a
        global label for all cubes.

    Returns
    -------
    dict[str, str] | pandas.DataFrame | None

    """
    dicts_dict = _cube_differences_to_dicts(cube_list, oper)

    if cube_labels is not None:
        if isinstance(cube_labels, str):
            labels = {
                cube_labels: [
                    "{}".format(cube.attributes.get(cube_labels, ""))
                    for cube in cube_list
                ]
            }
        elif isinstance(cube_labels, list) and (len(cube_labels) == len(cube_list)):
            labels = {"cube_labels": cube_labels}
    elif return_type == "dict":
        labels = {"cube #": np.arange(len(cube_list)).astype(str)}
    else:
        labels = {"label": [""] * len(cube_list)}

    all_dict = _merge_dicts(dicts_dict, labels)

    if return_type == "dict":
        return all_dict
    else:
        dataframe = pd.DataFrame.from_dict(all_dict).T
        dataframe.columns.name = "cube nr"
        if return_type == "DataFrame":
            return dataframe
        elif return_type == "logging":
            _print_dataframe(dataframe, cube_list)
            return None
    raise NotImplementedError
