import xarray as xr
import numpy as np
import netCDF4 as nc4


def test_open_subgroup(tmp_path) -> None:
    # Create a netCDF file with a dataset stored within a group within a
    # group
    tmp_file = tmp_path / 'test.nc'
    rootgrp = nc4.Dataset(tmp_file, "w")
    foogrp = rootgrp.createGroup("foo")
    bargrp = foogrp.createGroup("bar")
    ds = bargrp
    ds.createDimension("time", size=10)
    x = np.arange(10)
    ds.createVariable("x", np.int32, dimensions=("time", ))
    ds.variables["x"][:] = x
    rootgrp.close()

    expected = xr.Dataset()
    expected["x"] = ("time", x)

    # check equivalent ways to specify group
    for group in "foo/bar", "/foo/bar", "foo/bar/", "/foo/bar/":
        actual = xr.open_dataset(tmp_file, engine='netcdf4', group=group)
        assert np.all(actual["x"] == expected["x"])

        hfx = xr.open_dataset(tmp_file, engine='hidefix', group=group)
        assert np.all(hfx["x"] == expected["x"])
