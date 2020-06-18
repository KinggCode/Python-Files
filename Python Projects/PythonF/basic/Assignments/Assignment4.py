#Name: Eugene Parker
#Tasks : Grading Applications

maths,physics,chemistry = eval(input("Enter your grades for Maths,Physics,Chemistry according: "))
if(maths < 35 or  physics < 35 or chemistry < 35):
    print("You have failed the exams")
elif(maths >= 35 and physics >= 35 and chemistry >= 35):
    print("You have passed the exams")
    averagegrade = (maths + physics + chemistry)/3
    if(averagegrade <= 59):
        print("You got a C")
    elif(averagegrade <= 69):
        print("You got a B")
    elif(averagegrade > 69):
        print("You got an A")

    
