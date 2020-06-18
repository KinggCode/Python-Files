class Person:
    def __init__(self,fname,lname,age,height,weight):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.height = height
        self.weight = weight

    def getFullname(self):
        return self.fname + " " + self.lname

    def getLname(self):
        return self.lname

    def getAge(self):
        return self.age + ""+ "yrs"

    def getHeight(self):
        return self.height + " " +"cm"

    def getWeight(self):
        return self.weight +" "+"kg"


class User(Person):
    def __init__(self,fname,lname):
        Person.__init__(fname,lname)

    def userName(self):
        return self.fname +"."+self.lname
    

#user = Person("Eugene","Parker","22","169","95")
#print(user.getFullname())

user1 = User("Eugene","Parker")
print(user1.userName())
