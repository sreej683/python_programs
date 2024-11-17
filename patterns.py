for n in range(1,5):
    print('*'*n)


for n in range(5,0,-1):
    print('*'*n)


space,star=4,1
while(space!=-1):
    print('-'space,''*star,sep='')
    space-=1
    star+=1

space,star=4,1
while(star!=11):
    print('-'space,''*star,sep='')
    star+=2
    space-=1


num,count=1,5
while(num!=6):
    print(str(num)*count)
    num+=1
    count-=1

space,num,count=4,5,1
while(space!=-1):
    print('-'*space,str(num)*count,sep='')
    space-=1
    num-=1
    count+=1


space,star=0,4
while(space!=4):
    print('-'space,''*star,sep='')
    space+=1
    star-=1

num,count=1,5
while(num!=6):
    print(str(num)*count)
    num+=1
    count-=1


space,num,count=4,5,1
while(space!=-1):
    print('-'*space,str(num)*count,sep='')
    space-=1
    num-=1
    count+=1

num,count=1,4
while(num!=5):
    print(str(num)*count)
    num+=1
    count-=1


space,num,count=0,1,4
while(num!=5):
    print('-'*space,str(num)*count,sep='')
    space+=1
    num+=1
    count-=1

num,count=5,5
while(num!=0):
    print(str(num)*count,sep='')
    num-=1
    count-=1


space,num,count=0,5,5
while(space!=5):
    print('-'*space,str(num)*count,sep='')
    space+=1
    count-=1
    num-=1


num,count=97,1
while(num!=102):
    print(str(chr(num))*count)
    num+=1
    count+=1


num,count=65,1
while(num!=70):
    print(str(chr(num))*count,sep='')
    num+=1
    count+=1

star,space=7,0
while(star!=-1):
    print(' 'space,''*star,sep=' ')
    star-=2
    space+=1
star,space=3,2
while(star!=9):
    print(' 'space,''*star,sep='')
    star+=2
    space-=1

sv=5
while(sv!=0):
    for num in range(sv,0,-1):
        print(num,end='')
    print()
    sv-=1


ev=4
while(ev!=-1):
    for num in range(5,ev,-1):
        print(num,end='')
    print()
    ev-=1

 sv=1
while(sv!=6):
    for num in range(sv,6):
        print(num,end='')
    print()
    sv+=1

k=1
for lines in range(1,5):
    for col in range(lines):
        print(k,end='')
        k+=1
    print()

for lines in range(5):
    for col in range(lines):
        print('*',end='')
    print()


star,space=1,4
while(star!=6):
    print('*'*star,''*space,sep='')
    star+=1
    space-=1



space,star=4,1
while(space!=-1):
    print(' 'space,''*star,sep=' ')
    space-=1
    star+=1


star,space=5,0
while(star!=0):
    print('*'*star,''*space,sep='')
    star-=1
    space+=1


space,star=0,5
while(space!=5):
    print(' 'space,''*star,sep='')
    space+=1
    star-=1


count=1
while(count!=6):
    print('1'*count)
    count+=1

space,count=4,1
while(count!=6):
    print(' '*space,'2'*count,sep=' ')
    space-=1
    count+=1


count=6
while(count!=0):
    print('3'*count,sep=' ')
    count-=1


space,count=0,5
while(space!=5):
    print(' '*space,'4'*count,sep=' ')
    space+=1
    count-=1


num,count=65,1
while(num!=70):
    print(str(chr(num)*count),sep=' ')
    num+=1
    count+=1


space,num,count=4,65,1
while(num!=70):
    print(' '*space,str(chr(num)*count),sep=' ')
    space-=1
    num+=1
    count+=1


num,count,space=65,5,0
while(num!=70):
    print(str(chr(num)*count),''*space,sep='')
    num+=1
    count-=1
    space+=1


space,num,count=0,65,5
while(space!=5):
    print(' '*space,str(chr(num)*count),sep='')
    space+=1
    num+=1
    count-=1

num,count,space=1,1,4
while(num!=6):
    print(str(num)*count,' '*space,sep='')
    num+=1
    count+=1
    space+=1


space,num,count=4,1,1
while(num!=6):
    print(''*space,str(num)*count,sep=' ')
    space+=1
    num+=1
    count+=1

for ev in range(1,7):
    print(*list(range(1,ev)),sep='')

for space,sv in zip(range(4,-1,-1),range(5,0,-1)):
    print(' '*space,*list(range(sv,6)),sep='')

n=9
space=0
for lines in range(n):
    print(' 'space+'')
    if lines<n//2:
        space+=1
    else:
        space-=1

num,space=65,4
for lines in range(1,6):
    for col in range(lines):
        print(str(chr(num)),''*space,end='')
        num+=1
    print()

num=1
for space,lines in zip(range(4,-1,-1),range(1,6)):
    print(' '*space,end='')
    for col in range(lines):
        print(num,end='')
        num+=1
    print()


for lines in range(1,6):
    for col in range(lines):
      if(lines==0 or lines==3 or lines==5):
          for n in range(1,6):
              print(n,sep=' ')
      else:
          for n in range(6,1,-1):
              print(n,sep=' ')
    print()



n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        print('*',end='')
    print()


n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if(row==col):
            print('*',end='')
        else:
            print(' ',end='')
    print()


n=5
for row in range(1,n+1):
    for col in range(1+n):
        if(row+col==6):
            print('*',end='')
        else:
            print(' ',end='')
    print()


n=6
for row in range(1+n):
    for col in range(1+n):
        if(row==col or row+col==6):
            print('*',end='')
        else:
            print(' ',end='')
    print()



n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if(row>=col):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if(row<=col):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


n=6
for row in range(1,n+1):
    for col in range(1,n+1):
        if(row+col>1+n):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


n=7
for row in range(1,n+1):
    for col in range(1,n+1):
        if(row-col<=1+n):
            print('*',end=' ')
        else:
            print(' ',end='')
    print()

num=5
for row in range(1,num+1):
    dummy=1
    for col in range(1,num+1):
        print(dummy,end='')
        dummy+=1
    print()

num=5
for row in range(1,num+1):
    dummy=row
    for col in range(1,num+1):
        print(dummy,end='')
    print()

num=5
dummy=1
for row in range(1,num+1):
    for col in range(1,num+1):
        print(dummy,end='')
        dummy+=1
    print()

num=int(input("enter"))
for row in range(1,num+1):
    dummy=row
    for col in range(1,num+1):
        print(dummy,end=' ')
        dummy+=1
    print()

num=int(input("enter"))
for row in range(1,num+1):
    for col in range(1,num+1):
        print(num,end='')
        num+=1
    print()
