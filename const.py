class Employee:
    def __init__(self,sal,avg):
        self.salary=sal
        self.age=avg
    def display(self):
        print(f"slaray is {self.salary} and age is {self.age}")
e1=Employee(2000,21)
e2=Employee(26000,26)


print(e1.salary) #Accecing attribute
print(e1.display()) #Accessing method
e1.salary=34000 #updati
print(e1.salary) #Accecing attribute