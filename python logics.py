def string_ex(string):
    if(len(string)<2):
        return ' '
    return string[0:2]+string[-2:]
print(string_ex('jayashree'))


def sum(ele):
    sum_num=0
    for i in ele:
        sum_num+=i
    return sum_num
print(sum([1,2,3,4]))'''



#simple progrms:

'''l=[]
for i in range(2000,3201):
    if(i%7==0 and i%5!=0):
        l.append(i)
print(l)

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(8))

n=int(input("enter a number"))
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)

def generate_lst_tuple():
    input_str=input("enter values seperated by commas:")
    num_list=input_str.split(',')
    num_tuple=tuple(num_list)
    print('list:',num_list)
    print('tuple:',num_tuple)
generate_lst_tuple()

values=34,67,55,33,12,98
print('tuple:',tuple(values))
print('list:',list(values))


class strobj(object):
    def _init_(self):
        self.s=" "
    def getstring(self):
        self.s=input("enter a string")
    def printstring(self):
        print(self.upper)
obj=strobj()
obj=getstring()
obj=printstring()'''



'''class strprocessor:
    def _init_(self):
        self.input_str=None
    def getstring(self):
        self.input_str=input("enter a string:")
    def printstring(self):
        if self.input_str is not None:
            print(self.input_str.upper())
        else:
            print("nothing is provided")
def test_processor():
    obj=strprocessor()
    obj.getstring()
    obj.getstring()
test_processor()


class StringProcessor:
    def _init_(self):
        self.input_string = None

    def getString(self):
        """Gets a string from console input."""
        self.input_string = input("Enter a string: ")

    def printString(self):
        """Prints the string in upper case."""
        if self.input_string is not None:
            print(self.input_string.upper())
        else:
            print("No string input provided.")


def test_string_processor():
    """Tests the StringProcessor class methods."""
    processor = StringProcessor()
    processor.getString()
    processor.printString()


# Calling the test function
test_string_processor()


#Anagram

def anagram(str1,str2):
    str1=str1.replace(" "," ").lower()
    str2=str2.replace(" "," ").lower()
    return sorted(str1)==sorted(str2)
print(anagram('silent','listen'))


n=1
c=0
while(True):
    fc=0
    for fa in range(1,n+1):
        if(n%fa==0):
            fc+=1
    if(fc==2):
        print(n)
        c+=1
    n+=1
    if(c==5):
        break

s='jayashree'
for sv in range(len(s)):
    for ev in range(sv+1,len(s)+1):
        word=s[sv:ev]
        if word==word[::]


def reverse_str(st1):
    words=st1.split()
    rev=words[::-1]
    return ' '.join(rev)
st1='yash is good boy'
print(reverse_str(st1))


def sum_digit(num):
    d_sum=0
    for num in list:
        while(num!=0):n 
            d_sum+=num
            num//=10
    return d_sum
lst=[1,2,3,4,5]
print(max(list,key=sum_digit))


l=[]
for i in range(2000,3200):
    if(i%7==0) and (i%5!=0):
        l.append(str(i))
print(','.join(l))


def fact(n):
    if(n==1)or(n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(8))'''
