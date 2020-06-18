lst = []
# print(lst)


lst1 = [10,20,"Kwadjo",-22.5, 30.5]
# print(lst1[2][:3].upper())


#Adding elements to a list container
lst1.append(40)
print(lst1)

#Removing the last elements in list
lst1.pop()
# print(lst1)

#Removing an element in list
lst1.remove("Kwadjo")
print(lst1)


#Maximum Number
print(lst1)
a = max(lst1)
print(a)


#Minimum Number
b = min(lst1)
print(b)

#Inserting an element in a list
lst1. insert(3, "Eugene")
print(lst1)
del(lst1[3])
print(lst1)

#Sort list
lst1.sort()
print(lst1)

#Reverse sorting
lst1.sort(reverse = True)
print(lst1)
