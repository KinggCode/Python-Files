#Arthur: Eugene Parker

def changeY(y1,y2):
    dy = y2 - y1
    return dy

def changeX(x1,x2):
    dx = x2 - x1
    return dx


def slope():
    x1,x2,y1,y2 = eval(input("Please enter coorinates for {x1,x2,y1,y2}: "))
    y = changeY(y1,y2)
    x = changeX(x1,x2)

    m = y / x
    print("Therefore slope is equal to {}".format(m))


