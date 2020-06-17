class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname)


user1 = Person("Eugene","Parker")
user1.printname()

class Student(Person):
    def __init__(self,firstname,lastname,year):
        super().__init__(firstname,lastname)
        self.year = year
        
    def getgradValue(self):
        print(self.year)

    def welcomeMessage(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.year)


        
student1 = Student('Bladd','Fox',2019)
student1.printname()
student1.getgradValue()

