import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ds = xr.open_dataset("u_v_data_mau_diresize.nc")
target = xr.open_dataset("eaeaea.nc")

year = ['2002','2003']

year_month_idx = pd.MultiIndex.from_arrays([np.array(ds['time.year']), np.array(ds['time.month'])])
ds.coords['year_month'] = ('time', year_month_idx)
ds_mean = ds.groupby('year_month').mean()

new_lon = np.linspace(ds_mean.longitude[0], ds_mean.longitude[-1], target.dims["lon"])
new_lat = np.linspace(ds_mean.latitude[0], ds_mean.latitude[-1], target.dims["lat"])

dsi = ds_mean.interp(latitude=new_lat, longitude=new_lon)

dsi.sel(year_month=ds_mean.year_month[238]).u10.plot()

#kalo mau export ke netcdf kudu disatuin index waktunya
dsi = dsi.reset_index('year_month', drop=False)

dsi.to_netcdf('angin_bulanan.nc')
