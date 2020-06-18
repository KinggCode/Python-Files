from graphics import *

def polyGraph():
    win = GraphWin("Polygraph",300,300)

    message = Text (Point(2.0,0.5),"Click three points")
    message.draw(win)
    win.setCoords(0.0,0.0,5.0,5.0)
    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)

    p3 = win.getMouse()
    p3.draw(win)


    poly = Polygon(p1,p2,p3)
    poly.setFill("cyan")
    poly.setOutline("red")
    poly.draw(win)

    message.setText("Click to quit")
    win.getMouse()
    win.close()

polyGraph()
