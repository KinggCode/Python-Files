def usernameGenerator():
    firstname = input("Enter your  firstname: ")
    lastname  =input("Enter your lastname: ")

    formula = firstname[0] + lastname[:7]
    username = formula.lower()

    print("Your username is {}".format(username))

usernameGenerator()
