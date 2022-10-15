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

flist1 = [1,2,3]
data_gabungan = xr.concat([data_stack, data_input],dim=['time','lon','lat'])

data_gabungan
