class Employee:
    no_of_leaves=8
keshaw=Employee()
arko=Employee()
arko.name="Arko Ghosh Dastidar"
arko.salary="100k usd per month"
arko.role="Software developer"


keshaw.name="Keshaw Kumar"
keshaw.salary="500k usd per month"
keshaw.role="CEO of company"

print(keshaw.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves=15
print(keshaw.__dict__)
print(Employee.__dict__)