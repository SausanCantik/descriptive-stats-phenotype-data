'''A function to replace null in column with numerical data. NaN
is replaced by the group mean.
'''

def fillna_numerical(numeric, dataframe):
    import numpy as np
    mean_values = group_means(numeric)
    total_group = len(dataframe['Accession_group'].unique())
    
    #looping to all trait
    for trait in  numeric :
        for i in range(total_group) :
            group_index = list(dataframe.groupby(['Accession_group']).groups[i])
            entry = dataframe[[trait]].loc[group_index]
            value = mean_values[trait][i]
            entry.replace(np.nan, value)
            
    return dataframe
