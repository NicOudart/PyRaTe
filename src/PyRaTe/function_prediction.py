###############################################################################
#HEADER

#This function allows you to predict the identification of pixels in an 
#imported image with a trained classifier pipeline.

#Inputs:
# - classifier_pipeline: Scikit-Learn trained classifier pipeline.
# - band_list: list of arrays containing the bands of the imported GeoTIFF.

#Outputs:
# - img_label: array of int of the same dimensions as the input image, 
#              corresponding to the clusters assigned to every pixel in the 
#              image.
# - label_code: list of str containing the labels corresponding to intergers in
#               img_label array.

###############################################################################

#Libraries importation:--------------------------------------------------------

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#Function definition:----------------------------------------------------------

def prediction(classifier_pipeline,band_list):
    
    dict_img = {'pixel_x': [],'pixel_y': []}
    for band_nb in range(len(band_list)):
        dict_img['band_'+str(band_nb)] = []
    
    len_x,len_y = np.shape(band_list[0])
    
    for x in range(len_x):
        for y in range(len_y):
            dict_img['pixel_x'] += [x]
            dict_img['pixel_y'] += [y]
            for band_nb in range(len(band_list)):
                dict_img['band_'+str(band_nb)] += [band_list[band_nb][x,y]]
                
    df_img = pd.DataFrame(dict_img)
                
    df_img['label'] = classifier_pipeline.predict(df_img.drop(columns=['pixel_x','pixel_y']))
    
    encoder = LabelEncoder()
    df_img['label'] = encoder.fit_transform(df_img['label'])
    labels_code = encoder.classes_
        
    img_label = np.zeros((df_img['pixel_x'].max()+1,df_img['pixel_y'].max()+1))
    
    img_label[df_img['pixel_x'],df_img['pixel_y']] = df_img['label']
    
    return img_label,labels_code       