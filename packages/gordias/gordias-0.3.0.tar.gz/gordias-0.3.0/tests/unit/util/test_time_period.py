"""Module with tests for gordias.util.time_period module."""

from contextlib import nullcontext as does_not_raise

import iris.coords
import iris.cube
import numpy as np
import pytest
from cf_units import Unit

import gordias.util.time_period
import gordias.util.time_string

TEST_CREATE_AUX_COORD_FOR_TIME_RANGE = {
    "test_first_year": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2920).reshape(730, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 730, 1),
                var_name="time",
                standard_name="time",
                units="days since 2022-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2022/2022"),
        does_not_raise(
            iris.coords.AuxCoord(
                var_name="reference_period",
                standard_name="reference_epoch",
                points=182.5,
                bounds=[0, 365],
                units="days since 2022-01-01 00:00:00",
            ),
        ),
    ),
    "test_last_year": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2920).reshape(730, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 730, 1),
                var_name="time",
                standard_name="time",
                units="days since 2022-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2023/2023"),
        does_not_raise(
            iris.coords.AuxCoord(
                var_name="reference_period",
                standard_name="reference_epoch",
                points=547.5,
                bounds=[365, 730],
                units="days since 2022-01-01 00:00:00",
            ),
        ),
    ),
    "test_leap_year": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2924).reshape(731, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 731, 1),
                var_name="time",
                standard_name="time",
                units="days since 2023-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2024/2024"),
        does_not_raise(
            iris.coords.AuxCoord(
                var_name="reference_period",
                standard_name="reference_epoch",
                points=548,
                bounds=[365, 731],
                units="days since 2023-01-01 00:00:00",
            ),
        ),
    ),
    "test_fail": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2924).reshape(731, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 731, 1),
                var_name="time",
                standard_name="time",
                units="days since 2023-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2024/2025"),
        pytest.raises(
            ValueError,
            match=(
                r".* time period .* outside .* time range."
                r" .* <2022-12-31 12:00:00, 2024-12-31 12:00:00>"
            ),
        ),
    ),
}


@pytest.mark.parametrize(
    ("f_cube", "time_range", "expected_output"),
    TEST_CREATE_AUX_COORD_FOR_TIME_RANGE.values(),
    ids=TEST_CREATE_AUX_COORD_FOR_TIME_RANGE.keys(),
    indirect=["f_cube"],
)
def test_create_aux_coord_for_time_range(f_cube, time_range, expected_output):
    """Test function create_aux_coord_for_time_range()."""
    with expected_output:
        assert (
            gordias.util.time_period.create_aux_coord_for_time_range(f_cube, time_range)
            == expected_output.enter_result
        )


TEST_EXTRACT_CUBE_FOR_TIME_RANGE = {
    "test_first_year": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2920).reshape(730, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 730, 1),
                var_name="time",
                standard_name="time",
                units="days since 2022-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2022/2022"),
        does_not_raise(
            iris.cube.Cube(
                data=np.arange(1460).reshape(365, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
                dim_coords_and_dims=[
                    (
                        iris.coords.DimCoord(
                            points=np.arange(0, 365, 1),
                            var_name="time",
                            standard_name="time",
                            units="days since 2022-01-01 00:00:00",
                        ),
                        0,
                    ),
                ],
            ),
        ),
    ),
    "test_last_year": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2920).reshape(730, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 730, 1),
                var_name="time",
                standard_name="time",
                units="days since 2022-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2023/2023"),
        does_not_raise(
            iris.cube.Cube(
                data=np.arange(1460, 2920).reshape(365, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
                dim_coords_and_dims=[
                    (
                        iris.coords.DimCoord(
                            points=np.arange(365, 730, 1),
                            var_name="time",
                            standard_name="time",
                            units="days since 2022-01-01 00:00:00",
                        ),
                        0,
                    ),
                ],
            ),
        ),
    ),
}


@pytest.mark.parametrize(
    ("f_cube", "time_range", "expected_output"),
    TEST_EXTRACT_CUBE_FOR_TIME_RANGE.values(),
    ids=TEST_EXTRACT_CUBE_FOR_TIME_RANGE.keys(),
    indirect=["f_cube"],
)
def test_extract_cube_for_time_range(f_cube, time_range, expected_output):
    """Test function extract_cube_for_time_range()."""
    with expected_output:
        subcube = gordias.util.time_period.extract_cube_for_time_range(
            f_cube, time_range
        )
        assert subcube.shape == expected_output.enter_result.shape
        assert np.array_equal(
            subcube.data, expected_output.enter_result.data, equal_nan=True
        )


TEST_EXTRACT_DATA_FOR_TIME_RANGE = {
    "test_first_year": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2920).reshape(730, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 730, 1),
                var_name="time",
                standard_name="time",
                units="days since 2022-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2022/2022"),
        0,
        does_not_raise(np.arange(1460).reshape(365, 2, 2)),
    ),
    "test_last_year": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2920).reshape(730, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 730, 1),
                var_name="time",
                standard_name="time",
                units="days since 2022-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2023/2023"),
        0,
        does_not_raise(np.arange(1460, 2920).reshape(365, 2, 2)),
    ),
    "test_leap_year": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2924).reshape(731, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 731, 1),
                var_name="time",
                standard_name="time",
                units="days since 2023-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2024/2024"),
        0,
        does_not_raise(np.arange(1460, 2924).reshape(366, 2, 2)),
    ),
    "test_leap_year_with_365_calendar": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2920).reshape(730, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 730, 1),
                var_name="time",
                standard_name="time",
                units=Unit("days since 2023-01-01 00:00:00", calendar="365_day"),
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2024/2024"),
        0,
        does_not_raise(np.arange(1460, 2920).reshape(365, 2, 2)),
    ),
    "test_value_error": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2920).reshape(2, 2, 730),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
                dim_coords_and_dims=(
                    [
                        (
                            iris.coords.DimCoord(
                                points=np.arange(0, 730, 1),
                                var_name="time",
                                standard_name="time",
                                units=Unit(
                                    "days since 2023-01-01 00:00:00", calendar="365_day"
                                ),
                            ),
                            2,
                        )
                    ]
                ),
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2024/2024"),
        0,
        pytest.raises(
            ValueError,
            match=r"Time dimension is expected to be the first dimension. .* ",
        ),
    ),
    "test_padding": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(40).reshape(10, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 10, 1),
                var_name="time",
                standard_name="time",
                units="days since 2022-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2022-01-01/2022-01-10"),
        2,
        does_not_raise(
            np.array(
                [
                    [[0, 1], [2, 3]],
                    [[0, 1], [2, 3]],
                    [[0, 1], [2, 3]],
                    [[4, 5], [6, 7]],
                    [[8, 9], [10, 11]],
                    [[12, 13], [14, 15]],
                    [[16, 17], [18, 19]],
                    [[20, 21], [22, 23]],
                    [[24, 25], [26, 27]],
                    [[28, 29], [30, 31]],
                    [[32, 33], [34, 35]],
                    [[36, 37], [38, 39]],
                    [[36, 37], [38, 39]],
                    [[36, 37], [38, 39]],
                ],
            )
        ),
    ),
}


@pytest.mark.parametrize(
    ("f_cube", "time_range", "padding", "expected_output"),
    TEST_EXTRACT_DATA_FOR_TIME_RANGE.values(),
    ids=TEST_EXTRACT_DATA_FOR_TIME_RANGE.keys(),
    indirect=["f_cube"],
)
def test_extract_data_for_time_range(f_cube, time_range, padding, expected_output):
    """Test funtion extract_data_for_time_range()."""
    with expected_output:
        ref_data = gordias.util.time_period.extract_data_for_time_range(
            f_cube, time_range, padding
        )
        assert np.array_equal(ref_data, expected_output.enter_result, equal_nan=True)


TEST_TEST_GET_TIME_RANGE_BOUNDS = {
    "test_one_year": (
        gordias.util.time_string.parse_isodate_time_range("2023/2023"),
        Unit("days since 2023-01-01 00:00:00", calendar="standard"),
        does_not_raise((0, 365)),
    ),
    "test_one_leap_year": (
        gordias.util.time_string.parse_isodate_time_range("2024/2024"),
        Unit("days since 2024-01-01 00:00:00", calendar="standard"),
        does_not_raise((0, 366)),
    ),
    "test_two_years": (
        gordias.util.time_string.parse_isodate_time_range("2022/2023"),
        Unit("days since 2022-01-01 00:00:00", calendar="standard"),
        does_not_raise((0, 730)),
    ),
    "test_two_years_with_leap_year": (
        gordias.util.time_string.parse_isodate_time_range("2023/2024"),
        Unit("days since 2023-01-01 00:00:00", calendar="standard"),
        does_not_raise((0, 731)),
    ),
    "test_included_last_day_leap_year": (
        gordias.util.time_string.parse_isodate_time_range("2023-01-01/2024-12-31"),
        Unit("days since 2023-01-01 00:00:00", calendar="standard"),
        does_not_raise((0, 731)),
    ),
}


@pytest.mark.parametrize(
    ("time_range", "unit", "expected_output"),
    TEST_TEST_GET_TIME_RANGE_BOUNDS.values(),
    ids=TEST_TEST_GET_TIME_RANGE_BOUNDS.keys(),
)
def test_get_time_range_bounds(time_range, unit, expected_output):
    """Test function get_time_range_bounds()."""
    with expected_output:
        assert (
            gordias.util.time_period.get_time_range_bounds(time_range, unit)
            == expected_output.enter_result
        )


TEST_GET_FIRST_AND_LAST_INDICES = {
    "test_one_year": (
        gordias.util.time_string.parse_isodate_time_range("2023/2023"),
        "standard",
        gordias.util.time_string.TimesHelper(
            iris.coords.DimCoord(
                np.arange(0, 731),
                units=Unit("days since 2023-01-01 00:00:00", calendar="standard"),
            )
        ),
        does_not_raise((0, 364)),
    ),
    "test_a_couple_of_days": (
        gordias.util.time_string.parse_isodate_time_range("2023-01-02/2023-01-12"),
        "standard",
        gordias.util.time_string.TimesHelper(
            iris.coords.DimCoord(
                np.arange(0, 365),
                units=Unit("days since 2023-01-01 00:00:00", calendar="standard"),
            )
        ),
        does_not_raise((1, 11)),
    ),
    "test_unit_seconds 2023-01-02 00:00:00/2023-01-12 59:59:59": (
        gordias.util.time_string.parse_isodate_time_range("2023-01-02/2023-01-12"),
        "standard",
        gordias.util.time_string.TimesHelper(
            iris.coords.DimCoord(
                np.arange(0, 2000000, 1),
                units=Unit("seconds since 2023-01-01 00:00:00", calendar="standard"),
            )
        ),
        does_not_raise((86400, 1036799)),
    ),
    "test_unit_hours_and_time_is_not_exact": (
        gordias.util.time_string.parse_isodate_time_range("2023-01-01/2023-01-02"),
        "standard",
        gordias.util.time_string.TimesHelper(
            iris.coords.DimCoord(
                np.arange(0.5, 100.5, 1),
                units=Unit("hours since 2023-01-01 00:00:00", calendar="standard"),
            )
        ),
        does_not_raise((0, 47)),
    ),
    "test_unit_days_and_time_is_not_exact": (
        gordias.util.time_string.parse_isodate_time_range("2022/2022-01-02"),
        "standard",
        gordias.util.time_string.TimesHelper(
            iris.coords.DimCoord(
                np.arange(0.5, 365.5, 1),
                units=Unit("days since 2022-01-01 00:00:00", calendar="standard"),
            )
        ),
        does_not_raise((0, 1)),
    ),
    "test_different_time_units": (
        gordias.util.time_string.parse_isodate_time_range("2022/2022"),
        "standard",
        gordias.util.time_string.TimesHelper(
            iris.coords.DimCoord(
                np.arange(0.5, 8770.5, 1),
                units=Unit("hours since 2022-01-01 00:00:00", calendar="standard"),
            )
        ),
        does_not_raise((0, 8759)),
    ),
    "test_different_calendar": (
        gordias.util.time_string.parse_isodate_time_range("2022/2022"),
        "proleptic_gregorian",
        gordias.util.time_string.TimesHelper(
            iris.coords.DimCoord(
                np.arange(0.5, 8770.5, 1),
                units=Unit("hours since 2022-01-01 00:00:00", calendar="standard"),
            )
        ),
        does_not_raise((0, 8759)),
    ),
    "test_one_year_P1Y/2022": (
        gordias.util.time_string.parse_isodate_time_range("P1Y/2022"),
        "standard",
        gordias.util.time_string.TimesHelper(
            iris.coords.DimCoord(
                np.arange(0, 731),
                units=Unit("days since 2022-01-01 00:00:00", calendar="standard"),
            )
        ),
        does_not_raise((0, 364)),
    ),
}


@pytest.mark.parametrize(
    ("time_range", "calendar", "times", "expected_output"),
    TEST_GET_FIRST_AND_LAST_INDICES.values(),
    ids=TEST_GET_FIRST_AND_LAST_INDICES.keys(),
)
def test_get_first_and_last_indices(time_range, calendar, times, expected_output):
    """Test function get_first_and_last_indices()."""
    with expected_output:
        assert (
            gordias.util.time_period.get_first_and_last_indices(
                time_range, times, calendar
            )
            == expected_output.enter_result
        )


TEST_GET_TIMES_HELPER = {
    "test": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(40).reshape(10, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 10, 1),
                var_name="time",
                standard_name="time",
                units="days since 2022-01-01 00:00:00",
            ),
        },
        does_not_raise(
            gordias.util.time_string.TimesHelper(
                iris.coords.DimCoord(
                    points=np.arange(0, 10, 1),
                    var_name="time",
                    standard_name="time",
                    units="days since 2022-01-01 00:00:00",
                )
            ),
        ),
    )
}


@pytest.mark.parametrize(
    ("f_cube", "expected_output"),
    TEST_GET_TIMES_HELPER.values(),
    ids=TEST_GET_TIMES_HELPER.keys(),
    indirect=["f_cube"],
)
def test_get_times_helper(f_cube, expected_output):
    """Test function get_times_helper()."""
    with expected_output:
        assert np.array_equal(
            gordias.util.time_period.get_times_helper(f_cube).times,
            expected_output.enter_result.times,
        )
        assert (
            gordias.util.time_period.get_times_helper(f_cube).units
            == expected_output.enter_result.units
        )


TEST_VALIDATE_TIME_BOUNDS = {
    "test_first_year": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2920).reshape(730, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 730, 1),
                var_name="time",
                standard_name="time",
                units="days since 2022-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2022/2022"),
        does_not_raise(),
    ),
    "test_last_year": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2920).reshape(730, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 730, 1),
                var_name="time",
                standard_name="time",
                units="days since 2022-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2023/2023"),
        does_not_raise(),
    ),
    "test_leap_year": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2924).reshape(731, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 731, 1),
                var_name="time",
                standard_name="time",
                units="days since 2023-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2024/2024"),
        does_not_raise(),
    ),
    "test_fail": (
        {
            "cube": iris.cube.Cube(
                data=np.arange(2924).reshape(731, 2, 2),
                standard_name="air_temperature",
                var_name="tas",
                units="degree_Celsius",
            ),
            "dim_coord_time": iris.coords.DimCoord(
                points=np.arange(0, 731, 1),
                var_name="time",
                standard_name="time",
                units="days since 2023-01-01 00:00:00",
            ),
        },
        gordias.util.time_string.parse_isodate_time_range("2024/2025"),
        pytest.raises(
            ValueError,
            match=(
                r".* time period .* outside .* time range."
                r" .* <2022-12-31 12:00:00, 2024-12-31 12:00:00>"
            ),
        ),
    ),
}


@pytest.mark.parametrize(
    ("f_cube", "time_range", "expected_output"),
    TEST_VALIDATE_TIME_BOUNDS.values(),
    ids=TEST_VALIDATE_TIME_BOUNDS.keys(),
    indirect=["f_cube"],
)
def test_validate_time_bounds(f_cube, time_range, expected_output):
    """Test function validate_time_bounds()."""
    with expected_output:
        assert (
            gordias.util.time_period.validate_time_bounds(f_cube, time_range)
            == expected_output.enter_result
        )
