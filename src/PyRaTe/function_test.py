###############################################################################
#HEADER

#This function 

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