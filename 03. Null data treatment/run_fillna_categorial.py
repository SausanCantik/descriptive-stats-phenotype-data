#Function to run fillna_categorial
def run_fillna_categorial(excel_path) :
    dataframe = loaddata(excel_path)
    numeric, categorial = classifying_column(dataframe) #prone to changes
    df = fillna_categorial(categorial, dataframe)
    null_name, length = null_column(df)
    
    print ( 'How many colum with null data remaining?', length)
    print ('\n', null_name)
