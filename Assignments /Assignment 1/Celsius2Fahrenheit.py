#Arthur : Eugene Parker
#Tasks : Developing a program that converts temperature from Fahrenheit to Celsius.
#Assignment no: 2


#Temperature Converter Program 
def Temperature():
    print("Temperature Hub \n This program converts temperatures from Fahrenheit to Celsius")
    response1 = eval(input("Simulator Run Time: "))     #Program Runtime
    response2=input("Do you want to proceed:  {yes or no}: ")
    if(response2 == "yes" or response2 == "y"):
        firstname = input("Enter firstname: ")          #Firstname input 
        surname = input("Enter surname: ")              #Surname input 
        username = firstname + "." + surname            #Username derived 
        count = 0 
        for i in range(response1):
            count += 1
            if(count == 1):
                print("Welcome,",username.upper())
            user_input = eval(input("Please enter the temperature you prefer in Fahrenheit: "))
            program_formula = 5*(user_input - 32) /9       #Program Formula 
            print("Your temperature in Celsius  is ",program_formula)      #Converted temperature display 
    else:
        print("Thanks for visiting Temperature Hub!")       #exit message 
            

Temperature()
