   for i in range(1,5):
    print(i)

    
l=[1,2,3,4,5]
t=(2,3,4,5,6)
s1='jayashree'
s2='lasya'
z=zip(l,t,s1,s2)
for (v1,v2,v3,v4) in z:
    print(v1,v2,v3,v4,sep=',')


d={'a':10,'b':30,'name':'yash'}
for key,value in d.items():
    print(f'{key}={value}')


s='jayashree'
for ch in s:
    print(ch)
else:
    print('hi')



num=range(1,10)
for num in range(1,11):
    print(num)


num=range(11,0,-1)
for num in range(10,0,-1):
    print(num)


while(False):
    print('hi')
else:
    print('yash')


a=2
while(a!=12):
    print(a)
    a+=2

a=-10
while(a!=0):
    print(a)
    a+=1


a=10
while(a!=20):
    print(a)
    a+=1


n=26
while(n!=30):
    if(n==28):
        break
    print(n)
    n+=1


n=21
while(n!=24):
    if(n==24):
        break
    print(n)
    n+=1


s='jayashree'
for ch in s:
    if ch=='j':
        continue
    print(ch)
else:
    print('yash')


num=2
while(num!=7):
    if(num==5):
        num+=1
        continue
    print(num)
    num+=1
else:
    print('jai')

for i in range(5):
    print('hello world')
