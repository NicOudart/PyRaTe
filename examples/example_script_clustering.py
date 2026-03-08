###############################################################################
#HEADER

#This script 

###############################################################################

#Libraries importation:--------------------------------------------------------

import PyRaTe

#Dataset preparation:----------------------------------------------------------

#GeoTIFF image bands importation:
#(An example set of 9 bands GeoTIFF files is available in the example/dataset
#directory).

band_list,band_bounds = PyRaTe.importation()

#RBG image display:

PyRaTe.img_display(band_list,band_bounds,display_rgb=[3,2,1])