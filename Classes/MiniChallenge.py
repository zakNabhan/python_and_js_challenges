'''

I want you to create a class called programmer.
It should have a salary value, work_hours value,
 and a __del__(self) function. __del__(self) should return "oof, " + str(salary) + ", " + str(work_hours) when the object is destroyed. salary and work_hours will be in the constructor. Variables in a class are defined with self.name = value.

Also, define a function that will compare two programmers
(their salary and work_hours) and return the programmer with the lower salary. If their salary is equal, then compare their work_hours, which will always be different.

This is not really a challenge, just an introduction to Python classes.
'''

class Programmer:
	def __init__ (self,sallary,work_hours):
		self.sallary=sallary
		self.work_hours=work_hours
	def __del__ (self):
		return "oof, {}, {}".format(self.sallary,self.work_hours)
	def compare (self,other):
		if self.sallary<other.sallary:
			return self
		elif self.sallary>other.sallary:
			return other
		elif self.work_hours<other.work_hours:
			return self
		else:
			return other


prog = Programmer(25000, 5)

print(prog.sallary)
