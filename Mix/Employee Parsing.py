'''

In the class Employee, implement the instance attributes
as firstname, lastname and salary.

Create the method from_string() which parses a string
containing these attributes and assigns them to the correct
 properties.
Properties will be separated by a dash.
'''


class Employee:

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_string(cls, info):
        firstname, lastname, salary = info.split("-")
        return cls(firstname, lastname, int(salary))

    '''
    other versiob
    '''

    def from_string(info):
        firstname, lastname, salary = (info).split('-')
        return Employee(firstname, lastname, salary)

    '''
    other version
    '''

    @classmethod
    def from_string(cls, employee_data):
        data = employee_data.split("-")
        return Employee(data[0], data[1], int(data[2]))


emp1 = Employee("Mary", "Sue", 60000)

emp2 = Employee.from_string("John-Smith-55000")

print(emp2.firstname)
print(emp2.lastname)
print(emp2.salary)

