class student:
    course_name='python'
    trainer='lasya'
    batch=10
s1=student()
s2=student()
s3=student()
print(s1.trainer)
print(s2.course_name)
print(s3.batch)
print(student.trainer)


class student:
    course_name='python'
    trainer='lasya'
    batch=10
    def _init_(self,name,age,mno):
        self.name=name
        self.age=age
        self.mno=mno
s1=student('jai',22,9121685526)
s2=student('yash',22,9643562867)
print(s1.name)
print(s2.name)


class subject:
    subject_name='english'
    subject_faculty='Abhinav'
    def _init_(self,sname,sage,smno,sid):
        self.sname=sname
        self.sage=sage
        self.smno=smno
        self.sid=sid
s1=subject('lasya',22,9121685526,1)
s2=subject('akarsh',23,786956567,2)
s3=subject('yash',22,9675456789,3)
print(s1.sage)
print(s2.sid)
print(s3.sname)

class sample:
    def m1(self):
        print('object method is called')
    @classmethod
    def m2(cls):
        print('class method is called')
    @staticmethod
    def m3():
        print('static method is called')
s1=sample()
s1.m1()
sample.m1(s1)
s1.m2()
sample.m2()
s1.m3()
sample.m3()


class bank:
    bank_name='state'
    branch_name='pgr'
    ifsc=897654345678
    roi=10
    def _init_(self,name,accno,mno,balance,pin):
        self.name=name
        self.accno=accno
        self.mno=mno
        self.balance=balance
        self.pin=pin
b=bank('lasya',876789543256,9121685526,9000,9967)
print(b.name)
print(b.mno)
print(b.balance)
print(b.accno)
print(b.pin)


class sample:
    def _init_(self):
        print('object is created')
    @classmethod
    def create_object(cls):
        return cls()
s1=sample.create_object()
s2=sample.create_object()

class sample:
    def _init_(self,name,age,mno):
        self.name=name
        self.age=age
        self.mno=mno
    @classmethod
    def create_object(cls,*args):
        value=args[0].split()
        val1=value[0]
        val2=int(value[1])
        val3=int(value[2])
        return cls(val1,val2,val3)
s1=sample.create_object('yash',22,9121685526)
print(s1)


class abc:
    def _init_(self):
        print('init is called')
    def _del_(self):
        print('del is called')
    def __str_(self):
        return 'lasya...'
s1=abc()


class sample:
    def _init_(self):
        self.__x=10
s1=sample()
print(s1.__x)



class sample:
    def _init_(self):
        self.__x=90
    def getter(self):
        return self.__x
    def setter(self):
        self.__x=int(input('enter a number'))
s1=sample()
print(s1.getter())
s1.setter()
print(s1.getter())


class whatsup_v1:
    def chatting(self):
        print('photos')
        print('text')
class whatsup_v2(whatsup_v1):
    def chatting(self):
        super().chatting()
        print('documents')
        print('files')
class whatsup_v3(whatsup_v2):
    def call(self):
        print('audio call')
class whatsup_v4(whatsup_v3):
    def call(self):
        super().call()
        print('video call')
obj=whatsup_v4()
obj.call()
obj=whatsup_v1()
obj.chatting()


class database_1:
    def _init_(self,name,mno):
        self.name=name
        self.mno=mno
class database_2(database_1):
    def _init_(self,name,mno,mail,aadhar):
        super()._init_(name,mno)
        self.mail=mail
        self.aadhar=aadhar
class database_3(database_2):
    def _init_(self,name,mno,mail,aadhar,pan):
        super()._init_(name,mno,mail,aadhar)
        self.pan=pan
d=database_3('lasya',9121685526,'sreej683@gmail.com',897654345678,'PAN897643')
print(d.name)
print(d.mno)


class v1:
    def _init_(self,x):
        self.x=x
class v2(v1):
    def _init_(self,x,y):
        super()._init_(x)
        self.y=y
class v3(v2):
    def _init_(self,x,y,z):
        super()._init_(x,y)
        self.z=z
obj=v3(10,9,2)
print(obj.x,obj.y,obj.z)


class father:
    def _init_(self,fname,fage):
        self.fname
        self.fage
class mother(father):
    def _init_(self,mname,mage):
        super().__init(fname,fage)
        self.mname=mname
        self.mage=mage
class child(father,mother):
    def __init(self,cname,cage,fname,fage,mname,mage):
        super()._init_(fname,fage)
        mother._init_(self,mname,mage)
        self.cname=cname
        self.cage=cage
c=child('lasya',9,'abhinav',27,'bhoomi',25)
print(c.cname,c.fname,c.mname)

class student_v1:
    def behaviour(self):
        print('lasya is good girl')
        print('yash is intelligent')
class student_v2(student_v1):
    def behaviour(self):
        print('abhinav is great')
        print('we are best frnd')
s=student_v1()
s.behaviour()
s=student_v2()
s.behaviour()


class sample:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
    def add(self,a,b,c,d):
        return a+b+c+d
s=sample()
print(s.add(1,2))
print(s.add(2,3,4))
print(s.add(4,5,4,5))

class sample:
    def add(self,a=0,b=0,c=0,d=0):
        return a+b+c+d
s=sample()
print(s.add(2,3))
print(s.add(3,4,5))
print(s.add(4,7,8))


from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class dog:
    def speak(self):
        print('bow bow')
class cat:
    def speak(self):
        print('meow meow')
d=dog()
c=cat()
d.speak()
c.speak()

class abc:
    def _init_(self,x):
        self.x=x
    def _add_(self,other):
        return self.x+other.x
    def _sub_(self,other):
        return self.x-other.x
    def _mul_(self,other):
        return self.x*other.x
a1=abc(10)
a2=abc(8)
print(a1+a2)
print(a1-a2)
print(a1*a2)


def outer():
    a=20
    print(f'non local:{a}')
    def inner():
        a=30
        print(f'local:{a}')
    inner()
    print(f'nonlocal:{a}')
a=10
outer()
print(f'global:{a}')



def outer():
    a=20
    print(f'non local:{a}')
    def inner():
        global a
        a=30
        print(f'local{a}')
    inner()
    print(f'non local{a}')
a=10
outer()
print(f'global{a}')



def outer():
    a=20
    print(f'non local:{a}')
    def inner():
        nonlocal a
        a=30
        print(f'local:{a}')
    inner()
    print(f'global:{a}')
a=10
outer()
print(f'non local:{a}')
