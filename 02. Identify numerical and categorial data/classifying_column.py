'''
A function to define whether the data in the column is numerical
or categorial
'''

def classifying_column(dataframe) :
    numeric = [] #list column name with numerical data
    categorial = [] #list column name with categorial data
    col_index = indexingcolumn(dataframe)
    
    for i in range (len(list(dataframe))) :
        if i == 0 :
            print ('Excluded column : ', col_index[i], '\n')
        else :
            entry = len(dataframe[col_index[i]].unique())
            if  entry > 5 :
                numeric.append(col_index[i])
            else :
                categorial.append(col_index[i])
    return numeric, categorial
