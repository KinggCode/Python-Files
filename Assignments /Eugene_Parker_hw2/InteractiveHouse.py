 #EugeneParker
#Assignment2
#Source:Python Programming Book - John Zelle
#Chapter 4 (Objects & Graphics)

#Importing graphics & Math library
from graphics import *
from math import sqrt

def House():
    houseWin = GraphWin("House Construction",600,500)
    houseWin.setCoords(0.0,0.0,10.0,10.0)


    #Application Message
    title = Text(Point(5,9)," W E L C O M E   TO   H O U S E   C O N S T R U C T I O N")
    title.draw(houseWin)

    # House Container
    lower_coords = houseWin.getMouse()
    lower_corner = Text(lower_coords,"a")
    lower_corner.draw(houseWin)


    upper_coords = houseWin.getMouse()
    upper_corner = Text(upper_coords,"b")
    upper_corner.draw(houseWin)

    room = Rectangle(lower_coords,upper_coords)
    room.setFill("gray")
    room.draw(houseWin)

    x1 = lower_coords.getX()
    y1 = lower_coords.getY()
    x2 = upper_coords.getX()
    y2 = upper_coords.getY()

    #House Width 
    house_width = sqrt(((x1-x2)**2) + ((y1-y2)**2))
    door_width = (1/5)*house_width
    dmidpoint = door_width/2

    clicked_center = houseWin.getMouse()
    clicked_label = Text(clicked_center,"x")
    clicked_label.draw(houseWin)

    #Door Positive Coordinates
    dupperX = clicked_center.getX() + dmidpoint
    dupperY = clicked_center.getY()
    dupper_label = Text(Point(dupperX,dupperY),"o")
    dupper_label.draw(houseWin)

    #Door Negative Coordinates
    dupper_X = clicked_center.getX() - dmidpoint
    dupper_Y = clicked_center.getY()

    dupper_label = Text(Point(dupper_X,dupper_Y),"o")
    dupper_label.draw(houseWin)

    #Door Frame 
    door = Rectangle(Point(dupper_X,lower_coords.getY()),Point(dupperX,dupperY))
    door.setFill("white")
    door.setOutline('red')
    door.draw(houseWin)

    #Window Width
    window_width = (1/2) * door_width
    wmidpoint = window_width/2

    #Window Frame
    window_center = houseWin.getMouse()
    window_label = Text(window_center,"x")
    window_label.draw(houseWin)

    #Window Positive Coordinates
    winUX = window_center.getX() 
    winUY = window_center.getY() + wmidpoint

    #winUpper_label = Text(Point(winUX,winUY),"a")
    #winUpper_label.draw(houseWin)

    winMidX = window_center.getX() + wmidpoint
    winMidY = window_center.getY()

    #winMid_label = Text(Point(winMidX,winMidY),"c")
    #winMid_label.draw(houseWin)

    pointA = Text(Point(winMidX,winUY),"o")
    pointA.draw(houseWin)


    #Window Negative Coordinates

    #Lower Corner
    winMin_X = window_center.getX() - wmidpoint
    winMin_Y = window_center.getY()

    winLX = window_center.getX()
    winLY = window_center.getY() - wmidpoint

    pointB = Text(Point(winMin_X,winLY),"k")
    pointB.draw(houseWin)

    #Window Frame
    window = Rectangle(Point(winMin_X,winLY),Point(winMidX,winUY))
    window.setFill("white")
    window.setOutline("blue")
    window.draw(houseWin)

    #Roof
    leftside = Point(x1,y2)
    rightside = Point(x2,y2)
    topclick = houseWin.getMouse()
    topside = Point(topclick.getX(),topclick.getY())

    roof = Polygon(leftside,rightside,topside)
    roof.setFill('black')
    roof.setOutline('red')
    roof.draw(houseWin)

    #wait for click and then quit
    houseWin.getMouse()
    houseWin.close()
    

House()
    
