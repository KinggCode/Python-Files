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



