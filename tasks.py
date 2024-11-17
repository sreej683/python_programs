'''#number of vowels and consonats in a string:

def count_vowels_consonants(string):
    vowels='aeiouAEIOU'
    vowels_count=sum(1 for char in string if char in vowels)
    consonants_count=sum(1 for char in string if char.isalpha() and char not in vowels)
    return vowels_count, consonants_count
string=input("enter a string:")
vowels,consonants=count_vowels_consonants(string)
print (f"Vowels:{vowels}")
print (f"Consonants:{consonants}")

#program to check string is palindrome or not:

def revstr(string):
    if string==string[::-1]:
        return 'palindrome'
    else:
        return 'not palindrome'
string='madam'
print(revstr(string))


#program to remove duplicates in a string:

def removeduplicates(string):
    new_str=''
    for chr in string:
        if chr not in new_str:
            new_str+=chr
    return new_str
string='jayashree'
print(removeduplicates(string))


#Armstrong number:
num=153
copy=num
dsum=0
count=len(str(num))
while(num!=0):
    ld=num%10
    dsum+=ld**count
    num//=10
print('armstrong'if(dsum==copy)else 'not armstrong')


#Palindrome:

num=222
copy=num
rev=0
while(num!=0):
    ld=num%10
    rev=rev*10+ld
    num//=10
print('Palindrome'if(copy==rev)else 'not palindrome')


#sum of digits:

def sum_digit(num):
    if num==0:
        return 0
    else:
        return(num%10)+sum_digit(num//10)
print(sum_digit(18))


#fibonacci series:

def fibonacci(num):
    fib_seq=[0,1]
    while(len(fib_seq))<num:
          fib_seq.append(fib_seq[-1]+fib_seq[-2])
    return fib_seq
print(fibonacci(12))


#number pattern:

num=1
for lines in range(1,5):
    for col in range(lines):
        print(num,end='')
        num+=1
    print()


#mutiplication table:

n=5
for i in range(1,11):
    print(n,'*',i,'=',n*i)

#factorial of number 5:

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#prime number:

num=2
fcount=0
for fa in range(1,num+1):
    if num%fa==0:
        fcount+=1
print('prime'if(fcount==2)else 'not prime')

#list containing squares of 1-10:

squares=[i**2 for i in range(1,11)]
print(squares)

cubes=[i**3 for i in range(1,11)]
print(cubes)


#character count:

def print_chr_count(string):
    char_count={}
    for char in string:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
        for char,count in char_count.items():
            print(f"character:{char},count:{count}")
string="hello"
print(print_chr_count(string))


#list comprehension:

strings=['Hello','yash','JAYASREE']
uppercase_letters=[char for string in strings for char in string if char.isupper()]
print(uppercase_letters)

strings=['YASh']
lower_case=[char for string in strings for char in string if char.islower()]
print(lower_case)


#finding second smallest and third largest numbers in list:

def find_numbers(num_list):
    unique_list=sorted(set(num_list))
    if len(unique_list)<3:
        return "list must have atleast 3 unique elements"
    second_smallest=unique_list[1]
    third_largest=unique_list[-3]
    return second_smallest,third_largest
numbers=[12,45,7,23,56,89,34,1,6,8]
second_smallest,third_largest=find_numbers(numbers)
print(f"second smallest number:{second_smallest}")
print(f"third largest number:{third_largest}")


#program to reverse a string:

def reverse_string(string):
    return string[::-1]
print(reverse_string('jayashree'))

#program to remove duplicates:

arr=[1,2,3,2,3,4,3]
unique_arr=list(set(arr))
print(unique_arr)'''

#simple calculator operations using functions:

def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y==0:
        return error

    












    
    

