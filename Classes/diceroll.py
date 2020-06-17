import random as r
def dice():
    dice =[1,2,3,4,5,6]
    no_of_users = eval(input("Number of users: "))
    for i in range(no_of_users):
        username = input("Please enter your name: ")
        print("Please roll a dice!!")
        user_input = input("Reply by typing 'yes' or 'y':  ")
        if(user_input == "yes" or user_input == user_input[0]):
            dice_roll = r.randrange(1,len(dice))
            print("You selected ",dice_roll)
        else:
            
    
dice()
