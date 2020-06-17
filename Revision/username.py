#Arthur : Eugene Parker



def username():
    print("This application is to provide customer usernames based on their names")
    firstname = input("Please enter your firstname: ")
    surname = input("Please enter your surname: ")

    #Formula
    first = firstname[0].lower()
    last = surname[:8].lower()
    username = first + "." + last


    print("Dear {}, your assigned username is {}".format(firstname,username))

username()

    
