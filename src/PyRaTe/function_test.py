###############################################################################
#HEADER

#This function 

###############################################################################

#Function definition:----------------------------------------------------------

def test(classifier_pipeline,df_input):
    
    features = df_input.drop(columns=['label'])
    labels = df_input['label']
    
    print("Test accuracy:")
    print(classifier_pipeline.score(features,labels))