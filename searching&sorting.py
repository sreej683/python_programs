#linear search

l=[23,99,456,67]
se=99
for ind in range(len(l)):
    if l[ind]==se:
        print(ind)
        break
else:
    print(-1)


def linear(list,se):
    for ind in range(len(lst)):
Z        if lst[ind]==se:
            return ind
    return -1
lst=[12,45,88,99]
se=99
print(linear(lst,se))'''


'''#binary search

l=[1,3,4,5,6,9]
se=99
lowind=0
highind=len(l)-1
while(lowind<=highind):
    mid=(lowind+highind)//2
    if l[mid]<se:
        lowind=mid+1
    elif l[mid]>se:
        highind=mid-1
    elif l[mid]==se:
        print(mid)
        break
else:
    print(-1)





