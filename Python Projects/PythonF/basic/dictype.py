dict={1:"john",2:"Bob",3:"Bill"}
print(dict)

#Getting the sepearate elements
print(dict.items())

#Getting the keys
a = dict.keys()
print(a)

#Getting VALUES
v = dict.values()
for i in v:
    print(i)

del(dict[2])
print(dict)
