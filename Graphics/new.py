from graphics import * 


# Get principal and interest rate
principal = eval(input("Enter the initial principal: "))
apr = eval(input("Enter the annualized interest rate: "))


win = GraphWin("Investment Chart",640,480)
win.setBackground('white')
win.setCoords(-1.75,-200,11.5,10400)
Text(Point(-1, 0), ' 0.0K').draw(win)
Text(Point(-1, 2500), ' 2.5K').draw(win)
Text(Point(-1, 5000), ' 5.0K').draw(win)
Text(Point(-1, 7500), ' 10.0K').draw(win)
bar = Rectangle(Point(0, 0), Point(1, principal))
bar.setFill("green")
bar.setWidth(2)
bar.draw(win)

for year in range(1,11):
    principal *= (1 + apr)
    bar = Rectangle(Point(0,0),Point(year+1,principal))
    bar.setFill('blue')
    bar.setWidth(2)
    bar.draw(win)
