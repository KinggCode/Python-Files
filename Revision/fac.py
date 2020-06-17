#Arthur : Eugene Parker

def main():
    n = eval(input("Please a number: "))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
        print(fact)
