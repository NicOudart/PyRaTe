###############################################################################
#HEADER

#This function 

###############################################################################

#Libraries importation:--------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap,BoundaryNorm

#Function definition:----------------------------------------------------------

def label_display(img_label,band_bounds,labels_code):
    
    nb_labels = len(labels_code)
    
    lon_min,lon_max = band_bounds.left,band_bounds.right
    lat_min,lat_max = band_bounds.bottom,band_bounds.top
    
    cmap = plt.get_cmap("tab10",nb_labels)
    norm = BoundaryNorm(np.arange(-0.5,nb_labels+0.5,1),nb_labels)
    
    fig,ax = plt.subplots()
    img = ax.imshow(img_label,extent=[lon_min,lon_max,lat_min,lat_max],origin='upper',cmap=cmap,norm=norm)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    
    colorbar = plt.colorbar(img,ticks=np.arange(nb_labels))
    colorbar.ax.set_yticklabels(labels_code)
    
    plt.show()