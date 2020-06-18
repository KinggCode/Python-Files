tpl = (40,50,40,"xyz")
print(tpl)

#Indexing with tuple
a = tpl[3]
print(a)
b = tpl.index("xyz")
print(b)

#Counting with Tuples
c = tpl.count(40)
print(c)


#Converting list to Tuples
lst = [67,34,"XYZ"]
tpl1 = tuple(lst)
print(tpl1)


#Convering tuple to list
d = list(tpl)
print(d)
