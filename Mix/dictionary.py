

import requests

url = "http://apifahrtservices.pythonanywhere.com/api/fahrten/"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

#num1 = int(input("Bitt geben sie first number ein!"))
#num2 = int(input("bitte geben Sie the second number ein!"))
num1=20
num2=30
def multi_or_sum(num1, num2):
    product = num1 * num2

    if (product <= 1000):
        return product
    else:
        return num1+num2
print("result: ", multi_or_sum(num1, num2))

'''
Frage 2: Bei einem Bereich der ersten 10 Zahlen von der
 Startnummer bis zur Endnummer iterieren und 
 die Summe aus der aktuellen Nummer und der vorherigen Nummer drucken

'''

#num= int(input("Drucken der aktuellen und vorherigen Nummernsumme in einem bestimmten Bereich (10)"))
num=10
summe =0
vorherige=0
for x in range(num):
    summe = vorherige+x
    print("aktuelle nummer", x, " vorherige N", vorherige, " Summe", summe)
    vorherige=x


'''
dictionary exercise 1: Below are the two lists convert it into the dictionary
'''
keys = ['ten', 'twenty', 'thirty']
values = [10, 20 ,30]
sampleDict =dict(zip(keys, values))
print(sampleDict)

#two list
keys = ['vorname', 'nachname', 'alter']
values = ['zakaria', 'nabhan', '25']
#convert to dictionary
convert_into_dict = dict(zip(keys, values))
print(convert_into_dict)
# print all keys and values
for key, value in convert_into_dict.items():
    print(key, " : ", value)


'''
dictionary exercise 2: Merge following two Python dictionaries into one

'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict_merge = {**dict1,  **dict2}
# for other version
dict_merge_2 = dict1.copy()
dict_merge_2.update(dict2)
print('other merge' ,dict_merge_2)


'''
dictionary exercise 3: Access the value of key ‘history’
'''
sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}
print(sampleDict['class']['student']['marks']['history'])


'''
dictionary exercise 4: Initialize dictionary with default values

'''
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

resDict = dict.fromkeys(employees, defaults)
# Individual data
print(resDict['Kelly'])



'''
dictionary exercise 5: Create a new 
dictionary by extracting the following keys from a given dictionary
Keys to extract:
keys = ["name", "salary"]

'''

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}

keys = ["name", "salary"]
newdict = {k: sampleDict[k] for k in keys}
print(newdict)

'''
dictionary exercise 6: Delete set of keys from Python Dictionary

'''

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keysToRemove = ["name", "salary"]

sampleDict = {k: sampleDict[k] for k in sampleDict.keys() - keysToRemove}
print(sampleDict)



'''
Create the instance attributes fullname and email in the Employee class. 
Given a person's first and last names:

Form the fullname by simply joining the first and last name together, separated by a space.
Form the email by joining the first and last name together with a . in between,
and follow it with @company.com at the end. Make sure the entire email is in lowercase.
'''

class Employye:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = self.firstname + " " + self.lastname
        self.email = self.firstname + "_" + self.lastname +"@company.com"

    def getfullname(self):
        return self.firstname + " " + self.lastname
    # other solution to create email for a employee
    def create_eamil(self):
        return self.firstname + "_" + self.lastname + "@company.com"


emp_1 = Employye("John", "Smith")
print("fullname: ", emp_1.fullname)
print("email: ", emp_1.email)

employee = Employye('zakaria', "nabhan")
print(employee.getfullname())
print(employee.create_eamil())

'''
Create a method in the Person 
class which returns how another person's age compares.
 Given the objects p1, p2 and p3, which will 
 be initialised with the attributes name and age,
 return a sentence in the following format:
'''

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def compare_age(self, other):
         if other.age > self.age:
             return other.name +" is oder than me"
         elif other.age < self.age:
             return  other.name + "is younger than me"
         else:
             return "{} is the same age".format(other.name)

p1 = Person("Samuel", 36)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)
print(p1.compare_age(p2))


'''
Your task is to create a Circle constructor
that creates a circle with a radius provided by an argument. 
The circles constructed must have two getters getArea() (PIr^2) and
 getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).
'''
from math import pi

class Circle:
    def __init__(self, radius = 0):
        self.radius=radius

    def getArea(self):
        return 'ergebnis: {}'.format(pi*self.radius**2)

    def getPerimeter(self):
        return "Ergebnis: {}".format(2*pi*self.radius*2)


circy = Circle(11)
print(circy.getArea())

circy = Circle(4.44)
print(circy.getPerimeter())




