class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
e1= Employee("John", 21)
e2= Employee("Doe", 22)

print(Employee.__dict__)
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)