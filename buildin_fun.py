class Employee():
    def __init__(self,name, age):
        self.name= name
        self.age= age
    

e1= Employee("John", 21)
e2= Employee("Doe", 22)

print(getattr(e2,'name'))
print(setattr(e2,'name','Muskan'))
print(delattr(e1,'name'))
        
print(e1.__dict__)
print(e2.__dict__)