"""Module for working with units."""

from typing import NamedTuple

import cf_units
import iris.coords
import iris.cube

DENSITY_WATER = cf_units.Unit("1000 kg m-3")


class PrecipitationQuantity(NamedTuple):
    """
    Holds a precipitation unit with additional information.

    Parameters
    ----------
    unit : cf_units.Unit
        Unit of precipitation.
    is_rate_based : bool
        `True` if the unit has a time component.
    is_mass_based : bool
        `True` if the unit has a mass component.

    Attributes
    ----------
    unit : cf_units.Unit
        Unit of precipitation.
    is_rate_based : bool
        `True` if the unit has a time component.
    is_mass_based : bool
        `True` if the unit has a mass component.
    """

    unit: cf_units.Unit
    is_rate_based: bool
    is_mass_based: bool


PRECIPITATION_INFO = {
    "lwe_precipitation_rate": PrecipitationQuantity(
        cf_units.Unit("m s-1"), True, False
    ),
    "lwe_thickness_of_precipitation_amount": PrecipitationQuantity(
        cf_units.Unit("m"), False, False
    ),
    "thickness_of_rainfall_amount": PrecipitationQuantity(
        cf_units.Unit("m"), False, False
    ),
    "precipitation_amount": PrecipitationQuantity(cf_units.Unit("kg m-2"), False, True),
    "precipitation_flux": PrecipitationQuantity(
        cf_units.Unit("kg m-2 s-1"), True, True
    ),
}


def is_precipitation(standard_name: str) -> bool:
    """Check if given standard name is a precipitation standard name.

    Parameters
    ----------
    standard_name : str
        Standard name as string.

    Returns
    -------
    bool
        Whether standard name is a precipitation standard name.
    """
    return standard_name in PRECIPITATION_INFO.keys()


def get_standard_name_for_precipitation_unit(unit: cf_units.Unit) -> str:
    """Get standard name for given precipitation unit.

    Parameters
    ----------
    unit : cf_units.Unit
        Precipitation unit to find standard name for.

    Returns
    -------
    str
        Standard name for precipitation unit.

    Raises
    ------
    ValueError
        If unit is not a precipitation unit.
    """
    for standard_name, qty in PRECIPITATION_INFO.items():
        if unit.is_convertible(qty.unit):
            return standard_name
    raise ValueError(f"{unit} doesn't seem to be a precipitation unit.")


def ensure_precipitation_unit_and_standard_name(
    unit: cf_units.Unit | None,
    standard_name: str | None,
) -> tuple[cf_units.Unit, str]:
    """Get valid unit and standard name pair.

    This function expects at least one of the arguments to be given.
    If one or both of the arguments are given, a valid pair
    of unit and standard name is returned if possible, otherwise an
    exception will be raised.

    Parameters
    ----------
    unit : cf_units.Unit | None
        Unit to check.
    standard_name : str | None
        Standard name to check.

    Returns
    -------
    unit : cf_units.Unit
        A precipitation unit valid to the standard_name.
    standard_name : str
        A precipitation standard name valid to the unit.

    Raises
    ------
    ValueError
        If a valid pair of unit and standard name could not be found.
    """
    if isinstance(unit, str):
        unit = cf_units.Unit(unit)
    if unit is None and standard_name is None:
        raise ValueError("No unit or standard name is given.")
    if standard_name is None:
        standard_name = get_standard_name_for_precipitation_unit(unit)
    try:
        quantity = PRECIPITATION_INFO[standard_name]
    except KeyError:
        raise ValueError(f"Unknown precipitation standard name {standard_name}.")
    if unit is None:
        unit = quantity.unit
    if not unit.is_convertible(quantity.unit):
        raise ValueError(f"Unit {unit} does not match standard_name {standard_name}.")
    return unit, standard_name


def get_precipitation_rate_conversion(
    old_quantity: PrecipitationQuantity,
    new_quantity: PrecipitationQuantity,
    integration_time: cf_units.Unit,
) -> cf_units.Unit:
    """Get unit for rate conversion between precipitation units.

    Some precipitation units does not have time as part of their
    unit. In such cases the precipitation integration time must
    be supplied.

    Parameters
    ----------
    old_quantity : PrecipitationQuantity
        Old quantity containing unit with additional information.
    new_quantity : PrecipitationQuantity
        New quantity containing unit with additional information.
    integration_time : cf_units.Unit
        Unit of integration time.

    Returns
    -------
    cf_units.Unit
        Rate conversion as a unit.

    Raises
    ------
    ValueError
        If `integration_time` is not a time unit.
    """
    if not integration_time.is_time():
        raise ValueError("Integration time argument must be a time unit")
    if old_quantity.is_rate_based and not new_quantity.is_rate_based:
        return integration_time
    if not old_quantity.is_rate_based and new_quantity.is_rate_based:
        return integration_time.invert()
    return cf_units.Unit(1.0)


def get_precipitation_mass_conversion(
    old_quantity: PrecipitationQuantity,
    new_quantity: PrecipitationQuantity,
    density: cf_units.Unit,
) -> cf_units.Unit:
    """Get unit for mass conversion between precipitation units.

    Parameters
    ----------
    old_quantity : PrecipitationQuantity
        Old quantity containing unit with additional information.
    new_quantity : PrecipitationQuantity
        New quantity containing unit with additional information.
    density : cf_units.Unit
        Unit of integration time.

    Returns
    -------
    cf_units.Unit
        Mass conversion as a unit.
    """
    if not density.is_convertible(cf_units.Unit("kg m-3")):
        raise ValueError("Density argument must be a density unit")
    if old_quantity.is_mass_based and not new_quantity.is_mass_based:
        return density.invert()
    if not old_quantity.is_mass_based and new_quantity.is_mass_based:
        return density
    return cf_units.Unit(1.0)


def change_precipitation_units(
    cube_or_coord: iris.cube.Cube | iris.coords.Coord,
    new_unit: cf_units.Unit,
    new_standard_name: str | None = None,
    integration_time: cf_units.Unit = cf_units.Unit("1 day"),
    density: cf_units.Unit = DENSITY_WATER,
) -> None:
    """Convert precipitation unit considering standard names.

    Converts precipitation units and data to requested units.
    Standard names are converted too, if required.
    Changes are made in-place.

    Parameters
    ----------
    cube_or_coord : iris.cube.Cube | iris.coords.Coord
        Precipitation data.
    new_unit : cf_units.Unit
        Unit to convert to.
    new_standard_name : str | None, optional
        Standard name to convert to.
    integration_time : cf_units.Unit, optional
        Integration time for given data, if not included in unit.
        By default cf_units.Unit("1 day").
    density : cf_units.Unit, optional
        Density of medium. By default cf_units.Unit("1000 kg m-3")
    """
    new_units, new_standard_name = ensure_precipitation_unit_and_standard_name(
        new_unit, new_standard_name
    )
    old_units, old_standard_name = ensure_precipitation_unit_and_standard_name(
        cube_or_coord.units, cube_or_coord.standard_name
    )

    old_quantity = PRECIPITATION_INFO[old_standard_name]
    new_quantity = PRECIPITATION_INFO[new_standard_name]

    conv = get_precipitation_rate_conversion(
        old_quantity, new_quantity, integration_time
    ) * get_precipitation_mass_conversion(old_quantity, new_quantity, density)

    conv_factor = (old_units * conv).convert(1.0, new_units)
    if isinstance(cube_or_coord, iris.cube.Cube):
        cube_or_coord.data = cube_or_coord.core_data() * float(conv_factor)
    elif isinstance(cube_or_coord, iris.coords.Coord):
        cube_or_coord.points *= float(conv_factor)
        if cube_or_coord.bounds is not None:
            cube_or_coord.bounds *= float(conv_factor)
    cube_or_coord.units = new_units
    cube_or_coord.standard_name = new_standard_name


def change_units(
    cube_or_coord: iris.cube.Cube | iris.coords.Coord,
    new_unit: cf_units.Unit,
    new_standard_name: str | None = None,
    integration_time: cf_units.Unit = cf_units.Unit("1 day"),
) -> None:
    """Convert Cube or Coord units.

    Parameters
    ----------
    cube_or_coord: iris.cube.Cube | iris.coords.Coord
        Any Cube or Coord to change unit for.
    new_unit: cf_units.Unit
        Unit to convert to.
    new_standard_name: str | None, optional
        Standard name to convert to, by default None.
    integration_time : cf_units.Unit, optional
        Integration time for the Cube or Coord unit, if not included
        in the input unit. Default is cf_units.Unit("1 day")

    Raises
    ------
    ValueError
        If `integration_time` is not a time unit.
    """
    if not integration_time.is_time():
        raise ValueError("Integration time must be a time unit")
    if new_standard_name is not None and is_precipitation(new_standard_name):
        change_precipitation_units(
            cube_or_coord,
            new_unit,
            new_standard_name,
            integration_time,
        )
    else:
        cube_or_coord.convert_units(new_unit)
