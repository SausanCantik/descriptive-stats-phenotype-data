# A function to get all the column index in which the column contain null

def null_column(dataframe):
    null = list(dataframe.isnull().any())
    index = []
    null_name = []
    for i in range(len(null)):
        if null[i] == True :
            index.append(i)
            col_index = indexingcolumn(dataframe)
            null_name.append(col_index[i])
    length = len(null_name)
    return null_name, length
