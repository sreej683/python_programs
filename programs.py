'''def prime(num):
    fcount=0
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount==2
def primes(n):
    l=[]
    while len(l)<=10:
        if prime(n):
            l.append(n)
        n+=1
    return l
print(primes(1))


def composite(num):
    fcount=0
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount>2
def composites(n):
    l=[]
    while len(l)<=10:
        if composite(n):
            l.append(n)
        n+=1
    return l
print(composites(1))



def palindrome(num):
    copy=num
    rev=0
    while(num!=0):
        ld=num%10
        rev=rev*10+ld
        num//=10
    return copy==rev
def palindromes(n):
    l=[]
    while len(l)<=10:
        if palindrome(n):
            l.append(n)
        n+=1
    return l
print(palindromes(1))



def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

n=5
for row in range(1,n+1):
    for col in range(1,row):
        print('*',end='')
    print()


n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col:
            print('*',end='')
        else:
            print(' ',end='')
    print()


n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col==n+1:
            print('*',end='')
        else:
            print(' ',end='')
    print()



n=5
for n in range(1,n+1):
    print('*'*n)


def niven(num):
    copy=num
    dsum=0
    while(num!=0):
        ld=num%10
        dsum+=ld
        num//=10
    return copy%dsum
def nivens(n):
    l=[]
    while len(l)<=10:
        if niven(n):
            l.append(n)
        n+=1
    return l
print(nivens(1))

def spy(num):
    dsum=0
    dproduct=1
    while(num!=0):
        ld=num%10
        dsum+=ld
        dproduct*=ld
        num//=10
    return dsum==dproduct
def sp(n):
    l=[]
    while len(l)<=10:
        if spy(n):
            l.append(n)
        n+=1
    return l
print(sp(1))


def automorphic(num):
    square=num**2
    count=len(str(num))
    rem=square%(10**count)
    return num==rem
def auto(n):
    l=[]
    while len(l)<=10:
        if automorphic(n):
            l.append(n)
        n+=1
    return l
print(auto(1))


def trimorphic(num):
    cube=num**3
    count=len(str(num))
    rem=cube%(10**count)
    return num==rem
def tri(n):
    l=[]
    while len(l)<=10:
        if trimorphic(n):
            l.append(n)
        n+=1
    return l
print(tri(10))



def neon(num):
    square=num**2
    dsum=0
    while(square!=0):
        ld=square%10
        dsum+=ld
        square//=10
    return num==dsum
def neons(n):
    l=[]
    while len(l)<=10:
        if neon(n):
            l.append(n)
        n+=1
    return l
print(neons(9))


def armstrong(num):
    copy=num
    count=len(str(num))
    dsum=0
    while(num!=0):
        ld=num%10
        dsum+=ld**count
        num//=10
    return copy==dsum
def arm(n):
    l=[]
    while len(l)<=10:
        if armstrong(n):
            l.append(n)
        n+=1
    return l
print(arm(1))

def str(string):
    if string==string[::-1]:
        return 'palindrome'
    else:
        return 'not a palidrome'
string='madam'
print(str(string))


s='jayashree'
for sv in range(len(s)):
    for ev in range(sv+1,len(s)+1):
        word=s[sv:ev]
        if word==word[::-1]:
            print(word)

def revstr(str):
    words=str.split()
    rev=words[::-1]
    return ' '.join(rev)
str='lasya is good girl'
print(revstr(str))


def sum_digit(num):
    if num==0:
        return 0
    else:
        return num%10+sum_digit(num//10)
list=[12,3,45,6,99]
print(max(list,key=sum_digit))


str='hello world'
ns=''
for ch in str:
    if 'a'<=ch<='z':
        if ch in 'aeiou':
            ns+=ch
        else:
            ns+='@'
    else:
        ns+=ch
print(ns)


str='jayashree'
for ind in range(len(str),0,-1):
    print(str[ind:]+str[:ind])



str='hello'
count=0
for ch in str:
    count+=1
print(count)


str='lasya is good girl'
lst=str.split()
print(' '.join(map(lambda word:word[::-1],lst)))


wish=lambda:'hi'
print(wish())


lst=[23,5,6,99]
print(max(lst,key=lambda num:num%10))

st='lasya is very cool'
lst=st.split()
print(sorted(st.split(),key=lambda word:[len(word),word]))
print(' '.join(lst))


lst=[2,4,5,9,3]
new_lst=[num*10 for num in lst]
print(new_lst)


lst=[2,4,5,9,3]
new_lst=[num for num in lst if num%2==0]
print(new_lst)


lst=[0,11,4,0,5,0,10,0,7,0]
new_lst=[num for num in lst if num!=0]+[num for num in lst if num==0]
print(new_lst)


res=(num*2 for num in range(1,7))
print(res)
print(list(res))


class student:
    course_name='python'
    branch='marathahalli'
    trainer='yash'
s1=student()
s2=student()
s3=student()
print(s1.course_name)
print(s1.trainer)
print(student.trainer)


class student:
    course='python'
    trainer='yashu'
    branch='btm'
    def __init__(self,name,sid,age):
        self.name=name
        self.sid=sid
        self.age=age
s1=student('yash',1,22)
s2=student('jai',2,22)
print(s2.name)


#constructor:

class sample:
    def m1(self):
        print('object method is called')
    @classmethod
    def m2(cls):
        print('class method is called')
    @staticmethod
    def m3():
        print('static method is called')
s=sample()
s.m1()
s.m2()
s.m3()


class bank:
    bank_name='sbi'
    brach_name='pgr'
    roi=10
    def __init__(self,name,accno,mno,balance,pin):
        self.name=name
        self.accno=accno
        self.mno=mno
        self.balance=balance
        self.pin=pin
s1=bank('yash',289765432456,9121685526,1000,9999)
print(s1.name)
print(s1.balance)
print(s1.pin)


class sample:
    def __init__(self):
        print('object method is created')
    @classmethod
    def create_object(cls):
        return cls
s1=sample()
s2=sample()


num=1234
words=['one','two','three','four','five','six','seven','eight','nine']
new=''
num=str(num)
for i in num:
    new+=words[ord(i)-ord('0')]+""
print(new)

num=9121685526
while(num!=0):
    fcount=0
    ld=num%10
    num//=10
    for fa in range(1,ld+1):
        if(ld%fa==0):
            fcount+=1
    if(fcount==2):
        print(ld)'''


















        
    









    
