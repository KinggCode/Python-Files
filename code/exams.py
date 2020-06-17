#exams question

#i.Let the user enter a string "University" and output should be "Un(I)v(e)rs(i)ty"


def vowelCheck():
    print("This program provides vowel concatenation ")
    try:
        inputs = input("Enter a string: ")
        vowels = ["a","i","e","o","u"]
        for i in inputs:
            if(i in vowels):
                word = inputs.replace(i,"("+i+")")
                print(word)
    except("Syntax Error"):
        print("Please type a valid string")

#vowelCheck()



#ii. Let the user enter a string "University" and output should be "nvrty"


def wordCheck():
    print("This program provides vowel strip")
    try:
        word = []
        inputs = input("Enter a string: ")
        vowels = ["a","e","i","o","u"]
        for i in range(len(inputs)):
            for i in inputs:
                if(i in vowels):
                    inputs = inputs.split(i)
        print(word)
    except("Syntax Error"):
        print("Please type a valid string")


def wordCipher():
    print("This program provides vowel strip")
    try:
        inputs = input("Enter a string: ")
        for i in range(len(inputs),0,-1):
            print(inputs[i], end="")

    except("Syntax Error"):
        print("Please type a valid string")
    

wordCipher()

wordCheck()          
    
            
