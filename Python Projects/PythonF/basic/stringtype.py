s = "  You are awesome "
# print(s[0:9:2])
# print(s)

s1 = """ You are
    the creator
    of your desting """

# print(s)


t = s * 2
# print(t)


#length
# print(len(s))

#slicing
f = "Food"
# print(f[0:])
# print(f[0:3])
# print(f[:3])
# print(f[-3:-1])

#Striping
print(s.strip())
print(s.lstrip())


#Find
print(s.find('awe'))
print(s.find('awe',0,8))

#Count
print(s.count(" "))

#Replace
print(s.replace("awesome","super"))

#Upper
print(s.upper())

#Lower
print(s.lower())

#Title
print(s.title())
