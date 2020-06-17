def namecount():
    count = 0
    user = input("Enter name: ")
    for ch in user:
        num = int(ord(ch))
        count = count + num
        print(num,end=" ")
    print()
    print("Total is {}".format(count))

namecount()
        
