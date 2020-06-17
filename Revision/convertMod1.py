H def convertMod4():
    for celsius in range(10,110,10):
        fahrenheit = 9/5 * celsius + 32
        print("{}C = {}F".format(celsius,fahrenheit))
        
convertMod4()
