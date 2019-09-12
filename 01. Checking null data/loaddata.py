# Creating a function to load excel the data

def loaddata(excel_path):
    #import tools
    import numpy as np
    import pandas as pd

    # read the .xlsx file
    dataframe = pd.read_excel(excel_path, sheet_name=1)
    return dataframe

