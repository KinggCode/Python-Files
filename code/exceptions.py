from math import *
def main():
    print("This program finds the real solutions to a quadratic")

    a,b,c = eval(input("Please enter the coefficients: "))
    discrim = b * b -4 * a * c
    if(dsicrim <0):
        print("The equation has no real root")
    elif(discrim == 0):
        root = -b/(2*a)
        print("There is a double root at",root)
    else:
        discRoot = sqrt(b * b -4 * a * c)
        root1 =(-b + discRoot)/(2/a)
        root1 =(-b + discRoot)/(2/a)
        
