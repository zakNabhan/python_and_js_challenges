'''

The Python interpreter has a number of functions and
 types built into it that are always available
 They are listed here in alphabetical order.

'''

# 1
'''
abs() Parameters
abs() method takes a single argument:

num - a number whose absolute value is to be returned. The number can be:
integer
floating number
complex number
'''

integer = -4545
print("Absolute value of -20 is: ", abs(integer))

'''
The dict() constructor creates a dictionary in Python.
'''

# we have different forms of dict() constructors are:
'''
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
'''

creditenls = dict(username="nabhan", password='3sdk34944')
cre = dict(username="zakaeria", howmanlogin="22")
creditenls.update(cre)

print(creditenls)

worte = {"house": "Haus", "cat": "Katze", "black": "Schwarz"}

print(worte['cat'])

gerichte = ["Pizza", "Sauerkraut", "Paella", "Hamburger"]
laender = ["Italien", "Deutschland", "Spanien", "USA"]
land_gericht_dict = zip(laender, gerichte)

for x in land_gericht_dict:
    print(x)

# convert to dict

land_gericht = dict(land_gericht_dict)
for x in land_gericht:
    print(x)
print(land_gericht)

print("_______________________________________________")
mydcit = {200: 'ok', 404: 'Not Found', 502: 'Bad Gateway'}
print(mydcit)

# datenzugriff
# einzelnes Item
print(mydcit[200])

# mehrere Items
items = [200, 502]
values = [mydcit[i] for i in items]
print(values)

# --- Wertzuweisung
myDict = {200: 'OK', 404: 'Not Found', 502: 'Bad Gateway'}

myDict[200] = '__OK__'
print(myDict)
{200: '__OK__', 404: 'Not Found', 502: 'Bad Gateway'}

item = {200: "__NOT OK__"}
myDict.update(item)
print(myDict)
{200: '__NOT OK__', 404: 'Not Found', 502: 'Bad Gateway'}

# --- Keyzuweisung
myDict[2000] = myDict.pop(200)
print(myDict)
{2000: '__NOT OK__', 404: 'Not Found', 502: 'Bad Gateway'}

print("_______________________________________________")

dictklassse = dict(A=1, B=2, C=3)
print(dictklassse)

dict_numbers = dict([(1, '111'), (2, '222'), (3, '333',), ])

print(dict_numbers)

code = [1, 2, 3, 4, 5]
item = ['sehr gut', 'gut', 'befriedigen', 'ausreichend', 'mangelhaft']

zipped = zip(code, item)
print(dict(zipped))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

# DICTIONARIES IM SPEICHER

import sys

myDict = {}

print(id(myDict))  # Physikalischer Speicherort von myDict
print(sys.getsizeof(myDict))  # größe von myDict

myDict2 = {200: 'OK', 404: 'Not Found', 502: 'Bad Gateway', 403: 'Forbidden',
           500: 'Internal Server Error', 0000: 'not exists'}
myDict.update(myDict2)
print(id(myDict))
print(sys.getsizeof(myDict))

# --- Summiere die Größe aller im Dictionary enthaltenen Werte
total_size_values = 0
for x, y in myDict.items():
    total_size_values += sys.getsizeof(y)

print("Total size: ", total_size_values)
