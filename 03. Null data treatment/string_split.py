'''
Creating A function to group the sample based on the accession

split the sample name based on '-' and store it into variable called 'accession_group'
'''

def string_split (dataframe_column) :
    accession_group = []
    for word in dataframe_column : 
        split = word.split('-')
        accession_group.append(split[0])
        
    return accession_group
