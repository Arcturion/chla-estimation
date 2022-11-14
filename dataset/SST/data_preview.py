import xarray as xr
import numpy as np
import os
import matplotlib.pyplot as plt

path = "D:\DATASET\SST_AMSR2"
path_data = "RSS_AMSR2_ocean_L3_daily_2022-11-11_v08.2.nc"

full_path = os.path.join(path, path_data)
data = xr.open_dataset(full_path)

path_data = "hima.nc"

full_path_hima = os.path.join(path, path_data)
data_hima = xr.open_dataset(full_path_hima)

sliced_data_hima = data_hima.sel(lon=slice(100,150),lat=slice(-1,35))
sliced_data_hima.sea_surface_temperature.plot()

data.SST[0].plot()

sliced_data = data.sel(lon=slice(100,200),lat=slice(0,35))
sliced_data.SST[0].plot()
