'''
A function to show categorial crosstab : trait | category | frequency
'''

import numpy as np
import pandas as pd
def categorial_crosstab():
    #defining the trait with categorial data
    numeric, categorial = classifying_column(dataframe)
    
    #replacing NaN with mode value
    df = fillna_categorial(categorial, dataframe)
    
    #creating the containers for the dictionary
    trait = []
    category = []
    frequency = []
           
    for i in range(len(categorial)) :
        trait_i = categorial[i]
        frequency_i = list(df[trait_i].value_counts(sort = False))
        category_i = list(df[trait_i].unique())
    
        #Update the containers
        trait.append(trait_i)
        frequency.append(frequency_i)
        category.append(category_i)
        
    #create dictionary with trait as key and category and frequency as values
    d = {'Trait' : trait, 'Category' : category, 'Freq' : frequency}
    
    #create DataFrame from the dictionary
    crosstab = pd.DataFrame(d)
            
    return crosstab
