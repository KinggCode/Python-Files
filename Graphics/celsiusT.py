from graphics import *

win = GraphWin("Celsius Convertor",640,480)
win.setBackground('gray')
win.setCoords(0,0,3.0,4.0)

cel = Text(Point(1,3),"Celsius Temperature").draw(win)
fah = Text(Point(1,1),"Fahrenheit Temperature").draw(win)

input = Entry(Point(2,3),40)
input.setText("Enter a number: ")
input.draw(win)


output = Text(Point(2,1),"")
output.draw(win)
button = Text(Point(1.5,2.0),"Convert It")
button.draw(win)
Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

# wait for a mouse click
win.getMouse()
# convert input
celsius = eval(input.getText())
fahrenheit = 9.0/5.0 * celsius + 32
# display output and change button
output.setText(fahrenheit)
button.setText("Quit")
# wait for click and then quit
win.getMouse()
win.close()
