class student(Exception):
    def _init_(self):
        self=self.msg
    def _str_(self):
        return self.msg


try:
    raise saturday('Mock Interview')
except saturday as msg:
    print(f'error:{msg}')


try:
    print('lasya')
    print('12'+12)
except:
    print('except block is executed')

try:
    print(234)
    print('99'+'jai')
except:
    print('try block is executed')

try:
    print(99)
    print('lasya'+'shree')
except:
    print('except block is not executed')
finally:
    print('finally block is also not executed')

try:
    print(234)
    print(99)
    try:
        print(a)
    except:
        print('a is not available')
except:
    print(a=23)

try:
    print(234+'1')
    try:
        print(a)
    except:
        print('a is not available')
finally:
    print('hello')


l=[12,15,0,'a',9]
try:
    res=0
    for num in l:
        res+=l[num]
    print(num)
except IndexError as msg:
    print(f'error:{msg}')
except TypeError as msg:
    print(f'error:{msg}')
except ZeroDivisionError as msg:
    print(f'error:{msg}')


l=[12,99,34]
try:
    res=0
    for num in l:
        res+=num
    print(res)
except(IndexError,ZeroDivisionError,TypeError)as msg:
    print(f'error:{msg}')
else:
    print('no error')


try:
    print(56/0)
except:
    print('no error')
else:
    print('error')
finally:
    print('error executed')


raise IndexError('not possible')
raise TypeError('lasyashree......')

n=12
assert(n%2==0),'not even'
print('even')

n=99
assert(n%2!=0),'even'
print('not even')


s='123'
try:
    assert s[-1]=='0','not ending'
except AssertionError as msg:
    print(f'error:{msg}')
else:
    print('no error')

s=100
try:
    assert(s%2==0),'odd number'
except AssertionError as msg:
    print(f'error:{msg}')
else:
    print('odd number')


try:
    print('a'+23)
    print('shree')
except:
    print("hello lasya"+22)
finally:
    print("hello yash")
