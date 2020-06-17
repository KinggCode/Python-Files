#Arthur: Eugene Parker

from math import sqrt
def square(x):
    a = x ** 2
    return a

def diffX(x1,x2):
    x = x2 - x1
    return x

def diffY(y1,y2):
    y = y2 - y1
    return y

def distance():
    x1 = 2
    x2 = 4
    y1 = 5
    y2 = 9

    d = sqrt(square(diffX(x1,x2)) + square(diffY(y1,y2)))
    print(d)
