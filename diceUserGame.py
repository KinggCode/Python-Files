#Author : Eugene Parker
#Tasks : A Simple Dice Roll Simulation

########################################

#Principle Applied
# S - Single Responsibility Principle
# O - Open Closed Priniciple
# L - Liskov Substitution Principle
# I - Interface Segregation Principle
# D - Dependency Inversion Principle

########################################


#Random Library Import
import random as rand

#Creating a Parent Class ----> Person
class Person:
    def __init__(self,firstname,surname,age,gender,nickname):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.gender = gender
        self.nickname = nickname


#Creating a Child Class -----> Users
class Users(Person):
    def __init__(self,firstname,surname,age,gender,nickname,score):
        super().__init__(firstname,surname,age,gender,nickname)
        self.score = score
        
        
    def welcomeMessage(self):
        print("Welcome to CodeHub, ",self.nickname)

    def getName(self):
        return self.firstname
        return self.lastname

    def getAge(self):
        return self.age
        
    def getGender(self):
        return self.gender

    def getNickname(self):
        return self.nickname

    def getScore(self):
        return score


    def throwDice():
        diceValue = Dice.roll()
        return diceValue
        
    
#Creating a Game mod Class ----> Dice
class Dice:
    currentSide = 0
    def __init__(self,side,color,shape):
        self.side = side
        self.color = color
        self.shape = shape
        
    def getSide(self):
        return self.side

    def getColor(self):
        return self.color

    def getShape(self):
        return self.shape

    def roll():
        diceValue = rand.randrange(1,6)
        return diceValue

#Dice object
dice = Dice(6,'black','square')



#Creating Game Simulation Class -----> Game
class Game:
    points = 0
    def __init__(self,points):
        self.points = points

    #Users Object 
    player1 = Users('Eugene','Parker',20,'male','KP',0)
    player2 = Users('Amy',"Hufferman",18,'female','cupcakes',0)
    player3 = Users('Michael','Scoffield',27,'male','runner',0)
    player4 = Users('Steve',"Nelson",29,"male","bolt",0)
    player5 = Users("Merlin","Gary",10,"female","mumbo",0)

    player1Score = 0
    player2Score = 0
    player3Score = 0
    player4Score = 0
    player5Score = 0

    users1Score = 0
    users2Score = 0
    users3Score = 0
    users4Score = 0
    users5Score = 0
    count =0
    
    for i in range(5):
        player1Score = Users.throwDice()
        player2Score = Users.throwDice()
        player3Score = Users.throwDice()
        player4Score = Users.throwDice()
        player5Score = Users.throwDice()
        
        print(player1.nickname,'rolled',player1Score)
        print(player2.nickname,'rolled',player2Score)
        print(player3.nickname,'rolled',player3Score)
        print(player4.nickname,'rolled',player4Score)
        print(player5.nickname,'rolled',player5Score)

        gameScore = [player1Score,player2Score,player3Score,player4Score,player5Score]

        if(max(gameScore) == player1Score):
           print("Hurray!",player1.nickname.upper(),"won this round")
           users1Score = users1Score + 2
        elif(max(gameScore) == player2Score):
           print("Hurray!",player2.nickname.upper(),"won this round")
           users2Score = users2Score + 2
        elif(max(gameScore) == player3Score):
           print("Hurray!",player3.nickname.upper(),"won this round")
           users3Score = users3Score + 2
        elif(max(gameScore) == player4Score):
           print("Hurray!",player4.nickname.upper(),"won this round")
           users4Score = users4Score + 2
        elif(max(gameScore) == player5Score):
           print("Hurray!",player5.nickname.upper(),"won this round")
           users5Score = users5Score + 2
        elif(max(gameScore) == player1Score or max(gameScore) == player2Score or max(gameScore) == player3Score or max(gameScore) == player4Score):
            print("its a tie")
        



        
        count +=1


        if(count == 5):
            print()
            print("######################################################")
            print()
            message = "Game Simulation Over"
            print(message.upper())
            print("{} has {}Points".format(player1.nickname,users1Score))
            print("{} has {}Points".format(player2.nickname,users2Score))
            print("{} has {}Points".format(player3.nickname,users3Score))
            print("{} has {}Points".format(player4.nickname,users4Score))
            print("{} has {}Points".format(player5.nickname,users5Score))
            print()
            print("######################################################")
   
    
    

        

       
        
        
        
        
        
                
        
    
        


        

    
        
