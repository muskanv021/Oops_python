class employee:
    def __init__(self,name, age):
        self.name= name
        self.age= age
    def display(self):
        print(self.name,self.age)
    def change_date(self):
        self.name='mukku'
        self.age=20
e1= employee("John", 21)
e2= employee("Doe", 22)
e3= employee("Muskan", 23)
#outside the class
e1.avg=21 #add one more parameter 
print(e1.__dict__)
print(e2.__dict__)
e1.name ='mukku'
print(e1.__dict__)
e1.change_date()
e1.display()