#Arthur: Eugene Parker
#Tasks : A simple calculator to produce the distance between two lines
#Assignment no : 4

#Imported Library
from math import * 

#Program Function
def LinearEquation():
    print("Welcome to Cal Comoutation \n This simulator helps you find the slope of a line , the y-intercept")
    response1 = eval(input("Simulator Run time: "))     #Runtime inputted by the user 
    for k in range(response1):
        x1 = eval(input("Enter point x1: "))        #x-coordinate point 1 
        x2 = eval(input("Enter point x2: "))        #x-coordinate point 2 
        y1 = eval(input("Enter point y1: "))        #y-coordinate point 1
        y2 = eval(input("Enter point y2: "))        #y-coordinate point 2 


        deltaX = (x2 - x1 ) #Change in x 
        deltaY = (y2 -y1)   #Change in y 

        gradient = deltaY / deltaX      #gradient formula 
        print("The gradient of the line is {}".format(gradient))            #Gradient display 
        coefficient = (gradient * x1) - y1
        print("The coefficient of the line is {}".format(coefficient))      #Coeffocient derived 
        print("The equation of the line is Y= {}x + {}".format(gradient,coefficient))   #Linear epression display 
            
LinearEquation()
        
        
        
    
