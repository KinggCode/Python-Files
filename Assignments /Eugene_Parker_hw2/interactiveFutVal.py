#EugeneParker
#Assignment2
#Source: Python Programming:John Zelle
#Chapter 4 (Objects & Graphics)

#Importing graphics Library
from graphics import *


def futureValue():
    print("Welcome to Investment Simulator \n This application provides a forecast within a ten year period.")
    win = GraphWin("Investment Simulator",600,500)
    win.setCoords(0.0,0.0,10.0,10.0)
    win.setBackground('gray')

    #Interface Design

    #Application Title
    title = Text(Point(5,9),"W E L C O M E     T O      I N V E S T M E N T     H U B")
    title.setOutline('white')
    title.draw(win)

    #Principal Section
    principal_label = Text(Point(2,8),"PRINCIPAL  AMOUNT: ")
    principal_label.setOutline('white')
    principal_label.draw(win)
    principal_amt = Entry(Point(6,8),50)
    principal_amt.setText("0.0")
    principal_amt.draw(win)

    #Interest Section
    interestRate_label = Text(Point(2,7),"INTEREST  RATE:")
    interestRate_label.setOutline('white')
    interestRate_label.draw(win)
    interestRate = Entry(Point(6,7),50)
    interestRate.setText("0")
    interestRate.draw(win)

    #Period Section
    period_label = Text(Point(2,6),"PERIOD: ")
    period_label.setOutline('white')
    period_label.draw(win)

    periodLen = Entry(Point(6,6),50)
    periodLen.setText("0")
    periodLen.draw(win)

    #Simulator Button
    simulate_btn = Text(Point(5,4.5),"S I M U L A T E")
    simulate_btn.setOutline("white")
    simulate_btn.draw(win)
    simulate_box = Rectangle(Point(3,4),Point(7,5)).draw(win)


    #Result Section
    result_title = Text(Point(5,3),"A N A L Y S I S")
    result_title.setOutline('white')
    result_title.draw(win)
    
    #Future Value Section
    futureV_label = Text(Point(2,2),"PRINCIPAL AMOUNT:")
    futureV_label.setOutline('white')
    futureV_label.draw(win)
    future_amount = Text(Point(4,2),"")
    future_amount.draw(win)

    interest_label = Text(Point(2,1), "INTEREST: ")
    interest_label.setOutline('white')
    interest_label.draw(win)
    interest_amount = Text(Point(4,1),"")
    interest_amount.draw(win)

    win.getMouse()
    
    #Application Formulae:
    principal = eval(principal_amt.getText())
    in_amt = principal
    apr = eval(interestRate.getText())
    apr = apr/100
    period = eval(periodLen.getText())

    graphChart = GraphWin("Investment Growth Chart",320,340)
    graphChart.setBackground("white")
    Text(Point(20,230), '0.0K').draw(graphChart)
    Text(Point(20,180), '2.5K').draw(graphChart)
    Text(Point(20,130), '5.0K').draw(graphChart)
    Text(Point(20,80), '7.5K').draw(graphChart)
    Text(Point(20,30), '10.0K').draw(graphChart)
    
    
    #Bars
    height = principal * 0.02
    bar_box = Rectangle(Point(40, 230), Point(65, 230-height))
    bar_box.setFill("blue")
    bar_box.setWidth(2)
    bar_box.draw(graphChart)
    for year in range(1,period):
        principal = principal * (1 + apr)
        interest = principal - in_amt
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(graphChart)

    #Displaying Output & Chnaging button text
    future_amount.setText(principal)
    interest_amount.setText(interest)
    simulate_btn.setText("Quit")

    #wait for click and then quit
    win.getMouse()
    win.close()
    graphChart.close()

futureValue()
    
