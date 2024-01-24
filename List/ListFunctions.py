years = [1987, 1945, 1966, 1977, 1900]
Date = ["December", "November", "October","October", "September"]

""" years.extend(Date) #Adds the 2 list together
print(years)
 """
Date.append("January") #Appends 
print(Date)

Date.insert(1, "Febuary") #Inserts in a specific index
print(Date)

""" Date.remove("November") #Removes a specific element on a list
print(Date)
 """
""" years.clear() #clears everything
print(years)
 """
years.pop() #rEMOVES THE LAST ELEMENTS FROM THE LIST
print(years)

print(Date.index("November")) #tells the location of the said string

print(Date.count("October")) #counts the numbers of duplicate

years.sort() #sorts 
print(years)

Dates2 = Date.copy()
print(Dates2)