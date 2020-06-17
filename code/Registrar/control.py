def storageNames():
    users = []
    names = open("read.txt", "r")
    for name in names:
        y = name.split("/")
        user = y[0]
        users.append(user)
    return users

def EmailCheck(email):
    users = storageNames()
    if email in users:
        return "proceed"
    else:
        return "fail"


