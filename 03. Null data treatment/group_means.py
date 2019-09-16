# A function to calculate accession group means

def group_means(numeric):
    
    #defining the column with numerical data type
    #numeric, categorial = classifying_column(dataframe)
    
    #calculate column mean group by accession_group
    mean_values = {}
    
    for trait in numeric :
        group_mean = dataframe.groupby('Accession_group')[trait].mean()
        mean_values[trait] = group_mean
        
    return mean_values
