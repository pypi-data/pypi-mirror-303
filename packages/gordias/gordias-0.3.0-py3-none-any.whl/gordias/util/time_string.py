"""Module with time string parsing utilities."""

import datetime
import re
from typing import Any, NamedTuple

import dateutil.relativedelta
import iris.coords
import isodate

TIME_FORMATS = {
    4: "%Y",
    6: "%Y%m",
    8: "%Y%m%d",
    10: "%Y%m%d%H",
    12: "%Y%m%d%H%M",
    14: "%Y%m%d%H%M%S",
}

TIME_RELATIVE_DELTAS = {
    4: dateutil.relativedelta.relativedelta(years=+1),
    6: dateutil.relativedelta.relativedelta(months=+1),
    8: dateutil.relativedelta.relativedelta(days=+1),
    10: dateutil.relativedelta.relativedelta(hours=+1),
    12: dateutil.relativedelta.relativedelta(minutes=+1),
    14: dateutil.relativedelta.relativedelta(seconds=+1),
}

ISODATE_RELATIVE_DURATIONS = {
    r"[0-9]{4}": isodate.Duration(years=1),
    r"[0-9]{4}-[0-9]{2}": isodate.Duration(months=1),
    r"[0-9]{4}-[0-9]{2}-[0-9]{2}": isodate.Duration(days=1),
}


class TimesHelper:
    """
    Internal helper class needed for interaction with `cftime`.

    Functions of `cftime` requires a netCDF4 variable as input, this class wraps an
    iris cube time variable to get the behaviour of a netCDF4 variable.

    Parameters
    ----------
    time : iris.coords.DimCoord
        A coordinate that is 1D and numeric, representing the time dimension.

    Attributes
    ----------
    times : NDArray | array | None
        Core points array at the core of this coord, which may be a NumPy array or a
        dask array.
    units : str
        The S.I unit of the object.
    """

    def __init__(self, time: iris.coords.DimCoord):
        self.times = time.core_points()
        self.units = str(time.units)

    def __getattr__(self, name: str) -> Any:
        """Magic method returning attribute."""
        return getattr(self.times, name)

    def __len__(self) -> int:
        """Magic method returning length."""
        return len(self.times)

    def __getitem__(self, key: int) -> Any:
        """Magic method returning item."""
        return self.times[key]


class TimeRange(NamedTuple):
    """
    Simple time range class.

    Note
    -----
    For details on the interpretation of climatological time axis, refer to
    `CF Conventions 1.7, Section 7.4 <http://cfconventions.org/Data/
    cf-conventions/cf-conventions-1.7/
    cf-conventions.html#climatological-statistics>`_

    Parameters
    ----------
    start : datetime.datetime
        First time point (usually day) included in time range.
    end : datetime.datetime
        Last time point (usually day) included in time range.
    climatological : bool
        `True` if the range is climatological, `False` if it is consecutive.

    Attributes
    ----------
    start : datetime.datetime
        First time point (usually day) included in time range.
    end : datetime.datetime
        Last time point (usually day) included in time range.
    climatological : bool
        `True` if the range is climatological, `False` if it is consecutive.
    """

    start: datetime.datetime
    end: datetime.datetime
    climatological: bool


def parse_time(time: str) -> datetime.datetime:
    """Parse a time string to a datetime.datetime object.

    This function parses a time string in non-iso format.
    The following formats is currently supported:
    "%Y", "%Y%m", "%Y%m%d", "%Y%m%d%H", "%Y%m%d%H%M", "%Y%m%d%H%M%S".

    Parameters
    ----------
    time : str
        String to parse.

    Returns
    -------
    datetime.datetime
        The parsed time.

    Raises
    ------
    ValueError
        If the time could not be parsed.
    """
    time_length = len(time)
    if time_length not in TIME_FORMATS:
        raise ValueError(f"Invalid time string {time}")
    format_string = TIME_FORMATS[time_length]
    return datetime.datetime.strptime(time, format_string)


def parse_time_range(time_range: str, end_inclusive: bool = False) -> TimeRange:
    """Parse a time range string given in CMIP/CORDEX-like format.

    Parameters
    ----------
    time_range : str
        A time range given in CMIP/CORDEX-like format, as described in
        `CMIP6 Global Attributes, DRS, Filenames, Directory Structure,
        and CV's <http://goo.gl/v1drZl>`_:

        .. code-block:: text

            The <time_range> is a string generated consistent with the
            following:

            If frequency = "fx" then
                <time_range>=""
            else
                <time_range> = N1-N2 where N1 and N2 are integers of the form
                "yyyy[MM[dd[hh[mm[ss]]]]][<suffix>]" (expressed as a string,
                where "yyyy", "MM", "dd", "hh", "mm", and "ss" are integer
                year, month, day, hour, minute, and second, respectively)
            endif

            where <suffix> is defined as follows:

            if the variable identified by variable_id has a time dimension with
            a "climatology" attribute then
                suffix = "-clim"
            else
                suffix = ""
            endif

            and where the precision of the time_range strings is determined by
            the "frequency" global attribute as specified in Table 2.

    end_inclusive : bool, optional
        If True, a delta will be added to end time, to guarantee that the end time
        in the given string is within the returned time range. The size of the delta
        is determined by the resolution of the times in the given time string.
        Default is False.

    Returns
    -------
    TimeRange
        Extracted TimeRange object.
    """
    parts = time_range.split("-")
    n = len(parts)
    if n < 2 or n > 3:
        raise ValueError(f"Invalid time range {time_range}")
    if n == 3:
        if parts[2] != "clim":
            raise ValueError(f"Invalid time range {time_range}")
        climatological = True
    else:
        climatological = False
    if len(parts[0]) != len(parts[1]):
        raise ValueError(
            f"Start and end time must have the same resolution in {time_range}"
        )

    range_start = parse_time(parts[0])
    range_end = parse_time(parts[1])
    if range_start > range_end:
        raise ValueError(f"Invalid time range {time_range}")

    if end_inclusive:
        return TimeRange(
            range_start, range_end + TIME_RELATIVE_DELTAS[len(parts[1])], climatological
        )
    else:
        return TimeRange(range_start, range_end, climatological)


def is_valid_time(string: str) -> bool:
    """Check if given string is a time.

    Parameters
    ----------
    time : str
        String to check.

    Returns
    -------
    bool
        True if given string is a valid time.
    """
    try:
        parse_time(string)
        return True
    except ValueError:
        return False


def is_valid_time_range(string: str) -> bool:
    """Check if given string is a time range.

    Parameters
    ----------
    time : str
        String to check.

    Returns
    -------
    bool
        True if given string is a valid time range.
    """
    try:
        parse_time_range(string)
        return True
    except ValueError:
        return False


def is_valid_climatological_time_range(string: str) -> bool:
    """Check if given string is a valid climatological time range.

    Parameters
    ----------
    time : str
        String to check.

    Returns
    -------
    bool
        True if given string is a valid climatological time range.
    """
    try:
        parse_time_range(string)
        return string.endswith("-clim")
    except ValueError:
        return False


def parse_isodate(date: str) -> datetime.datetime:
    """Parse a date string in ISO 8601 format.

    Parameters
    ----------
    date : str
        Date string in ISO 8601 to parse.

    Returns
    -------
    datetime.datetime
        Parsed date.
    """
    return datetime.datetime.combine(isodate.parse_date(date), datetime.time.min)


def _parse_isodate_upper_bound(date: str) -> datetime.datetime:
    """Get upper bound of ISO8601 date string, in precision of date string.

    Parses a four-digit year or calendar date string in ISO8601 format
    and returns the upper bound for the time interval defined by the
    precision of the given date (i.e. the strings `1990`, `1990-12` and
    `1990-12-31` will all result in a datetime object with the time
    `1991-01-01T00:00:00`).

    Parameters
    ----------
    date : str
        Date string in ISO8601

    Returns
    -------
    datetime.datetime
        Upper bound of date string.

    Raises
    ------
    ValueError
        If date string could not be parsed.
    """
    for pattern, duration in ISODATE_RELATIVE_DURATIONS.items():
        if re.fullmatch(pattern, date):
            parsed_date = isodate.parse_date(date)
            return datetime.datetime.combine(parsed_date + duration, datetime.time.min)
    raise ValueError(
        "Only four-digit years and calendar dates in ISO8601 format are supported."
    )


def parse_isodate_time_range(time_range: str) -> TimeRange:
    """Parse a time interval in ISO8601 format.

    Parameters
    ----------
    time_range : str
        A time range in ISO8601 format.

    Returns
    -------
    TimeRange
        Extracted TimeRange object.
    """
    try:
        start, end = time_range.split("/")
    except ValueError as e:
        raise ValueError(
            "time range string must contain one and only one slash ('/')"
        ) from e
    if start.startswith("P"):
        end_date = _parse_isodate_upper_bound(end)
        start_date = end_date - isodate.parse_duration(start)
    elif end.startswith("P"):
        start_date = parse_isodate(start)
        end_date = start_date + isodate.parse_duration(end)
    else:
        start_date = parse_isodate(start)
        end_date = _parse_isodate_upper_bound(end)
    if start_date >= end_date:
        raise ValueError("Start date must be earlier than end date.")
    return TimeRange(start_date, end_date, False)
