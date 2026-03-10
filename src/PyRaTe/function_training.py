###############################################################################
#HEADER

#This function allows you to train a Naive Bayes classifier pipeline on a 
#labelled dataset of pixels.

#Inputs:
# - df_input: Pandas DataFrame containing the labelled dataset of pixels.

#Outputs:
# - classifier_pipeline: Scikit-Learn trained classifier pipeline.

###############################################################################

#Libraries importation:--------------------------------------------------------

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB

#Function definition:----------------------------------------------------------

def training(df_input):
    
    features = df_input.drop(columns=['label'])
    labels = df_input['label']
    
    classifier_pipeline = Pipeline([('scaler',StandardScaler()),('gnb',GaussianNB())])
    
    classifier_pipeline.fit(features,labels)
    
    print("Training accuracy:")
    print(classifier_pipeline.score(features,labels))
    
    return classifier_pipeline