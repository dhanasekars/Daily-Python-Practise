""" 
Created on : 11/11/22 5:57 AM
@author : ds  
"""


# https://edabit.com/challenge/9Q5nsEy2E2apYHwX8

# Python classes are easy to understand.
# They are almost the same as JavaScript classes, with a different syntax and different constructor function names.
# Constructors define some variables in your class;
# in Python that is def __init__(self). Other functions are defined the same as normal.
# I want you to create a class called programmer. It should have a salary value, work_hours value,
# and a __del__(self) function. __del__(self) should return "oof, " + str(salary) + ", " + str(work_hours)
# when the object is destroyed. salary and work_hours will be in the constructor.
# Variables in a class are defined with self.name = value.
# Also, define a function that will compare two programmers (their salary and work_hours) and return the programmer
# with the lower salary. If their salary is equal, then compare their work_hours, which will always be different

class programmer:
    def __init__(self, salary, work_hours):
        self.salary = salary
        self.work_hours = work_hours

    def __del__(self):
        return "oof, {}, {}".format(self.salary, self.work_hours)

    def compare(self, person):
        if self.salary == person.salary:
            return min(self.work_hours, person.work_hours)
        elif self.salary > person.salary:
            return person.salary
        else:
            return self.salary

    def salary(self):
        return self.salary()

    def work_hours(self):
        return self.work_hours()


prog = programmer(2500, 5)
prog1 = programmer(2500, 6)
print(prog.salary)
print(prog.work_hours)
print(prog.__del__())

print(prog.compare(prog1))


