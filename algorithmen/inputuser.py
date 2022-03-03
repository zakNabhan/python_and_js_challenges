
# pyhon 3.6 input()
# python 2.7 raw_input()

# to get the functions of python in console
# first step python eingeben
#second step dir()
#third step dir("")

name =input("Was ist deine Name ? :")
if len(name)< 2:
    print ("zu kurz")
elif name.isalpha():
    age = input("bitte geben Sie Alter ein: ")
    if age.isalpha():
        print("bitte zahl eingeben!!")
    elif age.isdigit():
        if int(age)< 18:
            klasse = input("Bitte geben Sie die KLasse ein:")
            if "abitur" in klasse:
                note = input("bitt geben Sie die note:")
                if float(note)<=1:
                    print("Studienangebote:\n")
                    print("Medizin","Jura")
                if int(note)>4:
                    print("Schade")
                else:
                    print("Sie alles machen")


elif name.isdigit():
    print("bitte keine Zahlen eingeben")
else:
    # convert the first charater to uppercas cpitalize
    #    # or with casefold to lowercase
    x = name.capitalize()

    # center value string.center(length, charater)
    y= name.center(30)
    # 30 is the space " "

    print(x)
    print (y)






"""

# ASCII code

print(ord("A"))# with this we read A in ascii and the output 65
print(chr(76))
print(chr(65))
print (ord("C"))
print(ord("S"))
print(chr(5))

#Indentation
def function():
    pass

for each in "zakaria":
    pass

# Single assignment

city="London"
money =100.3
count = 323
print(city, money, count)

#multiple assignment
a= b=c= 1
print(c, b , a)

'''
Data types in python
'''
# numbers, string, tuples, list , Dictionary
x = 4
y = 5
if x > y:
    print(x)
elif y < x or  y> x :
    print (y)

# identity operators
x= 34
y=3434
print (id(y))

str1="zakaria"
print(id(str1))
print(str1[0]) # print first letter
print(len(str1)) # print the length

"""
