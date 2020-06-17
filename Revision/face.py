#Author : Eugene Parker
from graphics import *

def facelook():
    facewin = GraphWin("Face Graph",600,400)
    facewin.setCoords(0.0,0.0,5.0,5.0)
    facewin.setBackground("brown")

    center = Point(1,3)
    radius = 0.5
    leftEye = Circle(center,radius)
    leftEye.setFill("red")
    leftEye.draw(facewin)


    rightEye = leftEye.clone()
    rightEye.move(2,0)
    rightEye.setFill("yellow")
    rightEye.draw(facewin)

    mouth = Rectangle(Point(1,1),Point(3,2))
    mouth.setFill("black")
    mouth.draw(facewin)

    inner = Rectangle(Point(1.2,1.2),Point(2.8,1.8))
    inner.setFill("white")
    inner.draw(facewin)

facelook()
