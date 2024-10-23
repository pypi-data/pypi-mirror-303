"""Module with time period utils."""

import logging
from typing import Any

import cf_units
import cftime
import iris
import iris.coords
import iris.cube
import numpy as np
from numpy.typing import NDArray

import gordias.util.time_string

logger = logging.getLogger(__name__)


def create_aux_coord_for_time_range(
    cube: iris.cube.Cube,
    time_range: gordias.util.time_string.TimeRange,
    standard_name: str = "reference_epoch",
    var_name: str = "reference_period",
) -> iris.coords.AuxCoord:
    """
    Return a CF auxiliary coordinate for the time range.

    Parameters
    ----------
    cube : iris.cube.Cube
        Input cube to use for the auxiliary coordinate.
    time_range : gordias.util.time_string.TimeRange
        :class:`TimeRange` object representing the time range.
    standard_name : str
        CF standard name for the coordinate. By default the standard name is
        "reference_epoch".
    var_name :  str
        The netCDF variable name for the coordinate. By default the var name is
        "reference_period".

    Returns
    -------
    iris.coords.AuxCoord
        A CF auxiliary coordinate for the time range.
    """
    validate_time_bounds(cube, time_range)
    time = cube.coord("time")
    bnds_start, bnds_end = get_time_range_bounds(time_range, time.units)
    middle_point = (bnds_start + bnds_end) / 2
    bounds = np.array([bnds_start, bnds_end])
    aux_coord = iris.coords.AuxCoord(
        var_name=var_name,
        standard_name=standard_name,
        points=middle_point,
        bounds=bounds,
        units=time.units,
    )
    return aux_coord


def extract_cube_for_time_range(
    cube: iris.cube.Cube, time_range: gordias.util.time_string.TimeRange
) -> iris.cube.Cube:
    """
    Extract a new cube for the new time range.

    Parameters
    ----------
    cube : iris.cube.Cube
        Input cube from which to extract subcube.
    time_range :  gordias.util.time_string.TimeRange
        :class:`TimeRange` object defining the time range for the new cube.

    Return
    ------
    iris.cube.Cube
        A new cube with the time range defined by the :class:`TimeRange`.
    """
    validate_time_bounds(cube, time_range)
    times = get_times_helper(cube)
    idx_0, idx_n = get_first_and_last_indices(
        time_range, times, cube.coord("time").units.calendar
    )
    logger.debug(f"Extracting subcube using indices <[{idx_0}:{idx_n + 1}]>.")
    subcube = cube.copy()
    return subcube[idx_0 : idx_n + 1]


def extract_data_for_time_range(
    cube: iris.cube.Cube,
    time_range: gordias.util.time_string.TimeRange,
    padding: int = 0,
) -> NDArray | Any | None:
    """
    Extract data from the input cube for the given time range.

    Parameters
    ----------
    cube : iris.cube.Cube
        Input cube from which to extract data.
    time_range : gordias.util.time_string.TimeRange
        :class:`TimeRange` object representing the time range.
    padding : int
        Padding of the time dimension in both edges of the time range. The
        values on the edges will be used as the fill value for the padding.

    Returns
    -------
        NDArray | array | None
            Data array with the values from the time range.

    Raises
    ------
        ValueError
            If the time dimension is not the first dimension in the cube.
    """
    time_dim = cube.coord(var_name="time").cube_dims(cube)
    if time_dim != (0,):
        raise ValueError(
            "Time dimension is expected to be the first dimension. "
            f"Following time dimension was found <{time_dim}>"
        )
    validate_time_bounds(cube, time_range)
    times = get_times_helper(cube)
    idx_0, idx_n = get_first_and_last_indices(
        time_range, times, cube.coord("time").units.calendar
    )
    logger.debug(f"Extracting data using indices <[{idx_0}:{idx_n + 1}]>.")
    extracted_data = cube.core_data()[idx_0 : idx_n + 1]
    if padding > 0:
        extracted_data = np.pad(
            extracted_data, ((padding, padding), (0, 0), (0, 0)), mode="edge"
        )
    return extracted_data


def get_time_range_bounds(
    time_range: gordias.util.time_string.TimeRange, time_units: cf_units.Unit
) -> tuple[int | float, int | float]:
    """
    Return the bounds of the time range.

    Parameters
    ----------
    time_range : gordias.util.time_string.TimeRange
        :class:`TimeRange` object representing the time range.
    time_units : cf_units.Unit
        A time unit to define the bounds.

    Returns
    -------
    start : int | float
        The start of the time range for the given time unit.
    end : int | float
        The end of the time range for the given time unit.
    """
    bnds_start = cftime.date2num(
        time_range.start, time_units.name, calendar=time_units.calendar
    )
    bnds_end = cftime.date2num(
        time_range.end, time_units.name, calendar=time_units.calendar
    )
    logger.debug(f"Returning time range bounds <({bnds_start}, {bnds_end})>.")
    return (bnds_start, bnds_end)


def get_first_and_last_indices(
    time_range: gordias.util.time_string.TimeRange,
    times: gordias.util.time_string.TimesHelper,
    calendar: str,
) -> tuple[int, int]:
    """
    Given a time vector return the first and last index for the time range.

    Parameters
    ----------
    time_range : gordias.util.time_string.TimeRange
        :class:`TimeRange` object representing the time range.
    times : gordias.util.time_string.TimesHelper
        :class:`TimesHelper` object for the time vector representing a
        netCDF time variable object.
    calendar : str
        A calendar to define the indices.

    Returns
    -------
    start : int | float
        The start index of the time range for the given calendar.
    end : int | float
        The end index of the time range for the given calendar.
    """
    try:
        idx_start = cftime.date2index(
            time_range.start,
            times,
            calendar=calendar,
            select="exact",
        )
    except ValueError:
        idx_start = cftime.date2index(
            time_range.start,
            times,
            calendar=calendar,
            select="after",
        )
    idx_end = cftime.date2index(
        time_range.end, times, calendar=calendar, select="before"
    )
    logger.debug(f"Returning time range indices <({idx_start}, {idx_end})>.")
    return (idx_start, idx_end)


def get_times_helper(cube: iris.cube.Cube) -> gordias.util.time_string.TimesHelper:
    """
    Return :class:`TimesHelper` object for the cube's time vector.

    The :class:`TimesHelper` object represents a netCDF time variable object.

    Parameters
    ----------
    cube : iris.cube.Cube
        Input cube with time coordinate.

    Returns
    -------
    gordias.util.time_string.TimesHelper
        :class:`TimesHelper` object representing a netCDF time variable object for
        the input cube.
    """
    time = cube.coord("time")
    return gordias.util.time_string.TimesHelper(time)


def validate_time_bounds(
    cube: iris.cube.Cube, time_range: gordias.util.time_string.TimeRange
) -> None:
    """
    Validate that the cube's time range is inside the bounds of the time period.

    Parameters
    ----------
    cube : iris.cube.Cube
        Input cube to check the bounds against.
    time_range : gordias.util.time_string.TimeRange
        :class:`TimeRange` object representing the time range.

    Raises
    ------
    ValueError
        If the bounds of the time range are outside of the cube's time range.
    """
    time = cube.coord("time")
    bnds_start, bnds_end = get_time_range_bounds(time_range, time.units)
    if bnds_start < time.bounds[0][0] or (bnds_end - 1) > time.bounds[-1][1]:
        start_date = cftime.num2date(
            time.bounds[0][0], time.units.name, calendar=time.units.calendar
        )
        end_date = cftime.num2date(
            time.bounds[-1][1], time.units.name, calendar=time.units.calendar
        )
        raise ValueError(
            "The time period cannot be outside of the cube's time range. "
            f"Choose a time period between <{start_date}, {end_date}>"
        )
