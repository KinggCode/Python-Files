from graphics import *

def convert():
    win = GraphWin("Convert Currency", 320,400)
    win.setCoords(0.0,0.0,4.0,4.0)


    #Celsius Label
    celsius_label = Text(Point(1.0,3.5),"Celsius Temperature: ")
    celsius_label.draw(win)

    #User Entry
    user_input = Entry(Point(3.0,3.5),10)
    user_input.setText("0.0")
    user_input.draw(win)

    #Fahrenheit Label
    fahren = Text(Point(1,1),"Fahrenheit Temperature: ")
    fahren.draw(win)

    #Output
    output = Text(Point(2.5,1),"")
    output.draw(win)

    #button
    button = Text(Point(1.5,2.0),"Convert It")
    button.draw(win)
    rec = Rectangle(Point(1,1.5),Point(2,2.5))
    rec.draw(win)

convert()
