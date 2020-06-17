#Author : Eugene Parker
#Task :Dice Game

#Random Library Import
import random as r

#------> Parent Class
class Person:
    def __init__(self,fname,lname,age,nickname,myTurn):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.nickname = nickname
        self.myTurn = myTurn

    def welcomemessage(self):
        print("Welcome to CodeHub, ",self.fname)

    def throwdice(self,Dice,setMyturn):
        Myturn = setMyturn()
        diceValue = Dice.roll()
        return diceValue
    
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
        
#----> Dice Class
class Dice:
    currentSide = 0
    def __init__(self,side,color,shape):
        self.side = side;
        self.color = color;
        self.shape = shape;

    def roll(self):
        currentSide= r.randint(1,self.side)
        return currentSide
    
    def getColor(self):
        color = self.color
        return color

        
x = Dice(6,'black','square')
print(x.getColor())



#-----> Game App Class
class Game:
    def __init__(self,points):
        self.points = points
        
player1 = Person("Eugene","Parker",22,"KP")
player2 = Person("Tony","Jones",20,"runner")
player3 = Person("Allisia","Coleman",22,"coolaid")

player1.getAge()

        
            
            
            
        
        
