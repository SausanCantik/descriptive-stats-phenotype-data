'''
Defining a function which return data dimension,
is there any column with null data and if yes, how many
'''

def nullstats(dataframe) :
    #dataframe = loaddata(excel_path)
    print ('Data dimension : ', dataframe.shape)
    print ( 'Is there any column with null data ? ', dataframe.isnull().any().any())
    null_name, length = null_column(dataframe)
    print ( 'How many colum with null data ?', length)
