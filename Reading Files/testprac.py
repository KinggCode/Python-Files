def test():
    try:
        user = eval(input("Enter a value above: "))
        a = user + 1
    except ValueError:
        print("Wrong input")
    except NameError:
        print("Name input worng")
    except SyntaxError:
        print("Syntax error")


test()
