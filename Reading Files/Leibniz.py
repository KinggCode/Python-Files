def Leibniz():
    print("Welcome to Leibniz COmputation")
    response1 = input("Do you want to continue: ")
    if(response1 == "yes" or response1 == "y"):
        userInput = eval(input("Please enter the nth term"))
        const = 4
        for n in range(userInput):
            if(n%2 == 0):
                p = const/n - const/n + const/n
                print(p)
                
Leibniz()
