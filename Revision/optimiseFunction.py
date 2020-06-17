#Arthur : Eugene Parker
#Tasks : Working with functions


def message(person):
    print("Dear {},".format(person))
    print("Welcome to Birthday Tunes on the hill")

def happy():
    print("Happy Birthday to you!")

def sing(person):
    happy()
    happy()
    print("Happy Birthday dear, {}.".format(person))
    happy()


def main():
    people = ["Ama","Kofi","Tasha","Zoe"]
    for person in people:
        message(person)
        sing(person)
        print()
main()
