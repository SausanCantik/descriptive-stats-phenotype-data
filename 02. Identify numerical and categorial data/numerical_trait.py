#A function to show the list of trait with numerical data from dataframe

def numerical_trait(dataframe):
    numeric, categorial = classifying_column(dataframe)
    print('Traits with numerical data : ','\n',numeric, '\n')
    print('Total count : ' ,len(numeric) ,'Traits')
