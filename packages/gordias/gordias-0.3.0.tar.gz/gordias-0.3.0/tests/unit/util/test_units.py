"""Module with tests for gordias.util.units module."""

from contextlib import nullcontext as does_not_raise

import cf_units
import iris.coords
import numpy as np
import pytest

from gordias.util import units

TEST_IS_PRECIPITATION = {
    "lwe_precipitation_rate": ("lwe_precipitation_rate", True),
    "lwe_thickness_of_precipitation_amount": (
        "lwe_thickness_of_precipitation_amount",
        True,
    ),
    "thickness_of_rainfall_amount": ("thickness_of_rainfall_amount", True),
    "precipitation_amount": ("precipitation_amount", True),
    "precipitation_flux": ("precipitation_flux", True),
    "air_temperature": ("air_temperature", False),
    "lwe_thickness_of_snowfall_amount": ("lwe_thickness_of_snowfall_amount", False),
}


@pytest.mark.parametrize(
    ("string", "expected_output"),
    TEST_IS_PRECIPITATION.values(),
    ids=TEST_IS_PRECIPITATION.keys(),
)
def test_is_precipitation(string, expected_output):
    """Test `is_precipitation`."""
    assert units.is_precipitation(string) == expected_output


TEST_GET_STANDARD_NAME_FOR_PRECIPITATION_UNIT = {
    "lwe_precipitation_rate": (
        cf_units.Unit("m s-1"),
        does_not_raise("lwe_precipitation_rate"),
    ),
    "lwe_thickness_of_precipitation_amount": (
        cf_units.Unit("m"),
        does_not_raise("lwe_thickness_of_precipitation_amount"),
    ),
    "precipitation_amount": (
        cf_units.Unit("kg m-2"),
        does_not_raise("precipitation_amount"),
    ),
    "precipitation_flux": (
        cf_units.Unit("kg m-2 s-1"),
        does_not_raise("precipitation_flux"),
    ),
    "air_temperature": (cf_units.Unit("K"), pytest.raises(ValueError, match="...")),
}


@pytest.mark.parametrize(
    ("string", "expected_output"),
    TEST_GET_STANDARD_NAME_FOR_PRECIPITATION_UNIT.values(),
    ids=TEST_GET_STANDARD_NAME_FOR_PRECIPITATION_UNIT.keys(),
)
def test_get_standard_name_for_precipitation_unit(string, expected_output):
    """Test `get_standard_name_for_precipitation_unit`."""
    with expected_output:
        assert (
            units.get_standard_name_for_precipitation_unit(string)
            == expected_output.enter_result
        )


TEST_ENSURE_PRECIPITATION_UNIT_AND_STANDARD_NAME = {
    "lwe_precipitation_rate_complete": (
        cf_units.Unit("m s-1"),
        "lwe_precipitation_rate",
        does_not_raise((cf_units.Unit("m s-1"), "lwe_precipitation_rate")),
    ),
    "lwe_precipitation_rate_unit": (
        cf_units.Unit("m s-1"),
        None,
        does_not_raise((cf_units.Unit("m s-1"), "lwe_precipitation_rate")),
    ),
    "lwe_precipitation_rate_standard_name": (
        None,
        "lwe_precipitation_rate",
        does_not_raise((cf_units.Unit("m s-1"), "lwe_precipitation_rate")),
    ),
    "bad_pair": (
        cf_units.Unit("m"),
        "lwe_precipitation_rate",
        pytest.raises(
            ValueError,
            match="Unit m does not match standard_name lwe_precipitation_rate.",
        ),
    ),
    "none": (
        None,
        None,
        pytest.raises(ValueError, match="No unit or standard name is given."),
    ),
    "not_precipitation": (
        cf_units.Unit("K"),
        "air_temperature",
        pytest.raises(
            ValueError, match="Unknown precipitation standard name air_temperature"
        ),
    ),
}


@pytest.mark.parametrize(
    ("unit", "string", "expected_output"),
    TEST_ENSURE_PRECIPITATION_UNIT_AND_STANDARD_NAME.values(),
    ids=TEST_ENSURE_PRECIPITATION_UNIT_AND_STANDARD_NAME.keys(),
)
def test_ensure_precipitation_unit_and_standard_name(unit, string, expected_output):
    """Test `ensure_precipitation_unit_and_standard_name`."""
    with expected_output:
        assert (
            units.ensure_precipitation_unit_and_standard_name(unit, string)
            == expected_output.enter_result
        )


TEST_GET_PRECIPITATION_RATE_CONVERSION = {
    "lwe_precipitation_rate-to-lwe_thickness_of_precipitation_amount": (
        units.PRECIPITATION_INFO["lwe_precipitation_rate"],
        units.PRECIPITATION_INFO["lwe_thickness_of_precipitation_amount"],
        cf_units.Unit("1 day"),
        does_not_raise(cf_units.Unit("1 day")),
    ),
    "lwe_thickness_of_precipitation_amount-to-lwe_precipitation_rate": (
        units.PRECIPITATION_INFO["lwe_thickness_of_precipitation_amount"],
        units.PRECIPITATION_INFO["lwe_precipitation_rate"],
        cf_units.Unit("1 day"),
        does_not_raise(cf_units.Unit("1 day-1")),
    ),
    "lwe_thickness_of_precipitation_amount-to-thickness_of_rainfall_amount": (
        units.PRECIPITATION_INFO["lwe_thickness_of_precipitation_amount"],
        units.PRECIPITATION_INFO["thickness_of_rainfall_amount"],
        cf_units.Unit("1 day"),
        does_not_raise(cf_units.Unit(1.0)),
    ),
    "lwe_precipitation_rate-to-precipitation_flux": (
        units.PRECIPITATION_INFO["lwe_precipitation_rate"],
        units.PRECIPITATION_INFO["precipitation_flux"],
        cf_units.Unit("1 day"),
        does_not_raise(cf_units.Unit(1.0)),
    ),
    "integration_time_not_time_unit": (
        units.PRECIPITATION_INFO["lwe_precipitation_rate"],
        units.PRECIPITATION_INFO["lwe_thickness_of_precipitation_amount"],
        cf_units.Unit("kg"),
        pytest.raises(
            ValueError, match="Integration time argument must be a time unit"
        ),
    ),
}


@pytest.mark.parametrize(
    ("old_quantity", "new_quantity", "integration_time", "expected_output"),
    TEST_GET_PRECIPITATION_RATE_CONVERSION.values(),
    ids=TEST_GET_PRECIPITATION_RATE_CONVERSION.keys(),
)
def test_get_precipitation_rate_conversion(
    old_quantity, new_quantity, integration_time, expected_output
):
    """Test `get_precipitation_rate_conversion`."""
    with expected_output:
        assert (
            units.get_precipitation_rate_conversion(
                old_quantity, new_quantity, integration_time
            )
            == expected_output.enter_result
        )


TEST_GET_PRECIPITATION_MASS_CONVERSION = {
    "lwe_precipitation_rate-to-precipitation_flux": (
        units.PRECIPITATION_INFO["lwe_precipitation_rate"],
        units.PRECIPITATION_INFO["precipitation_flux"],
        units.DENSITY_WATER,
        does_not_raise(units.DENSITY_WATER),
    ),
    "precipitation_flux-to-lwe_precipitation_rate": (
        units.PRECIPITATION_INFO["precipitation_flux"],
        units.PRECIPITATION_INFO["lwe_precipitation_rate"],
        units.DENSITY_WATER,
        does_not_raise(units.DENSITY_WATER.invert()),
    ),
    "precipitation_amount-to-precipitation_flux": (
        units.PRECIPITATION_INFO["precipitation_amount"],
        units.PRECIPITATION_INFO["precipitation_flux"],
        units.DENSITY_WATER,
        does_not_raise(cf_units.Unit(1.0)),
    ),
    "precipitation_flux-to-precipitation_amount": (
        units.PRECIPITATION_INFO["precipitation_flux"],
        units.PRECIPITATION_INFO["precipitation_amount"],
        units.DENSITY_WATER,
        does_not_raise(cf_units.Unit(1.0)),
    ),
    "density_not_density_unit": (
        units.PRECIPITATION_INFO["lwe_precipitation_rate"],
        units.PRECIPITATION_INFO["precipitation_flux"],
        cf_units.Unit("1 day"),
        pytest.raises(ValueError, match="Density argument must be a density unit"),
    ),
}


@pytest.mark.parametrize(
    ("old_quantity", "new_quantity", "integration_time", "expected_output"),
    TEST_GET_PRECIPITATION_MASS_CONVERSION.values(),
    ids=TEST_GET_PRECIPITATION_MASS_CONVERSION.keys(),
)
def test_get_precipitation_mass_conversion(
    old_quantity, new_quantity, integration_time, expected_output
):
    """Test `get_precipitation_mass_conversion`."""
    with expected_output:
        assert (
            units.get_precipitation_mass_conversion(
                old_quantity, new_quantity, integration_time
            )
            == expected_output.enter_result
        )


TEST_CHANGE_PRECIPITATION_UNIT = {
    "lwe_precipitation_rate-to-precipitation_flux": (
        iris.coords.AuxCoord(
            np.array([1.0, 2.0], dtype=np.float32),
            standard_name="lwe_precipitation_rate",
            units=cf_units.Unit("m s-1"),
        ),
        "kg m-2 s-1",
        "precipitation_flux",
        does_not_raise(
            iris.coords.AuxCoord(
                np.array([1000.0, 2000.0], dtype=np.float32),
                standard_name="precipitation_flux",
                units=cf_units.Unit("kg m-2 s-1"),
            )
        ),
    ),
    "precipitation_amount-to-precipitation_flux": (
        iris.coords.AuxCoord(
            np.array([1.0, 2.0], dtype=np.float32),
            standard_name="precipitation_amount",
            units=cf_units.Unit("kg m-2"),
        ),
        "kg m-2 s-1",
        "precipitation_flux",
        does_not_raise(
            iris.coords.AuxCoord(
                np.array([1.157e-05, 2.315e-05], dtype=np.float32),
                standard_name="precipitation_flux",
                units=cf_units.Unit("kg m-2 s-1"),
            )
        ),
    ),
}


@pytest.mark.parametrize(
    ("coord", "new_unit", "new_standard_name", "expected_output"),
    TEST_CHANGE_PRECIPITATION_UNIT.values(),
    ids=TEST_CHANGE_PRECIPITATION_UNIT.keys(),
)
def test_change_precipitation_units(
    coord, new_unit, new_standard_name, expected_output
):
    """Test `change_precipitation_units`."""
    with expected_output:
        units.change_precipitation_units(coord, new_unit, new_standard_name)
        assert coord.units == expected_output.enter_result.units
        assert coord.standard_name == expected_output.enter_result.standard_name
        assert np.allclose(coord.points, expected_output.enter_result.points)


TEST_CHANGE_UNIT = {
    "lwe_precipitation_rate-to-precipitation_flux": (
        iris.coords.AuxCoord(
            np.array([1.0, 2.0], dtype=np.float32),
            standard_name="lwe_precipitation_rate",
            units=cf_units.Unit("m s-1"),
        ),
        "kg m-2 s-1",
        "precipitation_flux",
        does_not_raise(
            iris.coords.AuxCoord(
                np.array([1000.0, 2000.0], dtype=np.float32),
                standard_name="precipitation_flux",
                units=cf_units.Unit("kg m-2 s-1"),
            )
        ),
    ),
    "air_temperature_celsius-to-air_temperature_kelvin": (
        iris.coords.AuxCoord(
            np.array([1.0, 2.0], dtype=np.float32),
            standard_name="air_temperature",
            units=cf_units.Unit("degree_Celsius"),
        ),
        "K",
        "air_temperature",
        does_not_raise(
            iris.coords.AuxCoord(
                np.array([274.15, 275.15], dtype=np.float32),
                standard_name="air_temperature",
                units=cf_units.Unit("K"),
            )
        ),
    ),
}


@pytest.mark.parametrize(
    ("coord", "new_unit", "new_standard_name", "expected_output"),
    TEST_CHANGE_UNIT.values(),
    ids=TEST_CHANGE_UNIT.keys(),
)
def test_change_units(coord, new_unit, new_standard_name, expected_output):
    """Test `change_units`."""
    with expected_output:
        units.change_units(coord, new_unit, new_standard_name)
        assert coord.units == expected_output.enter_result.units
        assert coord.standard_name == expected_output.enter_result.standard_name
        assert np.allclose(coord.points, expected_output.enter_result.points)
