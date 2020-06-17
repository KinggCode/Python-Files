import random as r
class Person:
    def __init__(self,fullname,age,nickname):
        self.fullname = fullname
        self.age = age
        self.nickname = nickname

    def myfunc(self):
        print("Hello my name is",self.fullname)

p1 = Person("Eugene Parker",22,"KP")
p2 = Person("Narnia Hull",20,"coolaid")
p3 = Person("Paul Max",30,"haywire")


        
class Dice:
    def __init__(self,num):
        self.num = num
        

    def dicerandom(self):
        diceroll = r.randrange(int(num[1]),len(self.num))

roll1 = Dice(dice)
print(roll1)
        

    
