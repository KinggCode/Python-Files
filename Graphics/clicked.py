from graphics import *
def main():
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        point = Text(Point(p.getX(),p.getY()),"x")
        point.draw(win)
        print("You clicked at:", p.getX(), p.getY())
main()
