def deco(fun):
    def inner():
        result = fun()
        return result * 2
    return inner

@deco
def num():
    return 5

#resultfun = deco(num)
print(num())
