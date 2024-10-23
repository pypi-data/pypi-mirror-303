"""Module with tests for gordias.util.time_string module."""

import datetime
from contextlib import nullcontext as does_not_raise

import pytest

from gordias.util import time_string

TEST_TIME_STRINGS = {
    "2001": ("2001", does_not_raise(datetime.datetime(2001, 1, 1))),
    "200102": ("200102", does_not_raise(datetime.datetime(2001, 2, 1))),
    "20010203": ("20010203", does_not_raise(datetime.datetime(2001, 2, 3))),
    "2001020304": ("2001020304", does_not_raise(datetime.datetime(2001, 2, 3, 4))),
    "200102030405": (
        "200102030405",
        does_not_raise(datetime.datetime(2001, 2, 3, 4, 5)),
    ),
    "20010203040506": (
        "20010203040506",
        does_not_raise(datetime.datetime(2001, 2, 3, 4, 5, 6)),
    ),
    "20011": ("20011", pytest.raises(ValueError, match="Invalid time string 20011")),
}


@pytest.mark.parametrize(
    ("string", "expected_output"),
    TEST_TIME_STRINGS.values(),
    ids=TEST_TIME_STRINGS.keys(),
)
def test_parse_time(string, expected_output):
    """Test `parse_time`."""
    with expected_output:
        assert time_string.parse_time(string) == expected_output.enter_result


@pytest.mark.parametrize(
    ("string", "expected_output"),
    TEST_TIME_STRINGS.values(),
    ids=TEST_TIME_STRINGS.keys(),
)
def test_is_valid_time(string, expected_output):
    """Test `is_valid_time`."""
    if isinstance(expected_output, does_not_raise):
        assert time_string.is_valid_time(string)
    else:
        assert not time_string.is_valid_time(string)


TEST_TIME_RANGE_STRINGS = {
    "2001-2002": (
        "2001-2002",
        False,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 1, 1),
                datetime.datetime(2002, 1, 1),
                False,
            )
        ),
    ),
    "2001-2002-clim": (
        "2001-2002-clim",
        False,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 1, 1),
                datetime.datetime(2002, 1, 1),
                True,
            )
        ),
    ),
    "2001-2002-inclusive": (
        "2001-2002",
        True,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 1, 1),
                datetime.datetime(2003, 1, 1),
                False,
            )
        ),
    ),
    "200102-200203": (
        "200102-200203",
        False,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 2, 1),
                datetime.datetime(2002, 3, 1),
                False,
            )
        ),
    ),
    "200102-200203-inclusive": (
        "200102-200203",
        True,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 2, 1),
                datetime.datetime(2002, 4, 1),
                False,
            )
        ),
    ),
    "200102-200212-inclusive-december": (
        "200102-200212",
        True,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 2, 1),
                datetime.datetime(2003, 1, 1),
                False,
            )
        ),
    ),
    "20010203-20020304": (
        "20010203-20020304",
        False,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 2, 3),
                datetime.datetime(2002, 3, 4),
                False,
            )
        ),
    ),
    "20010203-20020304-inclusive": (
        "20010203-20020304",
        True,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 2, 3),
                datetime.datetime(2002, 3, 5),
                False,
            )
        ),
    ),
    "2001020304-2002030405": (
        "2001020304-2002030405",
        False,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 2, 3, 4),
                datetime.datetime(2002, 3, 4, 5),
                False,
            )
        ),
    ),
    "2001020304-2002030405-inclusive": (
        "2001020304-2002030405",
        True,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 2, 3, 4),
                datetime.datetime(2002, 3, 4, 6),
                False,
            )
        ),
    ),
    "200102030405-200203040506": (
        "200102030405-200203040506",
        False,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 2, 3, 4, 5),
                datetime.datetime(2002, 3, 4, 5, 6),
                False,
            )
        ),
    ),
    "200102030405-200203040506-inclusive": (
        "200102030405-200203040506",
        True,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 2, 3, 4, 5),
                datetime.datetime(2002, 3, 4, 5, 7),
                False,
            )
        ),
    ),
    "20010203040506-20020304050607": (
        "20010203040506-20020304050607",
        False,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 2, 3, 4, 5, 6),
                datetime.datetime(2002, 3, 4, 5, 6, 7),
                False,
            )
        ),
    ),
    "20010203040506-20020304050607-inclusive": (
        "20010203040506-20020304050607",
        True,
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(2001, 2, 3, 4, 5, 6),
                datetime.datetime(2002, 3, 4, 5, 6, 8),
                False,
            )
        ),
    ),
    "2001-2002-2003": (
        "2001-2002-2003",
        False,
        pytest.raises(ValueError, match="Invalid time range 2001-2002-2003"),
    ),
    "2001_2002": (
        "2001_2002",
        False,
        pytest.raises(ValueError, match="Invalid time range 2001_2002"),
    ),
    "2001-200201": (
        "2001-200201",
        False,
        pytest.raises(
            ValueError,
            match="Start and end time must have the same resolution in 2001-200201",
        ),
    ),
    "2002-2001": (
        "2002-2001",
        False,
        pytest.raises(ValueError, match="Invalid time range 2002-2001"),
    ),
}


@pytest.mark.parametrize(
    ("string", "end_inclusive", "expected_output"),
    TEST_TIME_RANGE_STRINGS.values(),
    ids=TEST_TIME_RANGE_STRINGS.keys(),
)
def test_parse_time_range(string, end_inclusive, expected_output):
    """Test `parse_time_range`."""
    with expected_output:
        assert (
            time_string.parse_time_range(string, end_inclusive=end_inclusive)
            == expected_output.enter_result
        )


@pytest.mark.parametrize(
    ("string", "end_inclusive", "expected_output"),
    TEST_TIME_RANGE_STRINGS.values(),
    ids=TEST_TIME_RANGE_STRINGS.keys(),
)
def test_is_valid_time_range(string, end_inclusive, expected_output):  # noqa: ARG001
    """Test `is_valid_time_range`."""
    if isinstance(expected_output, does_not_raise):
        assert time_string.is_valid_time_range(string)
    else:
        assert not time_string.is_valid_time_range(string)


TEST_CLIMATOLOGICAL_TIME_RANGE_STRINGS = {
    "1970-2000-clim": ("1970-2000-clim", True),
    "1970-2000": ("1970-2000", False),
    "1970-2000-other": ("1970-2000-other", False),
}


@pytest.mark.parametrize(
    ("string", "expected_output"),
    TEST_CLIMATOLOGICAL_TIME_RANGE_STRINGS.values(),
    ids=TEST_CLIMATOLOGICAL_TIME_RANGE_STRINGS.keys(),
)
def test_is_valid_climatological_time_range(string, expected_output):
    """Test `is_valid_climatological_time_range`."""
    assert time_string.is_valid_climatological_time_range(string) == expected_output


TEST_PARSE_ISODATE_PARAMETERS = {
    "1961": ("1961", datetime.datetime(1961, 1, 1)),
    "2050": ("2050", datetime.datetime(2050, 1, 1)),
    "2010-01": ("2010-01", datetime.datetime(2010, 1, 1)),
    "2010-07": ("2010-07", datetime.datetime(2010, 7, 1)),
    "2010-01-01": ("2010-01-01", datetime.datetime(2010, 1, 1)),
    "2010-07-26": ("2010-07-26", datetime.datetime(2010, 7, 26)),
}


@pytest.mark.parametrize(
    ("date", "expected"),
    TEST_PARSE_ISODATE_PARAMETERS.values(),
    ids=TEST_PARSE_ISODATE_PARAMETERS.keys(),
)
def test_parse_isodate(date, expected):
    """Test `test_parse_isodate`."""
    assert time_string.parse_isodate(date) == expected


TEST_PARSE_ISODATE_UPPER_BOUND_PARAMETERS = {
    "1961": ("1961", datetime.datetime(1962, 1, 1)),
    "2050": ("2050", datetime.datetime(2051, 1, 1)),
    "2010-01": ("2010-01", datetime.datetime(2010, 2, 1)),
    "2010-07": ("2010-07", datetime.datetime(2010, 8, 1)),
    "2010-01-01": ("2010-01-01", datetime.datetime(2010, 1, 2)),
    "2010-07-26": ("2010-07-26", datetime.datetime(2010, 7, 27)),
}


@pytest.mark.parametrize(
    ("date", "expected"),
    TEST_PARSE_ISODATE_UPPER_BOUND_PARAMETERS.values(),
    ids=TEST_PARSE_ISODATE_UPPER_BOUND_PARAMETERS.keys(),
)
def test_parse_isodate_upper_bound(date, expected):
    """Test `test_parse_isodate_upper_bound`."""
    assert time_string._parse_isodate_upper_bound(date) == expected


TEST_PARSE_ISODATE_TIMERANGE_PARAMETERS = {
    "1961/1990": (
        "1961/1990",
        time_string.TimeRange(
            datetime.datetime(1961, 1, 1),
            datetime.datetime(1991, 1, 1),
            False,
        ),
    ),
    "2010/2050": (
        "2010/2050",
        time_string.TimeRange(
            datetime.datetime(2010, 1, 1),
            datetime.datetime(2051, 1, 1),
            False,
        ),
    ),
    "1961-01/2050-01": (
        "1961-01/2050-01",
        time_string.TimeRange(
            datetime.datetime(1961, 1, 1),
            datetime.datetime(2050, 2, 1),
            False,
        ),
    ),
    "P20Y/1990": (
        "P20Y/1990",
        time_string.TimeRange(
            datetime.datetime(1971, 1, 1),
            datetime.datetime(1991, 1, 1),
            False,
        ),
    ),
    "1961/P20Y": (
        "1961/P20Y",
        time_string.TimeRange(
            datetime.datetime(1961, 1, 1),
            datetime.datetime(1981, 1, 1),
            False,
        ),
    ),
    "P20Y6M/1990": (
        "P20Y6M/1990",
        time_string.TimeRange(
            datetime.datetime(1970, 7, 1),
            datetime.datetime(1991, 1, 1),
            False,
        ),
    ),
    "1961/P20Y6M": (
        "1961/P20Y6M",
        time_string.TimeRange(
            datetime.datetime(1961, 1, 1),
            datetime.datetime(1981, 7, 1),
            False,
        ),
    ),
}


@pytest.mark.parametrize(
    ("time_range", "expected"),
    TEST_PARSE_ISODATE_TIMERANGE_PARAMETERS.values(),
    ids=TEST_PARSE_ISODATE_TIMERANGE_PARAMETERS.keys(),
)
def test_parse_isodate_time_range(time_range, expected):
    """Test `test_parse_isodate_time_range`."""
    assert time_string.parse_isodate_time_range(time_range) == expected
