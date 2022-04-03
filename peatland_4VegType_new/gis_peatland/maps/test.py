from osgeo import gdal, gdalconst
#from gdalconst import *
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import scipy.interpolate
from inverseDistanceWeightedInterpolation import *

def savetxt(fileName, arr):

    np.savetxt(fileName, arr)
    line1 = "ncols         20"
    line2 = "nrows         41"
    line3 = "xllcorner     447028.2773"
    line4 = "yllcorner     5806201.289"
    line5 = "cellsize      50"
    line6 = "NODATA_value  -9999"
    with open(fileName, "r+") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5 + '\n' + line6 + '\n' + content)

def test1(path):
    ds1 = gdal.Open(path +'Predict_20210721_2.tif', gdalconst.GA_ReadOnly)
    band = ds1.GetRasterBand(1)

    file_driver = gdal.GetDriverByName('Gtiff')
    output_dataset = file_driver.Create(path + 'Predict_20210721_mask.tif', band.XSize, band.YSize, 1,
                                        GDT_Int16)
    output_dataset.SetProjection(ds1.GetProjection())
    output_dataset.SetGeoTransform(ds1.GetGeoTransform())
    data = ds1.GetRasterBand(1).ReadAsArray()

    data[data==16] = 7
    data[data==7]  = 3

    data[(np.logical_not(np.isnan(data)))] = 0

    data = data/2

    output_dataset.GetRasterBand(1).WriteArray(data)

def test2(path):
    for i in range(3):
        ds1 = gdal.Open(path+'predict'+str(i)+'.tif', gdalconst.GA_ReadOnly)
        band = ds1.GetRasterBand(1)
        file_driver = gdal.GetDriverByName('Gtiff')
        output_dataset = file_driver.Create(path + 'predict'+str(i)+'_modified.tif', band.XSize, band.YSize, 1,
                                            band.DataType)
        output_dataset.SetProjection(ds1.GetProjection())
        output_dataset.SetGeoTransform(ds1.GetGeoTransform())
        data = ds1.GetRasterBand(1).ReadAsArray()

        data[:, -4] = -1
        data[data<0] = np.nan

        data_new1 = IDW_raster(data, powerNum = -2)
        data_new2 = IDW_raster(data, powerNum = -5)



        fig, ax = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(15, 7))

        ax[0].imshow(data)
        ax[1].imshow(data_new1)
        ax[2].imshow(data_new2)
        plt.show()
        output_dataset.GetRasterBand(1).WriteArray(data_new2)

def test3(path):
    ds0 = gdal.Open(path + 'predict0_modified.tif', gdalconst.GA_ReadOnly)
    ds1 = gdal.Open(path + 'predict1_modified.tif', gdalconst.GA_ReadOnly)
    ds2 = gdal.Open(path + 'predict2_modified.tif', gdalconst.GA_ReadOnly)
    data0 = ds0.GetRasterBand(1).ReadAsArray()
    data1 = ds1.GetRasterBand(1).ReadAsArray()
    data2 = ds2.GetRasterBand(1).ReadAsArray()
    data0 -= 1e-4
    data1 -= 1e-4
    data2 = 1-data0-data1
    print(np.nanmin(data2))
    p0 = np.loadtxt(path+'type1.asc', skiprows=6)
    p1 = np.loadtxt(path+'type2.asc', skiprows=6)
    p0[p0==-9999] = np.nan
    p1[p1==-9999] = np.nan
    data0 = data0*p0
    data1 = data1*p0
    data2 = data2*p0


    fig, ax = plt.subplots(1, 5, sharex=True, sharey=True, figsize=(15, 7))

    ax[0].imshow(data0, vmin=0, vmax=1)
    ax[1].imshow(data1, vmin=0, vmax=1)
    ax[2].imshow(data2, vmin=0, vmax=1)
    ax[3].imshow(p1, vmin=0, vmax=1)
    ax[4].imshow(data0+data1+data2+p1, vmin=0, vmax=1)
    #plt.show()

    data0 -= 1e-3
    data1 -= 1e-3
    data2 -= 1e-3
    p1 -= 1e-3

    data0[data0<0] = 0
    data1[data1<0] = 0
    data2[data2<0] = 0
    p1[p1<0] = 0

    data0[np.isnan(data0)] = -9999.0
    data1[np.isnan(data1)] = -9999.0
    data2[np.isnan(data2)] = -9999.0
    p1[np.isnan(p1)] = -9999.0

    print(np.nanmax(data0+data1+data2+p1))

    savetxt('p0.asc', data0)
    savetxt('p1.asc', data1)
    savetxt('p2.asc', data2)
    savetxt('p3.asc', p1)

    tmp = np.full((data0.shape[0], data0.shape[1], 4), np.nan)
    tmp[:,:,0] = data0
    tmp[:,:,1] = data1
    tmp[:,:,2] = data2
    tmp[:,:,3] = p1
    patches = np.argmax(tmp, axis = 2).astype(np.float64)
    patches[p1==-9999.0] = np.nan
    patches += 1
    patches[np.isnan(patches)] = -9999.0


    savetxt('patches.asc', patches)






    #output_dataset.GetRasterBand(1).WriteArray(data_new2)



path = r'C:\Users\songjunwu\Documents\files_Songjun\peatlandModelling/maps/'
test3(path)