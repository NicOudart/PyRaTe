###############################################################################
#HEADER

#This function allows you to display 3 bands of imported GeoTIFF as a 
#georeferenced RGB image.

#Inputs:
# - band_list: list of arrays containing the bands of the imported GeoTIFF.
# - bands_bounds: georeferencing for the image.
# - co_polar: int corresponding to the co-polar band index in the list.
# - cross_polar : int corresponding to the cross-polar band index in the list.

#Outputs: None

###############################################################################

#Libraries importation:--------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

#Function definition:----------------------------------------------------------

def radar_display(band_list,band_bounds,co_polar=0,cross_polar=1):
    
    x_len,y_len = np.shape(band_list[0])
    
    lon_min,lon_max = band_bounds.left,band_bounds.right
    lat_min,lat_max = band_bounds.bottom,band_bounds.top
    
    #RGB image generation:-----------------------------------------------------
    
    co_band = band_list[co_polar]
    cross_band = band_list[cross_polar]
    polar_ratio = np.divide(co_band,cross_band,out=np.full_like(co_band,0,dtype=float),where=cross_band!=0)
    
    co_band = 10*np.log10(co_band+1e-6)
    cross_band = 10*np.log10(cross_band+1e-6)
    polar_ratio = 10*np.log10(polar_ratio+1e-6)
    
    co_low, co_high = np.percentile(co_band,(2,98))
    cross_low, cross_high = np.percentile(cross_band,(2,98))
    polar_ratio_low, polar_ratio_high = np.percentile(polar_ratio,(2,98))
    
    co_band = (co_band-co_low)/(co_high-co_low)
    cross_band = (cross_band-cross_low)/(cross_high-cross_low)
    polar_ratio = (polar_ratio-polar_ratio_low)/(polar_ratio_high-polar_ratio_low)
    
    co_band = np.clip(co_band,0,1)
    cross_band = np.clip(cross_band,0,1)
    polar_ratio = np.clip(polar_ratio,0,1)
        
    img_rgb = np.stack((cross_band,co_band,polar_ratio),axis=-1)
    
    #Display:------------------------------------------------------------------
    
    fig,ax = plt.subplots()
    ax.imshow(img_rgb,extent=[lon_min,lon_max,lat_min,lat_max],origin='upper')
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    
    plt.show()