###############################################################################
#HEADER

#This function 

###############################################################################

#Libraries importation:--------------------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

#Function definition:----------------------------------------------------------

def dataset_statistics(df_input):
    
    nb_columns = len(df_input.columns)
    
    for col in range(nb_columns-1):
        
        plt.figure()
        sns.histplot(data=df_input,x='band_'+str(col),hue='label')
        plt.title('Band '+str(col)+' histogram')