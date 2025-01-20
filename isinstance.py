class demo:
    pass
class employee:
    def __init__(self,name, age):
        self.name= name
        self.age= age
    def display(self):
        print(f"Name is {self.name} and age is {self.age}")
e1= employee("John", 21)
e2= employee("Doe", 22)

print(isinstance(e1,employee))
print(isinstance(e2,demo)) 