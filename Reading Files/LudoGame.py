#Author : Eugene Parker
#Tasks  : Ludo Game


#Importing the random library
import random as ran
class Person:
    def __init__(self,firstname,surname,age,gender):
        self.__firstname = firstname
        self.__surname = surname
        self.__age = age
        self.__gender = gender

    def getFirstName(self):
        return self.__firstname

    def getSurname(self):
        return self.__surname

    def getAge(self):
        return self.__age

    def getGender(self):
        return self.__gender

class Users(Person):
    def __init__(firstname,surname,age,gender,points,lead):
        super.__init__(firstname,surname,age,gender)

        self.__points = points
        self.__lead = lead


#Users Object
player1 = Users("Eugene","Parker",22,0,0)
print(player1.firtname)

class Dice:
    def __init__(self,color,shape):
        currentSide = 0 
        self.__color = color
        self.__shape = shape
        

    def getRoll(self):
        currentSide = ran.randint(1,6)
        return currenSide

    def getColor(self):
        return self.__color

    def getShape(self):
        return self.__shape

#Dice Objects
dice = Dice("Red","Box")
print(dice)
        
        
