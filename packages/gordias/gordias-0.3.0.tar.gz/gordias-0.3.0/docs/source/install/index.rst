.. _install:


Installation
============

Installing with conda-forge (recommended)
-----------------------------------------

To install Gordias from conda-forge, you can use the Conda package manager or Mamba.
If you don't already have a version of Conda or Mamba available to you, the best way to get started is by installing :miniforge:`miniforge <>`, an installer for Mamba that will pre-configure your installation to use the conda-forge distribution.

.. tip::
    If you prefer to use Conda instead of Mamba, for example because this has been pre-installed for you, just replace `mamba` with `conda` in the following commands.


To install the latest version of Gordias, just create an environment with the `gordias` package in it by running::

    mamba create -n gordias-env gordias

where `gordias-env` is an arbitrary name you choose.

To use Gordias at any time, you need to make sure that the `gordias-env` environment is activated.
To do that, execute::

    mamba activate gordias-env


Installing with Pip
-------------------
You can install Gordias with pip from PyPI. It is recommended to install the package in a virtual environment. ::

    python -m pip install gordias
