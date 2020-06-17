#Eugene Parker
#Assignment 3
#Source : Programming for Cs by  John Zella


def examGradingSystem():
    print("Welcome to Grades Square")
    user_response = eval(input("Program runtime: "))
    for i in range(user_response):
        user_response1 = eval(input("Enter exams score: "))
        grade = ""
        if(user_response1 >=90 and user_response1 <=100):
            print("You got an A")
        elif(user_response1 >=80 and user_response1 <= 89):
            print("You got a B")
        elif(user_response1 >=70 and user_response1 <= 79):
            print("You got a C")
        elif(user_response1 >=60 and user_response1 <= 69):
            print("You got a D")
        else:
            print("You failed")

#examGradingSystem()



def messageCount():
    user_response = input("Enter message here: ")
    word_filter = user_response.split()
    word_count = len(word_filter)
    print("Number of words: {}".format(word_count))

    
messageCount()
    
