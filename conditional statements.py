if(True):
    print('lasya')


if(False):
    print('yash')
else:
    print('jai')


num=9
if(num%2==0):
    print('even')
else:
    print('odd')


a=12
b=24
if(a>b):
    print('a is greater')
else:
    print('b is greater')


a=12
b=452
c=99
if(a>b):
    if(a>c):
        print('a is greater')
    else:
        print('c is greater')
else:
    if(b>c):
        print('b is greater')
    else:
        print('c is greater')



a=121111
b=23122
c=9045
d=999
if(a>b):
    if(a>c):
        if(a>d):
            print('a is greater')
        else:
            print('d is highest')
    else:
        if(c>d):
            print('c is greater')
        else:
            print('d is greater')
else:
    if(b>c):
        if(b>d):
            print('b is greater')
        else:
            print('d is greater')
    else:
        if(c>d):
            print('c is greater')
        else:
            print('c is greater')

if(False):
    print('lasya')
elif(False):
    print('jai')
elif(True):
    print('yash')
else:
    print('hello')
print('hi'+'jai')
print('wow')


year=2024
if(year%400==0):
    print('leapyear')
elif(year%4==0 and year%100!=0):
    print('leap year')
else:
    print('not a leap year')
