#Person ----> Class
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    #Printname ----> Method
    def printname(self):
        print(self.fname,self.lname)

#Username ----> Object
username = Person("Eugene","Parker")


#ChildClass
class Student(Person):
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname 
       

p1 = Student("melo","kilo")
print(p1.fname)
