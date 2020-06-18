from graphics import *
def tictactoe():
    win = GraphWin("Tic Tac Toe, 500,500")
    win.setCoords(0.0,0.0,3.0,3.0)

    #Creating Vertical Lines
    vl1 = Line(Point(1.0,0.0),Point(1.0,3.0))
    vl1.draw(win)

    vl2 = Line(Point(2.0,0.0),Point(2.0,3.0))
    vl2.draw(win)


    #Creating horiztoal lines

    hl1 = Line(Point(0.0,2.0),Point(3.0,2.0))
    hl1.draw(win)

    hl2 = Line(Point(0.0,1.0),Point(3.0,1.0))
    hl2.draw(win)

    for i in range(10):
        p = win.getMouse()
        print("X:",p.getX(), "Y:",p.getY())
        
    

tictactoe()
