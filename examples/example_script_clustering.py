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

#Clustering:-------------------------------------------------------------------

img_label = PyRaTe.clustering(band_list,6,1)

#Labelling:--------------------------------------------------------------------

#Label choice:

labels_code = ['vegetation_1','vegetation_2','urban_1','water','field','urban_2']

#Display the predicted labels:

PyRaTe.label_display(img_label,band_bounds,labels_code)
