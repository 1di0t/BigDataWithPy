shu = {"Name":"현엉","Gender":"woman","Height":405,"Weight":1450,"Vision":[55.0,73.0]}

for i in shu:#keys
    print(i,end=' ')
print()
for i in shu.values():#values
    print(i,end=' ')
print()
for i in shu.items():#key & values
    print(i,end=' ')
print()
for i in shu.items():#key & values
    print(f'{i[0]} is  {i[1]}')
print()
for i,k in shu.items():#unpacking
# #insert each values in another val
    print(f'{i} is  {k}')
print()