#Author : Eugene Parker
#Task :Dice Game

#Random Library Import
import random as r

#------> Parent Class
class Person:
    def __init__(self,fname,lname,age,nickname):
        myTurn = "false"
        self.fname = fname
        self.lname = lname
        self.age = age
        self.nickname = nickname
        self.myTurn = myTurn
        self.diceroll = Dice.roll()

    def welcomemessage(self):
        print("Welcome to CodeHub, ",self.fname)

    def getFirstname(self):
        return fname

    def getLastname(self):
        return lname

    def getAge(self):
        age = self.age
        return age

    def getNickname(self):
        nickname = self.nickname
        return nickname

    def setMyturn(self):
        myTurn = self.myTurn
        return myTurn

    def throwdice(self):
        Myturn = self.myTurn
        diceValue = self.diceroll
        return diceValue
        
#----> Dice Class
class Dice:
    currentSide = 0
    def __init__(self,side,color,shape):
        self.side = side;
        self.color = color;
        self.shape = shape;

    def roll():
        currentSide= r.randint(1,6)
        return currentSide
    
    def getColor(self):
        color = self.color
        return color


            
user1 = Person("Eugene","Parker",20,"kp")
print(user1.throwdice())
        
