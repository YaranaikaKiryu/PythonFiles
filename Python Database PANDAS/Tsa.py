import pandas as pd

excelfile = pd.read_excel('c:/Users/Castl/OneDrive/Documents/GitHub/PythonFiles/Python Database PANDAS/FreqOfMass.xlsx', engine = 'openpyxl')

excelfile[["MASS 5","MASS 7"]] =  excelfile[["MASS 5", "MASS 7"]].fillna("No Value")
print(excelfile)

