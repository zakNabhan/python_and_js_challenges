'''

Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords. Each instance should have a name and a lastname attributes
plus one more attribute for each of the keywords, if any.
'''


class Student:
    def __init__(self, fullname, **kwargs):
        self.name = fullname.split(" ")[0]
        self.lastname = fullname.split(" ")[1]

        for k, v in kwargs.items():
            setattr(self, k, v)


zak = Student("Jon Done")
print(zak.lastname)




class Employee:
    def __init__(self, fullname, **kwargs):
        self.name, self.lastname = fullname.split()
        self.__dict__.update(kwargs)



john = Employee("Jon Done")

print(john.name)


'''
class Employee:

    def __init__(self, str_names, **kwargs):
        _name, _lastname = str_names.split()
        self.name = _name
        self.lastname = _lastname
        for key, val in kwargs.items():
            setattr(self, key, val)


'''