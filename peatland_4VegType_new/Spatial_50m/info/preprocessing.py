import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal, gdalconst, osr
from inverseDistanceWeightedInterpolation import tree

def readtif(fn):

    ds = gdal.Open(fn, gdalconst.GA_ReadOnly)
    band = ds.GetRasterBand(1)
    data = band.ReadAsArray()
    return ds, data

def savetif(ds, data, fn, nodataValue):
    file_driver = gdal.GetDriverByName('Gtiff')
    band = ds.GetRasterBand(1)
    output_dataset = file_driver.Create(fn, band.XSize, band.YSize, 1,
                                        band.DataType)
    output_dataset.SetProjection(ds.GetProjection())
    output_dataset.SetGeoTransform(ds.GetGeoTransform())
    output_dataset.GetRasterBand(1).SetNoDataValue(nodataValue)
    output_dataset.GetRasterBand(1).WriteArray(data)

def readasc(fn):
    arr = np.loadtxt(fn, skiprows=6)
    return arr

def savetasc(fileName,arr):
    np.savetxt(fileName, arr)

    line1 = "ncols         80"
    line2 = "nrows         220"
    line3 = "xllcorner     447125"
    line4 = "yllcorner     5806065"
    line5 = "cellsize      10"
    line6 = "NODATA_value  -9999"
    with open(fileName, "r+") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5 + '\n' + line6 + '\n' + content)

def saveasc_50m(fileName,arr):
    np.savetxt(fileName, arr)
    line1 = "ncols         18"
    line2 = "nrows         43"
    line3 = "xllcorner     447078.2773"
    line4 = "yllcorner     5806051.289"
    line5 = "cellsize      50"
    line6 = "NODATA_value  -9999"
    with open(fileName, "r+") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5 + '\n' + line6 + '\n' + content)

def addNanBounds(fileName):
    arr = np.loadtxt('./source/'+fileName,skiprows=6)
    newarr = np.full((arr.shape[0]-2, arr.shape[1]+2), -9999.0)
    newarr[1:-1,1:-1] = arr[:39,:]

    np.savetxt(fileName, newarr)
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


def plot(data):
    plt.imshow(data, cmap='cool')
    plt.show()


dem = readasc('D:\OneDrive\Phd\WorkPackages/4\paper6\data\gis_peatland\spatial\info/source/dem.asc')

ds, mainStream_mask = readtif('D:\OneDrive\Phd\WorkPackages/4\paper6\data/gis/tmp/mainStream_mask.tif')
ds, tributaries_mask = readtif('D:\OneDrive\Phd\WorkPackages/4\paper6\data/gis/tmp/tributaries_mask.tif')

tributaries_mask[mainStream_mask==1] = 0
chanmask = (mainStream_mask+tributaries_mask).astype(np.float64)
chanmask[chanmask>0] = 1
chanmask[chanmask<1] = -9999
chanmask[dem<0] = -9999
saveasc_50m('./source/chanmask.asc',chanmask)




corr_streamDepthWidth_project = np.loadtxt('D:\OneDrive\Phd\WorkPackages/3\data\GIS/streamDepthWidth.txt', skiprows=1, delimiter=',')
xlist = corr_streamDepthWidth_project[:, -4]
ylist = corr_streamDepthWidth_project[:, -3]
depthList = corr_streamDepthWidth_project[:, 6] / 100
widthList = corr_streamDepthWidth_project[:, 7]

prosrs = ds.GetSpatialRef()
prosrs.ImportFromWkt(ds.GetProjection())
geosrs = prosrs.CloneGeogCS()
ct = osr.CoordinateTransformation(geosrs, prosrs)

X1 = np.full((len(xlist),2), np.nan)
for i in range(len(xlist)):
    coords = ct.TransformPoint(xlist[i], ylist[i])
    X1[i,:] = [coords[0], coords[1]]

# 'train'
idw_tree_width = tree(X1, widthList)
idw_tree_depth = tree(X1, depthList)

# 'test'
spacingx = np.arange(447078.2773, 447078.2773+50*18, 50)[::-1]
spacingy = np.arange(5806051.289, 5806051.289+50*43, 50)[::-1]
print(spacingy.shape)
X2 = np.meshgrid(spacingx, spacingy)
grid_shape = X2[0].shape
X2 = np.reshape(X2, (2, -1)).T
z2 = idw_tree_width(X2)
z_width = z2.reshape(grid_shape)
z2 = idw_tree_depth(X2)
z_depth = z2.reshape(grid_shape)
z_width = z_width*1.5
z_width[tributaries_mask==1] = 1.5
z_width[chanmask<0] = -9999
z_depth[chanmask<0] = -9999

saveasc_50m('./source/chanwidth.asc',z_width)


FileName = ['chanmask','chanwidth','ClimZones','dem','patches','type1','type2']
for fn in FileName:
    addNanBounds(fn+'.asc')