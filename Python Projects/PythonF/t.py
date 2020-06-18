#Name : Eugene Parker
#Tasks: Abstract Calculations
#Scope: Any Numbers Works

#Multiplication Function
def multiplications():
    user_input = eval(input("Please enter a number: "))
    for i in range(1,21):
        mult = user_input * i
        print("{} x {} = {} ".format(user_input,i,mult))
    print("Success!")
#multiplications()
        

def clearEven():
    cl_message = "Gone"
    lst = [2,9,10,20,31,99,39]
    for ce in lst:
        if (ce % 2 == 0):
            print("{} is Even".format(ce))
            lst.remove(ce)
            print("{}".format(cl_message))
            print(lst)

clearEven()
