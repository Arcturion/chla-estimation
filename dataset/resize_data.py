import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

ds = xr.open_dataset("u_v_data_mau_diresize.nc")
ds = ds.sel(time='2002-01')
target = xr.open_dataset("eaeaea.nc")

for y in range(2002, 2003):
    for m in range(1, 2):
        ds_sel = ds.sel(time=np.isin(ds.time.dt.month, m))
        ds_sel = ds.sel(time=np.isin(ds.time.dt.year, y))
        ds_sel = ds_sel.mean(dim='time')
        
        new_lon = np.linspace(ds_sel.longitude[0], ds_sel.longitude[-1], target.dims["lon"])
        new_lat = np.linspace(ds_sel.latitude[0], ds_sel.latitude[-1], target.dims["lat"])
        
        dsi = ds_sel.interp(latitude=new_lat, longitude=new_lon)
        dsi.to_netcdf(str(y)+"{:02d}".format(m)+".nc")

dsi.v10.plot()

