#1
'''n=int(input('enter a value'))
star=1
space=4
while(star!=6):
    print('*'*star,''*space,sep='')
    star+=1
    space-=1
print()'''


#2
'''n=int(input('enter a value'))
for space,star in zip(range(n-1,-1,-1),range(1,n+1)):
    print(' '*space,'*'*star,sep='')'''

#3
'''n=int(input('enter a value'))
space=1
star=5
while(space!=6):
    print(' '*space,'*'*star,sep='')
    space+=1
    star-=1
print()'''

#4
'''n=int(input())
for space,star in zip(range(0,n),range(n,0,-1)):
    print(' '*space,'*'*star,sep='')'''

#5
'''n=int(input('enter a value'))
for space in range(n-1,-1,-1):
    print(' '*space+'*',sep='')'''
#6
'''n=int(input('enter a value'))
for space in range(n+1):
    print(' '*space+'*',sep='')'''
#7
'''n=int(input('enter a value'))
for space in range(n):
    print(' '*space+'A',sep='')'''

#8
'''n=int(input('enter a value'))
for space in range(n-1,-1,-1):
    print(' '*space+'M',sep='')'''
#9
'''n=int(input('enter a value'))
for ch in range(1,n+1):
    print(ch*'A',sep='')'''
#10
'''n=int(input('enter a value'))
for ev in range(6,0,-1):
    num=1
    while(num!=ev):
        print(num,end='')
        num+=1
    print()'''
#11
'''n=int(input('enter a value'))
num=1
count=5
while(num!=6):
    print(str(num)*count,sep='')
    num+=1
    count-=1
print()'''
#12
'''n=int(input('enter a value'))
num=1
count=1
while(num!=6):
    print(str(num)*count,sep='')
    num+=1
    count+=1
print()'''

#13
'''n=int(input('enter a value'))
num=1
count=1
space=5
while(num!=6):
    print(' '*space,str(num)*count,sep='')
    num+=1
    count+=1
    space-=1
print()'''

#14
'''n=int(input('enter a value'))
for ev in range(2,7):
    num=1
    while(num!=ev):
        print(num,end='')
        num+=1
    print()'''

#15
'''n=int(input('enter a value'))
for space,ev in zip(range(5,0,-1),range(2,7)):
    print(' '*space,end='')
    num=1
    while(num!=ev):
        print(num,end='')
        num+=1
    print()'''

#16
'''n=int(input('enter a value'))
for space,ev in zip(range(1,n+1),range(n+1,0,-1)):
    print(' '*space,end='')
    num=1
    while(num!=ev):
        print(num,end='')
        num+=1
    print()'''

#17
'''n=int(input('enter a number'))
for lines in range(1,n+1):
    for col in range(lines):
        print(n,end='')
        n+=1
    print()'''

#18
'''k=65
n=int(input())
for lines in range(1,n+1):
    for col in range(lines):
        print(chr(k),end=' ')
        k+=1
    print()'''

#19
'''k=65
count=5
n=int(input('enter a value'))
for lines in range(1,n+1):
    for col in range(lines):
        print(chr(k)*count,sep='')
        k+=1
        count-=1'''
#20
'''n=int(input('enter a value'))
for lines in range(1,n+1):
    print('1'*lines,sep='')'''

#21
'''n=int(input('enter a value'))
for space,lines in zip(range(n-1,-1,-1),range(1,n+1)):
    print(' '*space,'2'*lines,sep='')'''

#22
'''n=int(input())
for lines in range(n-1,-1,-1):
    print('3'*lines,sep='''

#23
'''n=int(input('enter a value'))
for space,lines in zip(range(0,n),range(n,0,-1)):
    print(' '*space,'4'*lines,sep='')'''

#24
'''n=int(input())
num,count=65,1
while(num!=70):
    print(str(chr(num)*count))
    num+=1
    count+=1'''

#25
'''n=int(input())
num,count,space=65,1,5
while(num!=70):
    print(' '*space,str(chr(num)*count))
    num+=1
    count+=1
    space-=1'''
    
#26
'''n=int(input())
num,count,space=65,5,1
while(num!=70):
    print(' '*space,str(chr(num)*count))
    num+=1
    count-=1
    space+=1'''

#27
'''n=int(input('enter a value'))
for space,star in zip(range(5,0,-1),range(1,6)):
    print(' '*space,'B'*star,sep='')'''

#28
'''n=int(input())
for space,star in zip(range(5),range(5,0,-1)):
    print(' '*space,'D'*star,sep='')'''

#29
'''n=int(input('enter a value'))
for num,count in zip(range(1,6),range(5,0,-1)):
    print(str(num)*count)'''

#30
'''k=65
n=int(input())
for lines in range(n,0,-1):
    for col in range(lines):
        print(chr(k),end='')
        k+=1
    print()'''

#31
'''k=65
n=int(input())
for lines in range(1,n+1):
    for col in range(lines):
        print(chr(k),end='')
        k+=1
    print()'''


#32
'''n=int(input())
k=1
for space,lines in zip(range(n-1,-1,-1),range(1,n+1)):
    print(' '*space,end=' ')
    for num in range(lines):
        print(k,end='')
        k+=1
    print()'''

#33
'''n=1
for lines in range(5,0,-1):
    for col in range(lines):
        print(n,end='')
        n+=1
    print()'''

#34
'''n=int(input())
k=1
for space,lines in zip(range(n),range(n,0,-1)):
    print(space*' ',end='')
    for num in range(lines):
        print(k,end='')
        k+=1
    print()'''

#35
'''n=int(input())
for space,star in zip(range(1,n+1),range(n,-1,-1)):
    print(' '*space,'C'*star,sep='')'''
