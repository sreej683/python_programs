def genfunc():
    print('gen is started')
    yield 23
    print('content of first gen is printed')
    yield 'lasya'
    print('content of second gen is printed')
    print('last')
    yield 'yash','jai','lasya'
g=genfunc()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


def rangegen(ll,ul,up=1):
    while(ll<ul):
        yield ll
        ll+=up
ran=rangegen(1,10,1)
for i in ran:
    print(i)


def fibbgen(fv,sv,n):
    i=1
    while i<n+1:
        yield fv
        fv,sv=sv,fv+sv
        i+=1
gfo=fibbgen(2,3,10)
for i in gfo:
    print(i)

def func():
    print('hai')
    print('hello')
    return 23
s=func()
print(s)

def gen():
    i=1
    while i<2:
        yield i
        i+=1
g=gen()
print(g._sizeof_())
print(iter([1])._sizeof_())



def gen():
    yield 200
    yield 999
ob=gen()
print(next(ob))
print(next(ob))

def even():
    for num in range(20,31):
        if num%2==0:
            yield num
ob=even()
print(next(ob))
print(next(ob))
print(next(ob))
print(next(ob))
print(next(ob))
print(next(ob))
print(next(ob))


def fib(num,first=0,second=1):
    for i in range(num):
        third=first+second
        yield first
        first,second=second,third
obj=fib(6)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
