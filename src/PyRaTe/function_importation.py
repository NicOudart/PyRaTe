###############################################################################
#HEADER

#This function 

###############################################################################

#Libraries importation:--------------------------------------------------------

import os
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QFileDialog

import rasterio

#Function definition:----------------------------------------------------------

def importation():
    
    #Dialog window to import the GeoTIFF files:--------------------------------
    
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
        
    root_path = os.path.abspath(os.sep)

    file_path,_ = QFileDialog.getOpenFileNames(None,"Select GeoTIFF files",root_path,"All files (*)")
    
    #Read the different bands of the image and their bounds:-------------------
    
    band_list = []
    band_bounds_list = []
    
    for file in file_path:
        
        geotiff = rasterio.open(file)
        
        img = geotiff.read()
        
        for band in img:
            
            max_pixel = np.iinfo(band.dtype).max
            norm_band = band.astype(np.float32)/max_pixel
            
            band_list += [norm_band]
            
        band_bounds = geotiff.bounds
        
        band_bounds_list += [band_bounds]
            
        geotiff.close()
        
    #Check the bounds consistency and keep only one:---------------------------
        
    band_bounds_set = set(band_bounds_list)
    
    if len(band_bounds_set)==1:
        
        band_band_bounds = next(iter(band_bounds_set))
    
    else:
        
        raise ValueError('Inconsistency between the different GeoTIFF files !')
        
    #Return the list of raster bands and the bounds:---------------------------
        
    return band_list,band_band_bounds
        
        