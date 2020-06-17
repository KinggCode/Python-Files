#Author : Eugene Parker
#Task: Using graphics and objects to draw a rectangle and perform some functions.

from graphics import * 
def recGraph():
    print("Welcome to Graph World!")
    recGraph = GraphWin("Graph World!", 600,400)
    recGraph.setCoords(0.0,0.0,5.0,5.0)
    recGraph.setBackground("black")

    #Getting coordinates of the rectangle.
    p1 = recGraph.getMouse()
    p1Text = Text(p1,"a")
    p1Text.setFill("white")
    p1Text.draw(recGraph)

    p2 = recGraph.getMouse()
    p2Text = Text(p2,"b")
    p2Text.setFill("white")
    p2Text.draw(recGraph)

    rec = Rectangle(p1,p2)
    rec.setFill("white")
    rec.draw(recGraph)

    #Accessing iNstance Variable using getX() & getY()
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()


    width = abs(x2 - x1)
    length = abs(y2 - y1)

    #Program Default
    Area = width * length
    Perimeter = 2 **(length + width)

    print(width)

    print("The area of the rectangle is {}".format(Area))
    print("The perimeter of the rectangle is {}".format(Perimeter))

    #Wait for a last click to quit 
    recGraph.getMouse()
    recGraph.close()
    
recGraph()
