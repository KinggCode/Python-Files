def menu():
    menu ={
    "menu1":{
        "meal1":"Burgers",
        "price":"23.0"
        },
    "menu2":{
        "meal2":"Pizza",
        "price":"45.00"
        },
    "menu3":{
        "meal3":"fried rice",
        "price":"30.9"
        }
    }

    print("Menu Display")
    for meal in menu:
        print("{} : {} ".format(meal,menu[meal]))



def restaurant():
    print("Welcome to the Double Rush!!")
    user_amount = float(input("How much do you have: "))
    menu()
    response1 = input("What do you want to have: ")
    multiple_entry = response1.split(",")
    print(multiple_entry)
  
    
        

restaurant()
