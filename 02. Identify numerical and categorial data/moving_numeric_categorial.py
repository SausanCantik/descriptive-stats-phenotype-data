#A function to move from numeric to categorial, vice versa

def moving_numeric_categorial(numeric, categorial):
    '''
    In order to run this function, you need to specify these two parameter :
    
    numeric : list of traits with numerical data
    categorial : list of traits with categorial data
    
    if you want to use the column name from the raw data (the excel file), you may use
    this function :
    
    classifying_column(dataframe), which will return the parameters required for moving_numeric_categorial() 
    '''
    
    to_move = input('Which column name to move? : ') #takes only one name at a time
    
    if to_move in numeric :
        numeric.remove(to_move)
        categorial.append(to_move)
        print ('{} has been successfully removed from numeric to categorial' .format(to_move) )
        
        #check if is in categorial dataset
        print ('is {} still exist in numerical data list ? ' .format(to_move) , to_move in numeric)
        print ('is {} already in categorial data list ? ' .format(to_move) , to_move in categorial)
            
    elif to_move in categorial :
        categorial.remove(to_move)
        numeric.append(to_move)
        print ('{} has been successfully removed from categorial to numeric' .format(to_move) )
        
        #check if is in numerical dataset
        print ('is {} still exist in categorial data list ? ' .format(to_move) , to_move in categorial)
        print ('is {} already in numerical data list ? ' .format(to_move) , to_move in numeric)
        
    else :
        print ('Are you sure there is no typo ? The column name is not found in the dataset')
        
    return numeric, categorial
