import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import os

path = ""
path_data = os.listdir(path)

def data_siap(path, path_data):
    
    full_path = os.path.join(path, path_data)
    data = xr.open_dataset(full_path)
    
    tanggal = path_data[:8]
    times = pd.date_range(tanggal, tanggal, freq='MS', inclusive="left")
    
    time_da = xr.DataArray(times, [('time', times)])
    data = data.expand_dims(time=time_da)
    
    return data

data_gabungan = xr.concat([data_siap(path, path_data[0]), data_siap(path, path_data[1]), data_siap(path, path_data[2])], dim='time')

data_gabungan
