
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

