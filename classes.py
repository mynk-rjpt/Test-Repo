# class students() :
#     def printdetails(self):
#         print(self.name)
# mayank = students()
# akash = students ()
# mayank.name = "Mayank"
# mayank.std = 1
# print(mayank,akash)
# print(mayank.__dict__)
# mayank.printdetails()
# It means these two are the objects for students class at different locations
# These both objects are the instanaces of the students class.

# Now using init function(constructor)

class Employee :
    def __init__(self, xname, xsalary, xage):
        self.name = xname
        self.salary = xsalary
        self.age = xage

mayank = Employee("Mayank", 250, 24)
harry = Employee("Harry", 200, 25)
print(mayank.salary)
print(harry.name)
