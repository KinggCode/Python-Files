#Arthur : Eugene Parker
#Tasks : A simple annual percentage rate simulator
#Assignment no : 1 

#Compounded Annual Interest Rate Function 
def aprSimulator():
    quarter = 3
    print("Welcome to Invest Inc.  \n This simulator helps you forecast deposits earnings \n it uses a compounding formula on quarterly basis.")
    response1 = eval(input("Simulator Run Time: "))         #Runtime response 
    for i in range(response1):
        principalValue = eval(input("Enter principal amount: "))    #Principal Value 
        prin = principalValue
        annualrate = eval(input("Enter annual rate without %:  "))/100      #Annual Rate Value       
        noOfYears = eval(input("Number of years: "))
        periods =eval(input("Number of periods: "))
        for period in range(noOfYears):
            principalValue = principalValue *(1 + (annualrate/noOfYears))**(noOfYears*periods)                    #Program Formula 
            print("Year {} : {}".format(period,principalValue))     
            interestValue = principalValue - prin                            #Interest Value derived  
        print()
        print()
        print("Program Analysis")
        print("Initial Deposit: {} cedis".format(prin))                 #Intial Deposit displayed
        print("Number of periods: {}".format(periods))             #number of periods
        print("Total Amount Earned: {} cedis".format(principalValue))   #Total Principal Value earned 
        print("Interest generated: {}  cedis".format(interestValue))    #Tota interest generated 

aprSimulator()

        
