# Creating dictionary that contain index and assosiated column
def indexingcolumn(dataframe) :
    cols = list(dataframe)
    key = []
    value = []
    for i in range (len(cols)):
        key.append(i)
        value.append(cols[i])
    
    col_index = dict(zip(key, value))
    return col_index
