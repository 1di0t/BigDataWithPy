import copy
c= [1,2,3,4]
d=c
e = c.copy()
print(c,d,e)
d[1] = 200
print(c,d,e)
a= [[-9,8],11,7]
#deep copy
b =copy.deepcopy(a)

print(a,b)
b[0][1] =100
print(a,b)