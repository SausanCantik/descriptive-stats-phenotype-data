'''
A function to add accession_group as a column in phenotype data and
encode the entries
'''

def column_expansion (dataframe):       
    accession_group = string_split(dataframe)
    
    #encode the entries
    from sklearn import preprocessing #input encoder library
    
    le = preprocessing.LabelEncoder()
    accession_group = le.fit(accession_group).transform(accession_group)
           
    #Add column 'accession_group' to dataframe
    dataframe['Accession_group'] = accession_group
    
    return dataframe
