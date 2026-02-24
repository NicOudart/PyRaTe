###############################################################################
#HEADER

#This function 

###############################################################################

#Libraries importation:--------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

#Function definition:----------------------------------------------------------

def img_display(band_list,band_bounds,display_rgb=[0,1,2]):
    
    x_len,y_len = np.shape(band_list[0])
    
    lon_min,lon_max = band_bounds.left,band_bounds.right
    lat_min,lat_max = band_bounds.bottom,band_bounds.top
    
    red = band_list[display_rgb[0]]
    green = band_list[display_rgb[1]]
    blue = band_list[display_rgb[2]]
    
    red_low, red_high = np.percentile(red,(2,98))
    green_low, green_high = np.percentile(green,(2,98))
    blue_low, blue_high = np.percentile(blue,(2,98))
    
    red = (red-red_low)/(red_high-red_low)
    green = (green-green_low)/(green_high-green_low)
    blue = (blue-blue_low)/(blue_high-blue_low)
    
    red = np.clip(red,0,1)
    green = np.clip(green,0,1)
    blue = np.clip(blue,0,1)
    
    img_rgb = np.stack((red,green,blue),axis=-1)
    
    fig,ax = plt.subplots()
    ax.imshow(img_rgb,extent=[lon_min,lon_max,lat_min,lat_max],origin='upper')
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    
    plt.show()