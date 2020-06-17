def main():
    user_input = input("Please enter your name: ")
    count = 0
    for i in range(len(user_input)):
        letter = user_input[i]

      
        for i in letter:
            namesNum = ord(i)
            count +=namesNum
    print(count)
main()
