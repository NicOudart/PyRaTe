###############################################################################
#HEADER

#This script proposes a complete supervised classification process of pixels 
#from a satellite raster image:
# - GeoTIFF image importation (several bands).
# - RGB georeferenced display.
# - Training dataset preparation.
# - Statistical study of the training dataset.
# - Training of a pixel classifier.
# - Test dataset preparation, and test of the classifier.
# - Prediction and labelled display.

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

#Label a training dataset:

df_training = PyRaTe.labelling(band_list,display_rgb=[3,2,1])

#Statistics:-------------------------------------------------------------------

PyRaTe.dataset_statistics(df_training)

#Training:---------------------------------------------------------------------

#Train a Naive Bayes classifier pipeline on this training dataset:

classifier_pipeline = PyRaTe.training(df_training)

#Test:-------------------------------------------------------------------------

#Label a test dataset:

df_test = PyRaTe.labelling(band_list,display_rgb=[3,2,1])

#Test the classifier:
    
PyRaTe.test(classifier_pipeline,df_test)

#Prediction:-------------------------------------------------------------------

#Predict all pixels in the GeoTIFF:

img_label,labels_code = PyRaTe.prediction(classifier_pipeline,band_list)

#Display the predicted labels:

PyRaTe.label_display(img_label,band_bounds,labels_code)
