#Name : Eugene Parker
#Tasks : Conditional Statement Assignment


user_input = eval(input("Please enter a number: "))

for i in range(user_input):
    if( i % 10 == 0):
        continue
    elif(i >= 100):
        break
    print(i)
