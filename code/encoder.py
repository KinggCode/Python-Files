#Arthur : Eugene Parker


def encoder():
    message = input("Please a message: ")
    for ch in message:
        en_key = ord(ch)
        print(en_key, end = " ")

encoder()


def decoder():
    en_key = input("Enter decoder key given: ")
    de_key = en_key.split()
    for num in de_key:
        decoded_message = chr(int(num))
        print(decoded_message, end="")

decoder()
        
