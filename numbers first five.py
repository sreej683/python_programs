n=1
c=0
while True:
    fc=0
    for fa in range(1,n+1):
        if(n%fa==0):
            fc+=1
    if(fc==2):
        print(n)
        c+=1
    n+=1
    if(c==5):
        break



n=1
c=0
while True:
    fc=0
    for fa in range(1,n+1):
        if(n%fa==0):
            fc+=1
    if(fc>2):
        print(n)
        c+=1
    n+=1
    if(c==5):
        break
