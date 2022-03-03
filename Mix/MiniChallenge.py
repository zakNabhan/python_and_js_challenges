'''

I want you to create a class called programmer.
It should have a salary value, work_hours value,
 and a __del__(self) function. __del__(self) should return
 oof, " + str(salary) + ", " + str(work_hours) when the object is
 destroyed. salary and work_hours will be in the constructor.
  Variables in a class are defined with self.name = value.
'''


class programmer:
    def __init__(self, sallary, work_hours):
        self.sallary = sallary
        self.work_hours = work_hours

    def __del__(self):
        # code
        return "oof, " + str(self.sallary) + ", " + str(self.work_hours)

    def compare(self, other_programmer):
        if self.sallary == other_programmer.sallary:
            if self.work_hours < other_programmer.work_hours:
                return self
            else:
                return other_programmer
        else:
            if self.sallary < other_programmer.sallary:
                return self
            else:
                return other_programmer

# code


prog = programmer(25000, 5)
prog2 = programmer(402200, 235)

print(prog.sallary)
print(prog.work_hours)
print(prog.compare(prog2))

print(prog.__del__())