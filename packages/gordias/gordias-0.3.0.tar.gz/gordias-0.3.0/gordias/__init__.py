"""
Gordias
-------

A core package for climix and MIdAS (MultI-scale bias AdjuStment). Contains
utility tools to load, save and process data.

"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("gordias")
except PackageNotFoundError as e:
    raise PackageNotFoundError("Gordias package could not be found.") from e
