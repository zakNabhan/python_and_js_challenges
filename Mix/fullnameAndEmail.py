

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