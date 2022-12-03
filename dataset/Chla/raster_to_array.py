import xarray as xr
import numpy as np
import os
import matplotlib.pyplot as plt

def data_siap(path, path_data):
    
    full_path = os.path.join(path, path_data)
    data = xr.open_dataset(full_path)
    sliced_data = data.sel(lon=slice(120,150),lat=slice(35,10))
    xr.Dataset.close(data)
    
    return sliced_data
  
  
def irisan(data1, data2):
    masking_2 = (data1.where(data2>0)).fillna(np.nan)
    
    return masking_2

def interpolasi(data, referensi):
    new_lon = np.linspace(referensi.lon[0], referensi.lon[-1], referensi.dims["lon"])
    new_lat = np.linspace(referensi.lat[0], referensi.lat[-1], referensi.dims["lat"])
    
    data = data.interp(latitude=new_lat, longitude=new_lon)
    
    return data

list_data = os.listdir('./DATA')
path = "D:\DATASET\MODIS_DAILY\DATA"

ds = xr.open_dataset("u_v_data_mau_diresize.nc")

def make_dataset():
    
    for i in range(len(list_data)):
        path_data_1 = list_data[i]
        path_data_2 = list_data[i+1]
        
        data1 = data_siap(path, path_data_1)
        data2 = data_siap(path, path_data_2)
        
        data1 = irisan(data1, data2)
        data2 = irisan(data2, data1)
        
        u10_1= interpolasi(ds.u10.sel(time='2002-10-01')[0], data1).to_numpy()
        v10_1= interpolasi(ds.v10.sel(time='2002/10/01')[0], data1).to_numpy()
        
        u10_2= interpolasi(ds.u10.sel(time='2002-10-01')[1], data1).to_numpy()
        v10_2= interpolasi(ds.v10.sel(time='2002/10/01')[1], data1).to_numpy()
        
        u10_3= interpolasi(ds.u10.sel(time='2002-10-01')[2], data1).to_numpy()
        v10_3= interpolasi(ds.v10.sel(time='2002/10/01')[2], data1).to_numpy()
        
        u10_4= interpolasi(ds.u10.sel(time='2002-10-01')[3], data1).to_numpy()
        v10_4= interpolasi(ds.v10.sel(time='2002/10/01')[3], data1).to_numpy()
        
        data1 = data1.assign(u10_1=(['lat','lon'],u10_1))
        data1 = data1.assign(v10_1=(['lat','lon'],v10_1))
        
        data1 = data1.assign(u10_2=(['lat','lon'],u10_2))
        data1 = data1.assign(v10_2=(['lat','lon'],v10_2))
        
        data1 = data1.assign(u10_3=(['lat','lon'],u10_3))
        data1 = data1.assign(v10_3=(['lat','lon'],v10_3))
        
        data1 = data1.assign(u10_4=(['lat','lon'],u10_4))
        data1 = data1.assign(v10_4=(['lat','lon'],v10_4))
        
        break
    return data1


#test
data = make_dataset()

path_data_1 = list_data[0]
path_data_2 = list_data[1]

data1 = data_siap(path, path_data_1)
data2 = data_siap(path, path_data_2)

data1 = irisan(data1, data2)
data2 = irisan(data2, data1)

ds = xr.open_dataset("u_v_data_mau_diresize.nc")
#ds = xr.open_dataset("angin20021001.nc")

u10 = ds.u10.sel(time='2002-10-01')[0]
v10 = ds.v10.sel(time='2002-10-01')[0]

v10 = interpolasi(u10, data1)

new_lon = np.linspace(u10.longitude[0], u10.longitude[-1], data1.dims["lon"])
new_lat = np.linspace(u10.latitude[0], u10.latitude[-1], data1.dims["lat"])

v10 = v10.interp(latitude=new_lat, longitude=new_lon)
u10 = u10.interp(latitude=new_lat, longitude=new_lon)

u10.to_netcdf('u10_20021001.nc')
v10.to_netcdf('v10_20021001.nc')

tes = u10.to_numpy()
tes2 = v10.to_numpy()
data1 = data1.assign(u10=(['lat','lon'],tes))
data1 = data1.assign(v10=(['lat','lon'],tes2))

#TEST PLOT
(data1.u10.where(data1.chlor_a>0)).fillna(np.nan).plot()

(data1.v10.where(data1.chlor_a>0)).fillna(np.nan).plot()

array_jadi = (data1.v10.where(data1.chlor_a>0)).fillna(np.nan).to_numpy()
