import pandas as pd

divider = '----------------------------------------'

exelfile = pd.read_excel('c:/Users/Castl/OneDrive/Documents/GitHub/PythonFiles/Python Database PANDAS/FreqOfMass.xlsx', engine = 'openpyxl')

dataset = {
    "cars":["Toyota", "Mitsubishi", "Ferrari"],
    "year":["2023","2011","1987"],
    "model": [2.1, 2.2 , 2.3]
}

datasetforseries = {
    
    "day1": 23,
    "day2": 89,
    "day3": 79,
    "day4": 90,
    "day5": 100
    
}

datawithnonameindex = [1,2,3,4,5,6,7,8,9,10]

#SERIES WITH INDEX
indexedset = ["Mark", 23, "Male"]
myanothersetofseries = pd.Series(indexedset, index=["Name", "Age", "Gender"])
print(myanothersetofseries)

#DATAFRAME
print(divider)
mynewdataset = pd.DataFrame(dataset)
print(mynewdataset)
print(divider)


print(divider)
#SERIES WITH NO NAMED INDEX
mydataseries = pd.Series(datawithnonameindex)
print(mydataseries)

print(divider)

#Tail() method
ExcelpyTail = exelfile.tail(n=5)
print(ExcelpyTail)

print(divider)
#Head() method
ExcelpyHead = exelfile.head(n=5)
print(ExcelpyHead)
print(divider)

#Info Method
print(exelfile.info())
print(divider)

#DATA CLEANING
#DROPNA
dropnafunc = exelfile.dropna()
print(dropnafunc.to_string())
print(divider)


#FILLNA
""" exelfile.fillna("AKO AY MAY LAMAN NA", inplace=True)
print(exelfile.to_string()) """

print(divider)

#REPLACING USING MEAN, MEDIAN, MODE

x = exelfile["MASS 5"].mode() #.median() .mode()
exelfile["MASS 5"] = exelfile["MASS 5"].fillna(x)
print(exelfile)

