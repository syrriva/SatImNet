# In order to read many images via the _vsicurl_ driver, please use the command _gdal.VSICurlClearCache()_ after every _gdalRead_ command.

import numpy as np
from osgeo import gdal, osr
import os
os.environ["GDAL_HTTP_MULTIRANGE"]="SERIAL"

def gdalRead(infile):
    src = gdal.Open(infile)
    if infile.split('.')[-1] in ['jpg', 'png']:
        Info = {
                    'projection': '-',
                    'geotransform': '-',
                    'EPSG': '-',
                    'datatype': gdal.GetDataTypeName(src.GetRasterBand(1).DataType),
                    'columns': src.RasterXSize,
                    'rows': src.RasterYSize,
                    'numofbands': src.RasterCount
                }
    else:
        proj = osr.SpatialReference(wkt=src.GetProjection())
        Info = {
                    'projection': src.GetProjection(),
                    'geotransform': src.GetGeoTransform(),
                    'EPSG': proj.GetAttrValue('AUTHORITY',1),
                    'datatype': gdal.GetDataTypeName(src.GetRasterBand(1).DataType),
                    'columns': src.RasterXSize,
                    'rows': src.RasterYSize,
                    'numofbands': src.RasterCount
                }
    Image = np.zeros((src.RasterYSize, src.RasterXSize, src.RasterCount), dtype=NP2GDAL_CONVERSION[Info['datatype']])
    for band in range(Image.shape[2]):
        Image[:,:,band] = src.GetRasterBand(band+1).ReadAsArray()
    del src
    gdal.VSICurlClearCache()
    return Info, np.squeeze(Image)

NP2GDAL_CONVERSION = {
  "Byte": np.uint8,
  "UInt16": np.uint16  
}