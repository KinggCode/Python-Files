s ={20,30,10,'xyz',20,10}
# print(s)
# print(type(s))


#Adding elements to a set
s.update([88,99])
print(s)

#Frozen set
p = frozenset(s)
print(p)

#Updatin after set freeze
p.update([2,"Eugene"])
print(p)
