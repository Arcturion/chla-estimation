import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import os

path = ""
path_data = os.listdir(path)

full_path1 = os.path.join(path, path_data[0])
full_path2 = os.path.join(path, path_data[0])

data_stack = xr.open_dataset(full_path2)
data_input = xr.open_dataset(full_path1)

times = pd.date_range("2002/01/01","2002/02/02",freq='MS', inclusive="left")
times2 = pd.date_range("2002/02/01","2002/03/02",freq='MS', inclusive="left")

time_da = xr.DataArray(times, [('time', times)])
time_da2 = xr.DataArray(times2, [('time', times)])

data_input = data_input.expand_dims(time=time_da)
data_stack = data_stack.expand_dims(time=time_da2)

data_gabungan = xr.concat([data_input, data_stack], dim='time')

data_gabungan
