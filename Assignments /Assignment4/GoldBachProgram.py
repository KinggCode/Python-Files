#Importing GoldBach Module ...
import GoldBachMod as mod


def GoldBach():
    user_input = eval(input("Please enter a number: "))
    if(mod.evenNumbers(user_input)== 1):
       return 1
    else:
        return 0 

print(GoldBach())
