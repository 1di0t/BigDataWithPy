a= [[-9,8],11,7]
#shallow copy
b=a.copy()#copy list a data in list b
c= list(a)
d=a[:]
print(a,b,c,d)
b[0][1] =100
print(a,b,c,d)