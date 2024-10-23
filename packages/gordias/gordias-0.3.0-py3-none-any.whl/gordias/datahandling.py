"""Module for datahandling, e.g., load files, configure attributes and store results."""

from __future__ import annotations

import logging
import os
import time
from typing import Any

import iris
import iris.config
import iris.cube
import netCDF4
import numpy as np
from dask.distributed import Client

from gordias.config import (
    configure_global_attributes_input,
    configure_global_attributes_output,
)
from gordias.dask_setup import progress
from gordias.util.cube_diffs import find_cube_differences

logger = logging.getLogger(__name__)


iris.FUTURE.datum_support = True

#: Constant that is used to indicate missing value.
MISSVAL = 1.0e20


def prepare_input_data(
    datafiles: list[str], configuration: dict[str, Any] | None = None
) -> iris.cube.CubeList:
    """
    Produce a :class:`iris.cube.CubeList` with one cube per variable.

    Loads the data from all input files and merges them into one cube per variable. In
    the process, there might be potentially conflicting global attributes that cannot be
    merged. To transfer global attributes a configuration file can be given as an input
    to the `configuration` input parameter. If no configuration is given, the content of
    the cubes will be equalized by removing the attributes that conflict. If the given
    `datafiles` cannot be concatenated into a single cube per variable, the function
    raises a :exc:`ValueError`.

    Parameters
    ----------
    datafiles : list[str]
        A list of paths to datafiles.
    configuration : dict[str, Any] or None, optional
        A dictionary containing configuration objects.

    Returns
    -------
    iris.cube.CubeList
        A list of cubes, one per variable, referencing the corresponding data
        from all the input files.

    Raises
    ------
    ValueError
        If the given data can not be concatenated into one cube per variable. In this
        case, it is advised to investigate the problem by loading the same set of files
        in an interactive session with iris. Additionally a description of the
        differences found when comparing the cubes are logged.
    """
    datacubes = iris.load_raw(datafiles)
    iris.util.unify_time_units(datacubes)
    configure_global_attributes_input(datacubes, configuration)
    cubes = datacubes.concatenate()
    var_names = [c.var_name for c in cubes]
    if len(var_names) > len(set(var_names)):  # noqa
        cubes_per_var_name: dict[str, iris.cube.CubeList] = {}
        for c in cubes:
            cs = cubes_per_var_name.setdefault(c.var_name, [])
            cs.append(c)
        inconsistent_var_names = []
        for var_name, cubes in cubes_per_var_name.items():
            if len(cubes) > 1:
                logger.info(
                    f"Found too many cubes for variable <{var_name}>. Running "
                    "<find_cube_differences>."
                )
                inconsistent_var_names.append(var_name)
                find_cube_differences(cubes, oper="VGC", return_type="logging")
        raise ValueError(
            "Found too many cubes for var_names {}. See log for details.".format(
                inconsistent_var_names
            )
        )
    for c in cubes:
        time = c.coord("time")
        if not time.has_bounds():
            time.guess_bounds()
    return cubes


def save(
    result: iris.cube.Cube,
    output_filename: str,
    iterative_storage: bool = False,
    client: Client | None = None,
    conventions_override: bool = False,
    configuration: dict[str, Any] | None = None,
) -> None:
    """
    Save a single cube (iris.cube.Cube) to the given output filename.

    If there are outstanding computations in lazy data in the cube, this function
    realizes the results, i.e. performs all outstanding computations, loading the input
    data into memory. To avoid memory problems, we offer two different approaches on
    how this is done:

    If `iterative_storage` is `True`, first an empty cube is saved, putting all
    metadata and coordinates in place, then the result is realized and stored one
    timeslice at a time, sequentially. This potentially reduces parallelism, but also
    reduces memory requirements. Furthermore, it means that on unplanned termination,
    all finished calculations are already stored.

    If `iterative_storage` is `False`, the complete result is realized first,
    maximizing the parallel use of the cluster as exposed by `client`, but potentially
    leading to memory problems if there are large intermediate results. This also means
    that all results are lost in the case of unplanned termination. To use this option a
    `client` must be provided to the `client` input parameter.

    If `conventions_override` is `False`, the global attribute `Conventions` will be
    added as the default CF conventions version in iris. If `True` and `Conventions`
    exists in the global attributes the default `Conventions` will be overrided.

    A configuration can be given to apply the output configuration for creating global
    attributes to the output file.

    Parameters
    ----------
    result : iris.cube.Cube
        The iris cube to be saved.
    output_filename : string
        The filename of the output. Must refer to a netCDF4 file, i.e. `.nc`.
    iterative_storage : bool, optional
        Whether to perform iterative storage (see above). By default set to `False`.
    client : :class:`distributed.Client`, optional
        The :class:`distributed.Client` object giving access to the cluster.
    conventions_override : bool, optional
        Whether the existing global attribute `Conventions` will override the
        default CF conventions version in iris. By default set to `False`.
    configuration : dict[str, Any] or None, optional
        A dictionary with configuration objects.
    """

    def _calc_slices(
        chunks: tuple[int, ...], output_block_length: int = 1000
    ) -> list[slice]:
        """Prepare output slices."""
        div_points = [0]
        acc = 0
        next_div_point = 0
        for chunk in chunks:
            acc += chunk
            if acc > output_block_length:
                div_points.append(next_div_point)
                acc = chunk
            next_div_point += chunk
        slices = [
            slice(div_points[i], div_points[i + 1]) for i in range(len(div_points) - 1)
        ]
        slices.append(slice(div_points[-1], None))
        return slices

    if result.coords("day_of_year"):
        result.remove_coord("day_of_year")
    configure_global_attributes_output(result, configuration)
    data = result.core_data()
    time_dims = result.coord_dims("time")
    assert len(time_dims) == 1
    time_dim = time_dims[0]
    assert time_dim == 0
    output_slices = _calc_slices(data.chunks[time_dim])
    temporary_filename = f"{output_filename}.tmp.nc"
    if iterative_storage:
        logger.info("Storing iteratively")
        logger.debug("Creating empty data")
        placeholder = np.broadcast_to(np.zeros(data.shape[1:], data.dtype), data.shape)
        result.data = placeholder
        # Touch coord data to realize before save
        for coord in result.coords():
            coord.points
            coord.bounds
        logger.debug("Saving empty cube")
        with iris.config.netcdf.context(conventions_override=conventions_override):
            iris.save(
                result,
                temporary_filename,
                local_keys=["proposed_standard_name"],
                zlib=True,
                complevel=1,
                chunksizes=data.chunksize,
                fill_value=MISSVAL,
            )
        logger.debug("Reopening output file and beginning storage")
        result.data = data
        del placeholder
        with netCDF4.Dataset(temporary_filename, "a") as ds:
            var = ds[result.var_name]
            time_dim = result.coord_dims("time")[0]
            no_slices = result.shape[time_dim]

            end = time.time()
            cumulative = 0.0
            start_index = 0
            for output_slice in output_slices:
                result_data = data[output_slice].copy()
                result_id = f"{start_index + 1}/{no_slices}"
                logger.info(f"Storing partial result {result_id}")
                end_index = start_index + result_data.shape[0]
                logger.debug(f"{start_index}:{end_index}")
                logger.debug(f"{result_data.shape}")
                var[start_index:end_index, ...] = result_data[:]
                del result_data
                ds.sync()
                start_index = end_index
                start = end
                end = time.time()
                last = end - start
                cumulative += last
                eta = cumulative / (start_index + 1) * no_slices
                logger.info(
                    f"Finished {result_id} in (last cum eta): "
                    f"{last:4.0f} {cumulative:4.0f} {eta:4.0f}"
                )
    else:
        logger.info("Storing non-iteratively")
        logger.debug("Computing result")
        r = client.compute(data)  # type: ignore
        progress(r)
        result.data = r.result()
        # Touch coord data to realize before save
        for coord in result.coords():
            coord.points
            coord.bounds
        logger.debug("Storing result")
        with iris.config.netcdf.context(conventions_override=conventions_override):
            iris.save(
                result,
                temporary_filename,
                local_keys=["proposed_standard_name"],
                zlib=True,
                complevel=1,
                chunksizes=data.chunksize,
                fill_value=MISSVAL,
            )
    logger.info("Calculation complete, renaming result file")
    if os.path.exists(output_filename):
        logger.info(
            "Output file %s already exists; force is in effect; " "overwriting.",
            output_filename,
        )
        os.remove(output_filename)
    os.rename(temporary_filename, output_filename)
    logger.info("Renamed result file")
