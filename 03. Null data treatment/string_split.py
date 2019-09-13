'''
Creating A function to group the sample based on the accession

split the sample name based on '-' and store it into variable called 'accession_group'
'''

def string_split (dataframe) :
    column_name = list(dataframe)
    sample_ID = column_name[0]
    accession_group = []
    for word in dataframe[sample_ID] : 
        split = word.split('-')
        accession_group.append(split[0])
        
    return accession_group
