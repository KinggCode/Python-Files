#This mod checks for prime numbers only ..;

def primeNumMod(c):
    if(c>1):
        for i in range(2,c):
            if(c%i)==0:
                return 0
            else:
                return 1
    else:
        return 0

#End of prime Mod ...


    

#This mod checks for only even numbers...

def evenNumbers(a):
    if(a%2 == 0):
        return 1
    else:
        return 0


#End of even Mod...




#This mod checks for only odd numbers...

def oddNumbers(b):
    if(b%2!=0):
        return 1
    else:
        return 0


#End of odd Mod...


    
