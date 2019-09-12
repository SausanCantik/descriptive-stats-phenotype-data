#A function to show the list of trait with categorial data

def categorial_trait(dataframe):
    numeric, categorial = classifying_column(dataframe)
    print('Traits with categorial data : ','\n',categorial, '\n')
    print('Total count : ' ,len(categorial) , 'Traits')
