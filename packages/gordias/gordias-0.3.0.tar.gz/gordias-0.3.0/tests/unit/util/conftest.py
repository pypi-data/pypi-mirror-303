"""Module for test fixtures."""

import iris.cube
import pytest


def add_dim_coord(cube, coord):
    """Add time dimension coordinates to cube."""
    shape = cube.data.shape
    assert len(shape) == 3
    coord.guess_bounds()
    cube.add_dim_coord(coord, 0)


def add_aux_coord(cube, coord):
    """Add auxiliary coordinates to cube."""
    cube.add_aux_coord(coord)


@pytest.fixture
def f_cube(request) -> iris.cube.Cube:
    """Fixture for creating a iris cube."""
    test_cube = request.param["cube"]
    if "dim_coord_time" in request.param:
        add_dim_coord(test_cube, request.param["dim_coord_time"])
    if "aux_coord" in request.param:
        add_aux_coord(test_cube, request.param["aux_coord"])
    if test_cube.coord("time").bounds is None:
        test_cube.coord("time").guess_bounds()
    return test_cube
