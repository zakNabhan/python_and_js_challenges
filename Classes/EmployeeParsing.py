'''
Employee Parsing
In the class Employee, implement the instance attributes as firstname,
 lastname and salary.

Create the method from_string() which parses a string containing
these attributes and assigns them to the correct properties.
Properties will be separated by a dash.
'''


class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = int(salary)

    def from_string(data):
        firstname, lastname, salary = data.split(',')
        return Employee(firstname, lastname, salary)


emp1 = Employee("Mary", "Sue", 600000)

print(emp1.firstname)
emp2 = Employee.from_string("John,Smith,55000")

print(emp2.salary)
# other version

'''
class Employee:
	def __init__(n,f,l,s):
		n.firstname=f
		n.lastname=l
		n.salary=s
	@classmethod
	def from_string(c,a):
		f,l,s=a.split('-') 
		return c(f,l,int(s))
'''

class Student:
    def __init__(self, l, f, s):
        self.l= l
        self.f = f
        self.s= s

    @staticmethod
    def from_string(txt):
        l, f, s = txt.split(' ')
        return Student(l, f, int(s))

emp2 = Student.from_string("John Smith 55000")

print(emp2.f)

