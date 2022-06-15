"""class person:
    def __init__(self,aname,aage):
        self.name=aname
        self.age=aage
p1=person("keshaw", "56")
print(p1.name)
print(p1.age)"""
import pdb
class Employee:
    def __init__(self,aname,salary_in_usd,role):
        self.name=aname
        self.salary=salary_in_usd
        self.role=role
    def printdetails(self):
        return f"Name of employee is {self.name}, salary of employee is {self.salary} and role is {self.role}."

e1=Employee("Keshaw", "500k", "HR manager")
e2=Employee("Arko ghosh dastidar", "100k", "Software developer")
# print(e1.name)
# print(e2.salary)
print(e1.printdetails())
print(e2.printdetails())