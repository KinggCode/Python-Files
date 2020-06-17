#Arthur : Eugene Parker
#Tasks : KiloMile is  a program that converts distances in kilometers to miles 


def Temperature():
    print("KiloMile \n This program converts distances measured in kilometers to miles")
    response1 = eval(input("Simulator Run Time: "))             #Program Runtime 
    response2=input("Do you want to proceed:  {yes or no}: ")
    if(response2 == "yes" or response2 == "y"):
        firstname = input("Enter firstname: ")              #User firstname 
        surname = input("Enter surname: ")                  #User Surname 
        username = firstname + "." + surname                #Username derived 
        count = 0 
        for i in range(response1):
            count += 1
            if(count == 1):
                print("Welcome,",username.upper())
            prog_ques1 = eval(input("Please enter the distance in kilometers: "))
            program_formula = prog_ques1 * 0.62137          #Program Formula 
            print("Your distance in miles is ",round(program_formula))
    else:
        print("Thanks for visiting Temperature Hub!")           #Exit message 
        

Temperature()
