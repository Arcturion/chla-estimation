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
    
    xr.Dataset.close(data)
    
    return data

data_gabungan = data_siap(path, path_data[0])

for t in range(1, len(path_data)):
    data_gabungan = xr.concat([data_gabungan, data_siap(path, path_data[t])], dim='time')
    print(str(t)+" of "+str(len(path_data)))

data_gabungan
