"""Module with tests for gordias.util.cmip_path module."""

import datetime
import pathlib
from contextlib import nullcontext as does_not_raise

import pytest

from gordias.util import cmip_path, time_string

TEST_GET_STEM_BASE_PART = {
    "normal_case": (
        "tas_e1_historical_e3_day_19700101-19801231.nc",
        "e1_historical_e3_day",
    ),
    "single_time": ("tas_e1_historical_e3_day_19700101.nc", "e1_historical_e3_day"),
    "no_time_range": ("tas_e1_historical_e3_day.nc", "e1_historical_e3_day"),
}


@pytest.mark.parametrize(
    ("filename", "expected_output"),
    TEST_GET_STEM_BASE_PART.values(),
    ids=TEST_GET_STEM_BASE_PART.keys(),
)
def test_get_stem_base_part(filename, expected_output):
    """Test `get_stem_base_part`."""
    output_template = cmip_path.get_stem_base_part(pathlib.Path(filename))
    assert output_template == expected_output


TEST_GET_STEM_TIME_RANGE_PART = {
    "normal_case": (
        "tas_e1_historical_e3_day_19700101-19801231.nc",
        "19700101-19801231",
    ),
    "single_time": ("tas_e1_historical_e3_day_19700101.nc", "19700101"),
    "no_time_range": ("tas_e1_historical_e3_day.nc", ""),
}


@pytest.mark.parametrize(
    ("filename", "expected_output"),
    TEST_GET_STEM_TIME_RANGE_PART.values(),
    ids=TEST_GET_STEM_TIME_RANGE_PART.keys(),
)
def test_get_stem_time_range_part(filename, expected_output):
    """Test `get_stem_time_range_part`."""
    output_template = cmip_path.get_stem_time_range_part(pathlib.Path(filename))
    assert output_template == expected_output


TEST_GET_STEM_TIME_RANGE_PART = {
    "normal_case": (
        "tas_e1_historical_e3_day_19700101-19801231.nc",
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(1970, 1, 1),
                datetime.datetime(1980, 12, 31),
                False,
            )
        ),
    ),
    "single_time": (
        "tas_e1_historical_e3_day_19700101.nc",
        does_not_raise(
            time_string.TimeRange(
                datetime.datetime(1970, 1, 1),
                datetime.datetime(1970, 1, 1),
                False,
            )
        ),
    ),
    "no_time_range": (
        "tas_e1_historical_e3_day.nc",
        pytest.raises(ValueError, match="Filename stem does not include time range"),
    ),
}


@pytest.mark.parametrize(
    ("filename", "expected_output"),
    TEST_GET_STEM_TIME_RANGE_PART.values(),
    ids=TEST_GET_STEM_TIME_RANGE_PART.keys(),
)
def test_get_stem_time_range(filename, expected_output):
    """Test `get_stem_time_range`."""
    with expected_output:
        output_template = cmip_path.get_stem_time_range(pathlib.Path(filename))
        assert output_template == expected_output.enter_result


TEST_FILE_LIST_TO_BUILD_FILENAME_TEMPLATE = {
    "single_file_time": (
        ["tas_e1_historical_e3_day_19700101.nc"],
        True,
        False,
        "{var_name}_e1_historical_e3_{frequency}_19700101-19700101.nc",
    ),
    "single_file_time_range": (
        ["tas_e1_historical_e3_day_19700101-19801231.nc"],
        True,
        False,
        "{var_name}_e1_historical_e3_{frequency}_19700101-19801231.nc",
    ),
    "multiple_files_default": (
        [
            "tas_e1_historical_e3_day_19710101-19801231.nc",
            "tas_e1_historical_e3_day_19810101-19901231.nc",
        ],
        True,
        False,
        "{var_name}_e1_historical_e3_{frequency}_19710101-19901231.nc",
    ),
    "multiple_files_historical_rcp26": (
        [
            "tas_e1_historical_e3_day_19910101-20001231.nc",
            "tas_e1_rcp26_e3_day_20010101-20101231.nc",
        ],
        True,
        False,
        "{var_name}_e1_historical-rcp26_e3_{frequency}_19910101-20101231.nc",
    ),
    "multiple_files_historical_rcp85": (
        [
            "tas_e1_historical_e3_day_19910101-20001231.nc",
            "tas_e1_rcp85_e3_day_20010101-20101231.nc",
        ],
        True,
        False,
        "{var_name}_e1_historical-rcp85_e3_{frequency}_19910101-20101231.nc",
    ),
    "multiple_files_historical_ssp119": (
        [
            "tas_e1_historical_e3_day_19910101-20001231.nc",
            "tas_e1_ssp119_e3_day_20010101-20101231.nc",
        ],
        True,
        False,
        "{var_name}_e1_historical-ssp119_e3_{frequency}_19910101-20101231.nc",
    ),
    "multiple_files_historical_ssp585": (
        [
            "tas_e1_historical_e3_day_19910101-20001231.nc",
            "tas_e1_ssp585_e3_day_20010101-20101231.nc",
        ],
        True,
        False,
        "{var_name}_e1_historical-ssp585_e3_{frequency}_19910101-20101231.nc",
    ),
    "single_file_no_time_range": (
        ["tas_e1_historical_e3_day.nc"],
        True,
        False,
        "{var_name}_e1_historical_e3_{frequency}.nc",
    ),
    "multiple_files_exclude_time_range": (
        [
            "tas_e1_historical_e3_day_19710101-19801231.nc",
            "tas_e1_historical_e3_day_19810101-19901231.nc",
        ],
        False,
        False,
        "{var_name}_e1_historical_e3_{frequency}.nc",
    ),
    "multiple_files_time_range_placeholder": (
        [
            "tas_e1_historical_e3_day_19710101-19801231.nc",
            "tas_e1_historical_e3_day_19810101-19901231.nc",
        ],
        True,
        True,
        "{var_name}_e1_historical_e3_{frequency}_{start}-{end}.nc",
    ),
    "single_file_not_cmip_or_cordex": (
        ["file.nc"],
        True,
        False,
        "{var_name}_{frequency}.nc",
    ),
}


@pytest.mark.parametrize(
    ("file_list", "include_time_range", "template_time_range", "expected_output"),
    TEST_FILE_LIST_TO_BUILD_FILENAME_TEMPLATE.values(),
    ids=TEST_FILE_LIST_TO_BUILD_FILENAME_TEMPLATE.keys(),
)
def test_build_cmip_like_filename_template(
    file_list, include_time_range, template_time_range, expected_output
):
    """Test `build_cmip_like_filename_template`."""
    output_template = cmip_path.build_cmip_like_filename_template(
        file_list,
        include_time_range=include_time_range,
        time_range_placeholder=template_time_range,
    )
    assert output_template == expected_output
