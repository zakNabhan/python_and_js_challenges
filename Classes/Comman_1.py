# The hasattr() function returns True
# if the specified object has the specified attribute, otherwise False.
class Person:
    name = "zakaria"
    age = 34
    country = "gaza"


x = hasattr(Person, 'age')
y = hasattr(Person, "sdm")

print(x, y)

print("__________________________________________")


# The getattr() function returns the value
# of the specified attribute from the specified object.


class Student:
    name = "zakaria"
    age = 34


x = getattr(Student, 'age')
# Use the "default" parameter to write a message when the attribute does not exist:
y = getattr(Student, 'nachname', "attribute not exists")
print(x, y)

print("__________________________________________")


# delattr() function

class Employee:
    name = "zak"
    salary = 3434


delattr(Employee, "name")
print(Employee.salary)

print("__________________________________________")

class Player:
    name = "test"
    age = 34
    country= "Germany"

setattr(Person, 'age', 40)

print(Player.age)











print("__________________________________________")

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
print("__________________________________________")


import  sys

condi = 4

if condi < 5:
    sys.exit("condition muss be > 5")
else:
    print("continue")

print(sys)


target_int = input("")

