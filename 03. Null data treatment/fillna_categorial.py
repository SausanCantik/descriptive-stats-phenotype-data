'''
#B. replace null data with the mode value of each column with categorical data
'''

def fillna_categorial(categorial, dataframe):
    mode_value = []
    
    for i in range(len(categorial)):
        mode = int(dataframe[categorial[i]].mode())
        mode_value.append(mode)
        
    replacement = dict(zip(categorial, mode_value))
    dataframe = dataframe.fillna(value=replacement)
    
    return dataframe
