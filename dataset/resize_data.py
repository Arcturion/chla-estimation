import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

ds = xr.open_dataset("u_v_data_mau_diresize.nc").isel(time=60)
target = xr.open_dataset("eaeaea.nc")

new_lon = np.linspace(ds.longitude[0], ds.longitude[-1], target.dims["lon"])
new_lat = np.linspace(ds.latitude[0], ds.latitude[-1], target.dims["lat"])

#INTERPOLASI
dsi = ds.interp(latitude=new_lat, longitude=new_lon)

