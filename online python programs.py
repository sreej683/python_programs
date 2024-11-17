#printing hello world:

print('hello world')

#adding two numbers:
a=20
b=30
j=a+b
print(j)
#printing square root:
a=8
sqrt=a**0.5
print(sqrt)

#printing area of triangle:
a=2
b=6
c=9
s=(a+b+c)/2
print(s*((s-a)+(s-b)+(s-c))*0.5)
#swapping:
a=20
b=45
a,b=b,a
print(a,b)
#generate a random number:
import random
print(random.randint(0,9))

#check number is positive,negative or zero:
num=-2
if num>0:
    print('positive')
elif num==0:
    print('zero')
else:
    print('negative')

#check number is odd or even:

num=3
if num%2==0:
    print('even')
else:
    print('odd')

#check year is leap year or not:

year=2024
if year%400==0:
    print('leap year')
elif year%4==0 and year%100!=0:
    print('leap year')
else:
    print('not a leap year')

#largest among three numbers:

a=19
b=8
c=59
if a>b and a>c:
    print('a is greater')
elif b>c:
    print('b is greater')
else:
    print('c is greater')


#check prime number or not:

num=2
fcount=0
for fa in range(1,num+1):
    if(num%fa==0):
        fcount+=1
print('prime' if(fcount==2) else 'not prime')

#prime numbers in range:

lower=900
upper=1000
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                print(num)

a='xyz'
print(a[::-1])

#factorial:

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


#multiplication table:

num=5
for i in range(1,11):
     print(num, 'x', i, '=', num*i)


#Armstrong number:

num=153
copy=num
count=len(str(num))
dsum=0
while(num!=0):
    ld=num%10
    dsum+=ld**count
    num//=10
print('Armstrong'if(copy==dsum)else 'not Armstrong')


#Armstrong numbers within a range:

for num in range(100,1000):
    num=copy
    dsum=0
    count=len(str(num))
    while(num!=0):
        ld=num%10
        dsum+=ld**count
        num//=10
    if(copy==dsum):
        print(copy)

#sum of natural numbers:

def sum(n):
    if n==1 or n==0:
        return 1
    else:
        return n+sum(n+1)
print(sum(5))

d='kiran'
print(d[0:2])


arr=[12,5,8,19,29]
def second_largest(arr):
    arr.sort()
    return arr[-3]
print(second_largest(arr))
