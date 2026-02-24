###############################################################################
#HEADER

#This function 

###############################################################################

#Libraries importation:--------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox,RectangleSelector,Button

#Function definition:----------------------------------------------------------

def labelling(band_list,display_rgb=[0,1,2]):
    
    #Variables initialization:-------------------------------------------------
    
    label = ''
    finished = False
    
    dict_output = {}
    for band_nb in range(len(band_list)):
        dict_output['band_'+str(band_nb)] = []
    dict_output['label'] = []
    
    #Matplotlib widgets methods:-----------------------------------------------
    
    def submit(text):
        nonlocal label
        label = text
        
    def onselect(eclick,erelease):
        nonlocal dict_output
        nonlocal label
        y1,x1 = int(eclick.xdata), int(eclick.ydata)
        y2,x2 = int(erelease.xdata), int(erelease.ydata)
        x_min = min(x1,x2)
        x_max = max(x1,x2)
        y_min = min(y1,y2)
        y_max = max(y1,y2)
        nb_pixels = 0
        for x in range(x_min,x_max+1):
            for y in range(y_min,y_max+1):
                for band_nb in range(len(band_list)):
                    dict_output['band_'+str(band_nb)] += [band_list[band_nb][x,y]]
                dict_output['label'] += [label]
                nb_pixels += 1
        print(str(nb_pixels)+' pixels assigned to label '+label)
                
    def finish(event):
        nonlocal finished
        finished = True
    
    #RGB image generation:-----------------------------------------------------
    
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
    
    #RGB image display:--------------------------------------------------------
    
    fig,ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    ax.imshow(img_rgb,origin='upper')
    ax.set_title('Enter a label and select a rectangle on the image')
    
    #Define the Matplotlib widgets:--------------------------------------------

    ax_box = plt.axes([0.2, 0.1, 0.6, 0.05])
    ax.text_box = TextBox(ax_box,'Label: ')
    
    ax_button = plt.axes([0.8, 0.01, 0.15, 0.05])
    ax.button = Button(ax_button,'Finish')
    
    ax.selector = RectangleSelector(ax,onselect,useblit=True,button=[1],interactive=True)
    ax.text_box.on_submit(submit)
    ax.button.on_clicked(finish)
    
    #Loop until the dataset is finished:---------------------------------------
    
    while not finished:
        plt.pause(0.01)
        
    plt.close(fig)
    
    #Return the dataset as a Pandas DataFrame:---------------------------------
    
    df_output = pd.DataFrame(dict_output)
    
    return df_output