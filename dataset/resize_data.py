import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

ds = xr.open_dataset("u_v_data_mau_diresize.nc")
target = xr.open_dataset("eaeaea.nc")

# took the code from https://github.com/kbongi/models/blob/c6ecfa7facbd836965b37e5715b2f9ae3ee4d4e9/frequently_used_functions.py
def monthly_mean(dataset, start_date, end_date):
    
    #variable_monthly = dataset.groupby('time.month')

    monthly_mean = dataset.sel(time = slice(f'{start_date}', f'{end_date}')).groupby('time.month').mean(dim = 'time')

    return monthly_mean

year = ['2002','2003']
for y in year:
    ds_mean = monthly_mean(ds, y, y)
    for m in range(1, 13):        
        new_lon = np.linspace(ds_sel.longitude[0], ds_sel.longitude[-1], target.dims["lon"])
        new_lat = np.linspace(ds_sel.latitude[0], ds_sel.latitude[-1], target.dims["lat"])
        
        dsi = ds_sel.interp(latitude=new_lat, longitude=new_lon)
        dsi.to_netcdf(str(y)+"{:02d}".format(m)+".nc")

dsi.v10.plot()

