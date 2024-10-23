"""Module for configurations."""

from __future__ import annotations

import glob
import logging
import os
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any

import iris.cube
import yaml
from iris.fileformats.netcdf import CF_CONVENTIONS_VERSION
from iris.util import equalise_attributes

from gordias import __version__

logger = logging.getLogger(__name__)


@dataclass
class InputTransferConfiguration:
    """
    Input attribute configuration.

    Parameters
    ----------
    attr_name : str
        String describing the global attribute name.
    attributes : list[str]
        List of strings with global attribute values.

    Attributes
    ----------
    attr_name : str
        String describing the global attribute name.
    attributes : list[str]
        List of strings with global attribute values.
    """

    attr_name: str
    attributes: list[str]


@dataclass
class OutputCreateConfiguration:
    """
    Output attribute configuration.

    Parameters
    ----------
    attr_name : str
        String describing the global attribute name.
    attributes : str
        Strings with global attribute value.

    Attributes
    ----------
    attr_name : str
        String describing the global attribute name.
    attributes : str
        Strings with global attribute value.
    """

    attr_name: str
    attribute: str


@dataclass
class GlobalAttributesInputConfiguration:
    """
    Configuration for global input attributes.

    Parameters
    ----------
    default : str
        String describing the default configuration option. Default is 'equalize'.
    drop : list[str]
        List with strings describing global attributes to remove.
    transfer : list[`InputTransferConfiguration`]
        List with :class:`InputTransferConfiguration` objects.

    Attributes
    ----------
    default : str
        String describing the default configuration option. Default is 'equalize'.
    drop : list[str]
        List with strings describing global attributes to remove.
    transfer : list[`InputTransferConfiguration`]
        List with :class:`InputTransferConfiguration` objects.
    """

    default: str = "equalize"
    drop: list[str] = field(default_factory=list)
    transfer: list[InputTransferConfiguration] = field(default_factory=list)


@dataclass
class GlobalAttributesOutputConfiguration:
    """
    Configuration for global output attributes.

    Parameters
    ----------
    create : list[`OutputCreateConfiguration`]
        List with :class:`OutputCreateConfiguration` objects.

    Attributes
    ----------
    create : list[`OutputCreateConfiguration`]
        List with :class:`OutputCreateConfiguration` objects.
    """

    create: list[OutputCreateConfiguration] = field(default_factory=list)


@dataclass
class GlobalAttributesConfiguration:
    """
    Configuration for global attributes.

    The input configuration is described by the
    :class:`GlobalAttributeInputConfiguration` and the output configuration is described
    by the :class:`GlobalAttributeOutputConfiguration`.

    Parameters
    ----------
    input : `GlobalAttributeInputConfiguration`
        Input configuration :class:`GlobalAttributeInputConfiguration` object.
    output : `GlobalAtributeOutputConfiguration`
        Output configuration :class:`GlobalAttributeOutputConfiguration` object.
    extra_attributes: dict[str, Any]
        A dictionary with additional global attribute information.

    Attributes
    ----------
    input : `GlobalAttributeInputConfiguration`
        Input configuration :class:`GlobalAttributeInputConfiguration` object.
    output : `GlobalAtributeOutputConfiguration`
        Output configuration :class:`GlobalAttributeOutputConfiguration` object.
    extra_attributes: dict[str, Any]
        A dictionary with additional global attribute information.

    Notes
    -----
    The dictionary for `extra_attributes` can be used to include values during runtime.
    E.g, a dictionary created during runtime: ::

        extra_attributes = {'my-attribute' : 'Cube produced 2024-07-24T14:45'}

    can be included in the output configuration in the configuration-file: ::

        Output:
            create:
                'cube-production-date' : '{my-attribute}'

    """

    input: GlobalAttributesInputConfiguration
    output: GlobalAttributesOutputConfiguration
    extra_attributes: dict[str, Any] = field(default_factory=dict)


def _get_default_configuration_path() -> list[str]:
    """Return the path of the default YAML configuration file."""
    directory = os.path.join(os.path.dirname(__file__), "etc")
    if os.path.isdir(directory):
        return glob.glob(os.path.join(directory, "*.yml"))
    else:
        raise RuntimeError(
            "Failed to find YAML configuration file in directory " f"<{directory}>."
        )


def _get_default_configuration_metadata(
    path: str,
) -> dict[str, dict[str, dict[str, Any]]]:
    """Return the default configuration metadata."""
    try:
        with open(path, "r") as f:
            config_file: dict[str, dict[str, dict[str, str]]] = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        raise yaml.YAMLError(f"Error in configuration file: {exc}") from exc
    return config_file


def _get_default_configuration() -> dict[str, Any]:
    """Return the metadata of the default configuration."""
    config: dict[str, Any] = {}
    for path in _get_default_configuration_path():
        logger.info(f"Reading configuration default definitions from file {path}")
        config_file = _get_default_configuration_metadata(path)
        try:
            config = config_file["config"]
            config.update(get_configuration(config))
        except ValueError:
            raise ValueError(
                f"Failed to get default configuration from default file <{path}>."
            )
    return config


def _get_global_attribute_config(
    config_metadata: dict[str, dict[str, dict[str, Any]]],
) -> GlobalAttributesConfiguration | None:
    """Return the configuration of the global attributes."""
    global_attr_metadata = config_metadata.get("global_attributes", None)
    return build_global_attributes_configuration(global_attr_metadata)


def get_configuration(
    metadata: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """
    Construct the configuration from the configuration metadata.

    Given a dictionary containing configuration metadata, the corresponding
    metadata will be used when setting up a dictionary with configuration
    objects. If no metadata is given the default configuration metadata will
    be used.

    Parameters
    ----------
    metadata : dict[str, dict[str, Any]], optional
        A dictionary containing the configuration metadata. If `None` the default
        configuration is used.

    Returns
    -------
    dict[str, Any]
        A dictionary containing the configuration. By default loads the
        :ref:`Default configuration-file` if no other configuration is provided.
    """
    config = {}
    if metadata is not None:
        global_attributes_config = _get_global_attribute_config(metadata)
        if global_attributes_config is not None:
            config["global_attributes"] = global_attributes_config
    else:
        config = _get_default_configuration()
    return config


def _construct_input_transfer_config(
    metadata: dict[str, Any],
) -> list[InputTransferConfiguration]:
    """Construct :class:`InputTransferConfiguration`."""
    input_transfer = []
    transfer = metadata["input"]["transfer"]
    if transfer:
        if isinstance(transfer, dict):
            for attr_name, attributes in transfer.items():
                input_transfer.append(InputTransferConfiguration(attr_name, attributes))
    return input_transfer


def _construct_output_create_config(
    metadata: dict[str, Any],
) -> list[OutputCreateConfiguration]:
    """Construct :class:`OutputCreateConfiguration`."""
    output_create = []
    create = metadata["output"]["create"]
    if create:
        if isinstance(create, dict):
            for attr_name, attributes in create.items():
                output_create.append(OutputCreateConfiguration(attr_name, attributes))
    return output_create


def build_global_attributes_configuration(
    global_attribute_metadata: dict[str, Any] | None = None,
) -> GlobalAttributesConfiguration | None:
    """
    Construct the :class:`GlobalAttributesConfiguration` object.

    Given a dictionary with the configuration metadata of the global attributes the
    :class:`GlobalAttributesConfiguration` object is constructed. `None` is returned if
    no configuration is provided with the global attribute configuration.

    Parameters
    ----------
    global_attribute_metadata : dict[str, Any] or None
        A dictionary containing the global attributes configuration.

    Returns
    -------
    :class:`GlobalAttributesConfiguration`
        The constructed global attribute configuration object or `None`.

    Raises
    ------
    ValueError:
        If the construction of the global attribute configuration object fails.
    """
    global_attributes_configuration = None
    if global_attribute_metadata is not None:
        try:
            input_transfer = _construct_input_transfer_config(global_attribute_metadata)
            output_create = _construct_output_create_config(global_attribute_metadata)
            input = GlobalAttributesInputConfiguration(
                global_attribute_metadata["input"]["default"],
                global_attribute_metadata["input"]["drop"],
                input_transfer,
            )
            output = GlobalAttributesOutputConfiguration(
                output_create,
            )
            global_attributes_configuration = GlobalAttributesConfiguration(
                input,
                output,
            )
        except BaseException:
            raise ValueError(
                "Failed to construct global attributes configuration from metadata"
                f"<{global_attribute_metadata}>"
            )
    return global_attributes_configuration


def configure_global_attributes_input(
    cubes: iris.cube.Cube | iris.cube.CubeList,
    config: dict[str, GlobalAttributesConfiguration] | None = None,
) -> None:
    """
    Apply the input configuration of the global attributes to all cubes.

    By default, equalizes all attributes by removing the attributes that are not equal
    between all cubes. A configuration can be used to specify how the global attributes
    should be transferred to the output cube.

    Parameters
    ----------
    cubes : iris.cube.Cube or iris.cube.CubeList
        A single cube or a list of cubes.
    config : dict[`GlobalAttributesConfiguration`]
        A dictionary containing a :class:`GlobalAttributesConfiguration` object.
    """
    removed_attributes = set()
    if isinstance(config, dict):
        if isinstance(cubes, iris.cube.Cube):
            cubes = iris.cube.CubeList([cubes])

        if config["global_attributes"]:
            global_attribute_config = config["global_attributes"]
            if isinstance(global_attribute_config, GlobalAttributesConfiguration):
                logger.info("Configuring global attributes from input files")
                input_configuration = global_attribute_config.input
                transfer, attr_not_found = get_transfer_configuration_attributes(
                    cubes, input_configuration.transfer
                )
                if attr_not_found:
                    logger.debug(
                        "Following attributes were not found in all cubes: "
                        f"{list(attr_not_found)}"
                    )
                replaced_attributes = add_global_attributes(cubes, transfer)
                if replaced_attributes:
                    logger.debug(
                        f"Following attributes were replaced: {replaced_attributes}"
                    )
                if input_configuration.drop:
                    removed_attr = drop_global_attributes(
                        cubes, input_configuration.drop
                    )
                    removed_attributes.update(removed_attr)
                if input_configuration.default == "drop":
                    removed_attr = default_configuration(cubes, input_configuration)
                    removed_attributes.update(removed_attr)
    removed_attr = equalize_global_attributes(cubes)
    removed_attributes.update(removed_attr)
    if removed_attributes:
        logger.debug(
            f"Attributes were removed to equalize cubes: <{list(removed_attributes)}>."
        )


def configure_global_attributes_output(
    cubes: iris.cube.Cube | iris.cube.CubeList,
    config: dict[str, GlobalAttributesConfiguration] | None = None,
) -> None:
    """
    Apply the output configuration of the global attributes to all cubes.

    If no configuration object for the output global attributes is given, no changes
    will be made to the cubes. The `extra_attribues` in the
    :class:`GlobalAttributesConfiguration` can be used to store extra attributes that
    are created during runtime.

    Parameters
    ----------
    cubes : iris.cube.Cube or iris.cube.CubeList
        A single cube or a list of cubes.
    config : dict[str, `GlobalAttributesConfiguration`] or None, optional
        A dictionary containing a :class:`GlobalAttributesConfiguration` object.
    """
    if isinstance(config, dict) and config["global_attributes"]:
        if isinstance(cubes, iris.cube.Cube):
            cubes = iris.cube.CubeList([cubes])

        global_attribute_config = config["global_attributes"]
        if isinstance(global_attribute_config, GlobalAttributesConfiguration):
            logger.info("Configuring global attributes for output file")
            output_configuration = global_attribute_config.output
            extra_attributes = global_attribute_config.extra_attributes
            attributes = get_create_configuration_attributes(
                output_configuration.create, cubes[0], extra_attributes
            )
            replaced_attributes = add_global_attributes(cubes, attributes)
            if replaced_attributes:
                logger.debug(
                    f"Following attributes were replaced: {replaced_attributes}"
                )


def get_transfer_configuration_attributes(
    cubes: iris.cube.CubeList, transfer: list[InputTransferConfiguration]
) -> tuple[dict[str, str], list[str]]:
    """
    Create transfer attributes from the `transfer` configuration.

    Collects values from the cubes and returns a dictionary containing all transfer
    attributes and a list containing attributes that could not be found in all cubes.

    Parameters
    ----------
    cubes : iris.cube.CubeList
        A list of cubes.
    transfer : list[`InputTransferConfiguration`]
        A list containing :class:`InputTransferConfiguration` objects that describes
        the transfer configuration for the  global attributes in the input files.

    Returns
    -------
    attribute_dict : dict[str, str]
        A dictionary containing all transfer attributes defined by the
        configurations.
    attributes_not_found : list[str]
        A list of string containing global attributes that could not be found in all
        cubes.

    Raises
    ------
    ValueError
        If a `attribute` defined in the configuration could not be found.
    """
    attribute_dict = {}
    attributes_not_found = set()
    for attribute_config in transfer:
        attr_name = attribute_config.attr_name
        if attribute_config.attributes:
            attr_values, attr_not_found = join_global_attribute_values(
                cubes, attribute_config.attributes
            )
        else:
            raise ValueError(f"Attributes could not be found for <{attr_name}>")
        attributes_not_found.update(attr_not_found)
        if attr_values:
            attribute_dict[attr_name] = ", ".join(attr_values)
    return attribute_dict, list(attributes_not_found)


def create_creation_date(
    offset: timedelta = timedelta(0),
) -> str:
    """Create `UTC` creation date following ISO 8601 format.

    Parameters
    ----------
    offset: timedelta
        timedelta object representing the difference between the local time and
        `UTC`. Default is `timedelta(0)` which gives `UTC` time.

    Returns
    -------
    str
        A string representing the ISO 8601 formatted date based on current datetime.
    """
    time = datetime.now(timezone(offset=offset))
    if offset == timedelta(0):
        return time.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
    return time.isoformat(timespec="seconds")


def create_tracking_id() -> str:
    """
    Generate a string formatted UUID.

    Returns
    -------
    str
        A string formatted UUID.
    """
    return str(uuid.uuid4())


def get_create_configuration_attributes(
    attributes: list[OutputCreateConfiguration],
    cube: iris.cube.Cube | None = None,
    extra_attributes: dict[str, Any] | None = None,
) -> dict[str, str]:
    """
    Create attributes from the `create` configuration.

    A `extra_attributes` dictionary can be given to include attributes.

    Parameters
    ----------
    attributes : list[`OutputCreateConfiguration`]
        A list containing :class:`OutputCreateConfiguration` objects that describes
        the create configuration for the  global attributes in the output files.
    cube : iris.cube.Cube
        A iris cube with global attributes to be included in the global attribute
        configuration.
    extra_attributes : dict[str, Any], optional
        A dictionary containing extra attributes to be included in the global
        attributes.

    Returns
    -------
    dict[str, str]
        A dictionary of string containing the names and values of the created global
        attributes.

    """
    fill_value = {
        "NOW": create_creation_date(),
        "TRACKING_ID": create_tracking_id(),
        "GORDIAS_VERSION": f"gordias-{__version__}",
        "CF_CONVENTIONS_VERSION": f"{CF_CONVENTIONS_VERSION}",
    }
    if isinstance(cube, iris.cube.Cube):
        fill_value.update(cube.attributes)
    if extra_attributes is not None:
        fill_value.update(extra_attributes)
    attribute_dict = {}
    for attribute_config in attributes:
        attr_name = attribute_config.attr_name
        attr_value = attribute_config.attribute
        if attr_value:
            try:
                attribute_dict[attr_name] = attr_value.format(**fill_value)
            except KeyError:
                raise KeyError(
                    f"Value could not be found for <{attr_name}> <{attr_value}>"
                )
        else:
            raise ValueError(f"Attribute value could not be found for <{attr_name}>")
    return attribute_dict


def equalize_global_attributes(cubes: iris.cube.CubeList) -> list[str]:
    """
    Remove global attributes that are different between all cubes.

    A list is returned containing the set of removed attributes names and values.

    Parameters
    ----------
    cubes : iris.cube.CubeList
        A list of cubes.

    Returns
    -------
    list[str]
        A list of string containing the names and values of the removed global
        attributes.
    """
    removed_attributes = equalise_attributes(cubes)
    unique_attributes: set[str] = set()
    for attribute in removed_attributes:
        if isinstance(attribute, dict):
            unique_attributes.update(
                f"{attr_name} = {attr_value}"
                for attr_name, attr_value in attribute.items()
            )
    return list(unique_attributes)


def default_configuration(
    cubes: iris.cube.CubeList, config: GlobalAttributesInputConfiguration
) -> list[str]:
    """
    Apply the `default` configuration to all cubes.

    The `default` configuration can either drop all attributes that are not present in
    the transfer configuration or equalize the attributes between cubes. A list is
    returned containing the set of removed attributes names and values.

    Parameters
    ----------
    cubes : iris.cube.CubeList
        A list of cubes.
    config : `GlobalAttributesInputConfiguration`
        A :class:`GlobalAttributesInputConfiguration` object containing the input
        configuration for the global attributes.

    Returns
    -------
    list[str]
        A list of string containing the names and values of the removed global
        attributes.
    """
    removed_attributes = []
    if config.default == "drop":
        removed_attributes = drop_unspecified_global_attributes(cubes, config)
    if config.default == "equalize":
        removed_attributes = equalize_global_attributes(cubes)
    return removed_attributes


def drop_unspecified_global_attributes(
    cubes: iris.cube.CubeList, config: GlobalAttributesInputConfiguration
) -> list[str]:
    """
    Drop all unspecified global attributes for all cubes.

    The attributes that are not specified in the transfer configuration is removed. A
    list is returned containing the set of removed attributes names and values.

    Parameters
    ----------
    cubes : iris.cube.CubeList
        A list of cubes.
    config : `GlobalAttributesInputConfiguration`
        A :class:`GlobalAttributesInputConfiguration` object containing the input
        configuration for the global attributes.

    Returns
    -------
    list[str]
        A list of string containing the names and values of the removed global
        attributes.
    """
    removed_attributes = []
    if config.transfer is not None:
        attributes_to_keep = [attribute.attr_name for attribute in config.transfer]
        all_attributes = set()
        for cube in cubes:
            all_names = [
                attr_name
                for attr_name in cube.attributes
                if attr_name not in attributes_to_keep
            ]
            all_attributes.update(all_names)
        removed_attributes = drop_global_attributes(cubes, list(all_attributes))
    return removed_attributes


def add_global_attributes(
    cubes: iris.cube.CubeList, attributes: dict[str, str]
) -> list[str]:
    """
    Add global attributes to all cubes.

    Attributes specified in the dictionary `attributes` will be added. A list
    is returned containing the set of replaced attributes with names and values.

    Parameters
    ----------
    cubes : iris.cube.CubeList
        A list of cubes.
    attributes : dict[str, str]
        A dictionary containing new global attribute names and values.

    Returns
    -------
    list[str]
        A list of string containing the names and values of the replaced global
        attributes.
    """
    replaced_attributes = set()
    if attributes:
        for cube in cubes:
            for attr_name, attr_value in attributes.items():
                if (
                    attr_name in cube.attributes
                    and attr_value != cube.attributes[attr_name]
                ):
                    replaced_attributes.add(
                        f"{attr_name} = {cube.attributes[attr_name]}"
                    )
                cube.attributes[attr_name] = attr_value
    return list(replaced_attributes)


def drop_global_attributes(
    cubes: iris.cube.CubeList, attributes: list[str]
) -> list[str]:
    """
    Drop global attributes for all cubes.

    Given a list `attributes` containing the names of the attributes that should be
    dropped. A list is returned containing the set of removed attributes names and
    values.

    Parameters
    ----------
    cubes : iris.cube.CubeList
        A list of cubes.
    attributes : list[str]
        A list of string with global attribute names to drop.

    Returns
    -------
    list[str]
        A list of string containing the names and values of the removed global
        attributes.
    """
    removed_attributes = set()
    if attributes:
        for cube in cubes:
            for attr_name in attributes:
                if attr_name in cube.attributes:
                    attr_value = cube.attributes.pop(attr_name, None)
                    removed_attributes.add(f"{attr_name} : {attr_value}")
    return list(removed_attributes)


def join_global_attribute_values(
    cubes: iris.cube.CubeList, attr_names: list[str]
) -> tuple[list[str], list[str]]:
    """
    Join attribute values between all cubes.

    Given a list `attr_names` containing the names of the attributes which values should
    be joined between all cubes. Two lists are returned, the first containing joined
    global attributes and the second containing attributes that could not be found in
    all cubes.

    Parameters
    ----------
    cubes : iris.cube.CubeList
        A list of cubes.
    attr_names : list[str]
        A list of string containing global attribute names to join.

    Returns
    -------
    joined_attr_values : list[str]
        A list of string containing joined global attributes.
    attributes_not_found : list[str]
        A list of string containing global attribute names that could not be found
        in all cubes.
    """
    joined_attr_values = set()
    attributes_not_found = set()
    for cube in cubes:
        attr_values = []
        for attr_name in attr_names:
            if attr_name in cube.attributes:
                attr_values.append(cube.attributes[attr_name])
            else:
                attributes_not_found.add(attr_name)
        if attr_values:
            joined_attr_values.add("_".join(attr_values))
    return list(joined_attr_values), list(attributes_not_found)
