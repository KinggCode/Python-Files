from graphics import *

win = GraphWin("Triangle",320,240)
win.setCoords(0.0,0.0,10.0,10.0)
win.setBackground("black")

p1 = win.getMouse()
txt1 = Text(Point(p1.getX(),p1.getY()),"x")
txt1.setFill('white')
txt1.draw(win)

p2 = win.getMouse()
txt2 = Text(Point(p2.getX(),p2.getY()),"x")
txt2.setFill('white')
txt2.draw(win)

p3 = win.getMouse()
txt3 = Text(Point(p3.getX(),p3.getY()),"x")
txt3.setFill('white')
txt3.draw(win)

triangle = Polygon(p1,p2,p3)
triangle.setFill("red")
triangle.setOutline("blue")
triangle.draw(win)
