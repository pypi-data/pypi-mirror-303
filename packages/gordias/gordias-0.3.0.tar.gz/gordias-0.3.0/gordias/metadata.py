"""Module for metadata."""

import glob
import logging
import os

import yaml

logger = logging.getLogger(__name__)


def _find_metadata_files_in_dir(directory: str) -> list[str]:
    """Find all `yml` files in directory."""
    if os.path.isdir(directory):
        return glob.glob(os.path.join(directory, "*.yml"))
    return []


def find_metadata_files(
    metadata_files: str | list[str] | None = None,
) -> list[str]:
    """
    Find metadata files in default directory `etc`.

    Finds metadata files, i.e. `yml` files, in default directory `etc`. Additional
    external files can be provided through the input parameter `metadata_files` and will
    be included in the returned list of file paths.

    Parameters
    ----------
    metadata_files : string or list[str], optional
        A path or a list of paths to external `yml` files.

    Returns
    -------
    list[str]
        A list containing file paths.
    """
    directories = [os.path.join(os.path.dirname(__file__), "etc")]
    for d in directories:
        logger.info(f"Looking for metadata in directory {d}")
    files = sum(
        [_find_metadata_files_in_dir(directory) for directory in directories], []
    )
    if metadata_files is not None:
        if not isinstance(metadata_files, list):
            metadata_files = [metadata_files]
        for f in metadata_files:
            logger.info(f"Adding metadata from file: {f}")
            files.append(f)
    return files


def load_configuration_metadata(
    metadata_files: str | list[str] | None = None,
) -> dict[str, dict[str, str]] | None:
    """
    Load the configuration metadata from `yml` files.

    Loads the default configuration from the default directory `etc`. An external
    configuration file can be loaded trough the input parameter `metadata_files`. If
    multiple configurations are loaded, the last loaded configuration will supersede the
    other configurations including the default configuration.

    Parameters
    ----------
    metadata_files: string or list[str], optional
        A path or a list of paths to external configuration files.

    Returns
    -------
    dict[str, dict[str, str]] or None
        A dictionary containing the configuration metadata. `None` if no configuration
        was found.
    """
    config_metadata: dict[str, dict[str, str]] | None = None
    for path in find_metadata_files(metadata_files):
        with open(path) as md_file:
            metadata = yaml.safe_load(md_file)
        if "config" in metadata:
            config_metadata = metadata["config"]
            config_path = path
    if config_metadata:
        logger.info(f"Loading configuration with definition from file <{config_path}>.")
    return config_metadata
