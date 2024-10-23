.. _user_guide:

Getting started
===============

Gordias is a core package for :climix:`Climix <>` and :midas:`MIdAS (MultI-scale bias AdjuStment) <>`.
It contains utility tools to load, save and process data. The package is built on :dask:`Dask <>` and :iris:`Iris <>`.

Load files
----------

To load netCDF datafiles with gordias the :func:`gordias.datahandling.prepare_input_data` function can be used: ::

    import gordias.datahandling
    filenames = ['/path/to/files/*.nc']
    cubes = gordias.datahandling.prepare_input_data(filenames)

The function tries to merge :obj:`cubes<iris.cube.Cube>` of the same variables. It returns a :obj:`cube list<iris.cube.CubeList>` containing a single cube for each variable.

.. note:: If the input files for a variable could not be merged into a single cube an exception will be raised and a description of the difference between the files will be printed.


Save files
----------

A :obj:`cube<iris.cube.Cube>` can be saved to a netCDF file using the :func:`gordias.datahandling.save` function: ::

    import gordias.datahandling

    gordias.datahandling.save(cube, "/path/to/file/my-result-file.nc", iterative_storage=True)

If no dask scheduler is used the result needs to be stored with the flag `iterative_storage` set to `True`.


Configuration of global attributes
----------------------------------

A configuration file can be used to specify how the global attributes from the input files should be transferred to the output cube and what global attributes that should be created for the cube.

There is a :ref:`Default configuration-file` that can be used with the :func:`gordias.config.get_configuration` function: ::

    import gordias.datahandling
    import gordias.config

    configuration = gordias.config.get_configuration()
    filenames = ['/path/to/files/*.nc']
    cubes = gordias.datahandling.prepare_input_data(filenames, configuration)

By giving the configuration as a argument to :func:`gordias.datahandling.prepare_input_data` the input configuration will be applied when loading the data.

It is possible to use your own configuration file. First you need to create a configuration yml-file, it should follow the rules of the :ref:`Configuration template`.
Then the file can be loaded with the :func:`gordias.metadata.load_configuration_metadata` function and the configuration can be generated with the :func:`gordias.config.get_configuration` function: ::

    import gordias.config
    import gordias.datahandling
    import gordias.metadata

    path = "/path/to/my-config.yml"
    metadata = gordias.metadata.load_configuration_metadata(path)
    configuration = gordias.config.get_configuration(metadata)
    filenames = ["/path/to/files/*.nc"]
    cubes = gordias.datahandling.prepare_input_data(filenames, configuration)

.. note:: If no configuration is used when loading multiple files all global attributes that are not equal among the input files will be removed.

To save a cube and apply the output configuration, the configuration needs to be given as an argument to the :func:`gordias.datahandling.save` function ::

    import gordias.config
    import gordias.datahandling
    import gordias.metadata

    path = "/path/to/my-config.yml"
    metadata = gordias.metadata.load_configuration_metadata(path)
    configuration = gordias.config.get_configuration(metadata)
    filenames = ["/path/to/files/*.nc"]
    cubes = gordias.datahandling.prepare_input_data(filenames, configuration)
    gordias.datahandling.save(cubes[0], "/path/to/file/my-result-file.nc", iterative_storage=True, configuration=configuration)

.. note:: The input and output configurations can be applied at any time with the :func:`gordias.config.configure_global_attributes_input` and :func:`gordias.config.configure_global_attributes_output` functions.


Setup Dask Scheduler
--------------------
Gordias supports setting up a :obj:`dask scheduler<distributed.LocalCluster>` that can be used for computations in a parallel environment. To setup a schedeuler::

    import gordias.datahandling
    import gordias.dask_setup

    def main():
        scheduler = gordias.dask_setup.DistributedLocalClusterScheduler()
        with scheduler:
            filenames = ["/path/to/files/my-input-file.nc"]
            cubes = gordias.datahandling.prepare_input_data(filenames)
            ### do calculations ###
            gordias.datahandling.save(cube, "/path/to/file/my-result-file.nc", client=scheduler.client)

    if __name__ in "__main__":
        main()

The schedulers in :ref:`schedulers` are context managers, following PEP 343, using the `with` statement makes it easier to shutdown the schedulers.
