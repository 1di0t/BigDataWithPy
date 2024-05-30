#Generator
def my_range(f=0,length=10,step=1):
    number = f
    while number < length:
        yield number#return number and run next line
        number += step

print(my_range)
r = my_range(1,5)
print(r)
for i in r:
    print(i,end=' ')
for i in r:
    print(i,end=' ')