#printing primes:


num=9441531654
while(num!=0):
    ld=num%10
    fcount=0
    for fa in range(1,ld+1):
        if(ld%fa==0):
            fcount+=1
    if(fcount==2):
        print(ld)
    num//=10


num=123
dsum=0
while(num!=0):
    ld=num%10
    num//=10
    fcount=0
    for fa in range(1,ld+1):
        if(ld%fa==0):
            fcount+=1
        if(fcount==2):
            print(ld)
            dsum+=ld
print(dsum)


for num in range(23,43):
    fcount=0
    for fa in range(1,num+1):
        if(num%fa==0):
            fcount+=1
    if(fcount==2):
        print(num)


max=0
for num in range(10,50):
    fcount=0
    for fa in range(1,num+1):
        if(num%fa==0):
            fcount+=1
    if(fcount==2):
        if(max<num):
            max=num
print(max)


for num in range(100,1000):
    fcount=0
    for fa in range(1,num+1):
        if(num%fa==0):
            fcount+=1
    if(fcount==2):
        print(num,end=',')



#two digit palyprime:

for num in range(10,100):
    copy=num
    rev=0
    fcount=0
    while(num!=0):
        ld=num%10
        rev=rev*10+ld
        num//=10
    for fa in range(1,copy+1):
        if(copy%fa==0):
            fcount+=1
    if(copy==rev and fcount==2):
        print(copy)


num=2
fcount=0
for fa in range(1,num+1):
    if(num%fa==0):
        fcount+=1
print('prime' if(fcount==2)else 'not prime')


num=12
fcount=0
for fa in range(1,num+1):
    if(num%fa==0):
        fcount+=1
print('composite'if(fcount>2) else 'not composite')


num=6
dsum=0
for fa in range(1,num):
    if(num%fa==0):
        dsum+=fa
print('perfect'if(dsum==num)else 'not perfect')


num=324
copy=0
dsum=0
while(num!=0):
    ld=num%10
    dsum+=1
    num//=10
print('niven'if(copy%dsum==0)else 'not perfect')


num=222
copy=num
rev=0
while(num!=0):
    ld=num%10
    rev=rev*10+ld
    num//=10
print('palindrome' if(rev==copy)else 'not palindrome')


num=11
copy=num
rev=0
fcount=0
while(num!=0):
    ld=num%10
    rev=rev*10+ld
    num//=10
for fa in range(1,copy+1):
    if(copy%fa==0):
        fcount+=1
print('palyprime'if(copy==rev and fcount==2) else 'not palyprime')


num=13
copy=num
rev,fcount=0,0
while(num!=0):
    ld=num%10
    rev=rev*10+ld
    num//=10
for fa in range(1,copy+1):
    if(copy%fa==0):
        fcount+=1
for fa in range(1,rev+1):
    if(rev%fa==0):
        rev+=1
print('emirp'if(copy!=rev)and(fcount==2)and(rev==2)else 'not emirp')


num=153
copy=num
count=len(str(num))
dsum=0
while(num!=0):
    ld=num%10
    dsum+=ld**count
    num//=10
print('armstrong'if(copy==dsum)else 'not armstrong')


num=135
copy=num
count=len(str(num))
dsum=0
while(num!=0):
    ld=num%10
    dsum+=ld**len(str(num))
    num//=10
print('disarium'if(copy==dsum)else 'not disarium')

num=123
dsum=0
dprod=1
while(num!=0):
    ld=num%10
    dsum+=ld
    dprod*=ld
    num//=10
print('spy'if(dsum==dprod)else 'not spy')

num=145
fsum=0
copy=num
while(num!=0):
    ld=num%10
    fact=1
    num//=10
for n in range(ld,0,-1):
    fact*=n
dsum+=fact
print('strong'if(fsum==num)else 'not strong')

num=11
while(num>9):
    dsum=0
    while(num!=0):
        ld=num%10
        dsum+=ld**2
        num//=10
    num==dsum
print('happy'if(num==1 or num==7)else 'not happy')


num=25
square=num**2
count=len(str(num))
rem=square%(10**count)
print('automorphic'if(num==rem)else 'not automorphic')

num=125
cube=num**3
count=len(str(num))
rem=cube%(10**count)
print('trimorphic'if(num==rem)else 'not trimorphic')



def emirp(n):
    c,rev,copy=0,0,n
    while(n!=0):
        ld=n%10
        rev=rev*10+ld
        n//=10
    fc=0
    for fa in range(1,copy+1):
        if(n%fa==0):
            fc+=1
    rc=0
    for ja in range(1,rev+1):
        if(rev%ja==0):
            rc+=1
    if(copy!=rev and fc==2 and rc==2):
        print(copy)
        c+=1
        while(1):
            if(c==10):
                break
emirp(int(input('enter a number')))



#special number:
n=0
dummy=n
summ=0
while(dummy>0):
    rem=dummy%10
    dummy//=10
    fact+=1
