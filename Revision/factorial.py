def main():
    n = eval(input("Please enter the number: "))
    fact =1
    for factor in range(n,1,-1):
        fact = fact * factor
    print(fact)
main()
