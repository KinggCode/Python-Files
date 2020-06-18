#Name: Eugene Parker
#Tasks: Taemperature Converter

def message():
    print("Welcome to OxygenHub")
    print("We provide you with the most effective temperature converter")
    
def temp_type():
    temp_list = {"1":"Fahrenheit","2":"Celcius"}
    for i in temp_list:
        temp_available = temp_list[i].upper()
        print("{}. {}".format(i,temp_available))

def fahren_converter():
    print("Welcome to the Fahrenheit Convertor: ")
    fahren_input = eval(input("Please enter the temperature in fahrenheit: "))
    fahren_to_celsius = (fahren_input - 32)*5/9
    print("Your temperature in Degrees Celsius is {}".format(fahren_to_celsius))

def celsius_converter():
    print("Welcome to the Degrees Celcius Convertor: ")
    celsius_input = eval(input("Please enter the temperature in Degrees Celsius: "))
    celsius_to_fahren = (celsius_input * 9/5) + 32
    print("Your temperature in Degrees Fahrenheit is {}".format(celsius_to_fahren))

def win():
    window.clear()


def temp_func():
    user_choice = int(input("What temperature are converting ( 1 or 2): "))
    if(user_choice == 1):
        fahren_converter()
        
    elif(user_choice == 2):
        celsius_converter()
    else:
        prog_exist()

        
def prog_exit():
    print("Thank ypu for trting this program")



def temperature():
    message()
    temp_type()
    for i in range(2):
        temp_func()
    
    
temperature()

