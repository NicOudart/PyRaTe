###############################################################################
#HEADER

#This function 

###############################################################################

#Libraries importation:--------------------------------------------------------

import PyRaTe

#Training:---------------------------------------------------------------------

#GeoTIFF image bands importation:

band_list,band_bounds = PyRaTe.importation()

#RBG image display:

PyRaTe.img_display(band_list,band_bounds,display_rgb=[3,2,1])

#Label a training dataset:

df_training = PyRaTe.labelling(band_list,display_rgb=[3,2,1])

#Train a classifier on this training dataset:

classifier_pipeline = PyRaTe.training(df_training)

#Predict all pixels in the GeoTIFF:

img_label,labels_code = PyRaTe.prediction(classifier_pipeline,band_list)

#Display the predicted labels:

PyRaTe.label_display(img_label,band_bounds,labels_code)

#Test:-------------------------------------------------------------------------

#Label a test dataset:

df_test = PyRaTe.labelling(band_list,display_rgb=[3,2,1])

#Test the classifier:
    
PyRaTe.test(classifier_pipeline,df_test)
