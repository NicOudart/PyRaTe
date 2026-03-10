###############################################################################
#HEADER

#This function allows you to test the performances of a trained classifier 
#pipeline on a labelled dataset of pixels.

#Inputs:
# - classifier_pipeline: Scikit-Learn trained classifier pipeline.
# - df_input: Pandas DataFrame containing the labelled dataset of pixels.

#Outputs: None

###############################################################################

#Libraries importation:--------------------------------------------------------

from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay

#Function definition:----------------------------------------------------------

def test(classifier_pipeline,df_input):
    
    features = df_input.drop(columns=['label'])
    labels = df_input['label']
    
    set_labels = sorted(set(labels))
    
    print("Test accuracy:")
    print(classifier_pipeline.score(features,labels))
    
    cm = confusion_matrix(labels,classifier_pipeline.predict(features),labels=set_labels)
    ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=set_labels).plot()