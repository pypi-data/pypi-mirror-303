# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import sys
from importlib.metadata import version
from pathlib import Path

root = Path(__file__).absolute().parent.parent.parent
sys.path.insert(0, str(root))

# -- Project information -----------------------------------------------------

project = "Gordias"
copyright = "2024, Carolina Nilsson, Joakim Löw"
author = "Carolina Nilsson, Joakim Löw"

# The full version, including alpha/beta/rc tags
release = version(project)
version = ".".join(release.split(".")[:3])

theme_logo = f"Gordias v.{version}"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinx_toolbox.collapse",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "_templates"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]
html_theme_options = {
    "gitlab_url": "https://git.smhi.se/climix/gordias",
    "navbar_start": ["logo"],
}

# external links
extlinks = {
    "climix": ("https://git.smhi.se/climix/climix/%s", None),
    "midas": ("https://git.smhi.se/midas/midas/%s", None),
    "dask": ("https://www.dask.org/%s", None),
    "iris": ("https://scitools-iris.readthedocs.io/en/stable/%s", None),
    "miniforge": ("https://github.com/conda-forge/miniforge#miniforge/%s", None),
}
# Intersphinx mapping for references, helps with checking that the links still works.
intersphinx_mapping = {
    "iris": ("https://scitools-iris.readthedocs.io/en/stable", None),
    "dask": ("https://distributed.dask.org/en/stable/", None),
    "py3": ("https://docs.python.org/3", None),
    "cf-units": ("https://cf-units.readthedocs.io/en/stable", None),
}
