def add(a,b):
    return a+b
print(add(2,3))

wish=lambda:'hi lasya'
print(wish())


list=[2222,111,44,9]
print(sorted(list,key=lambda num:list.count(num)))

s='lasya'
print(max(s))

list=[212,115,313,21,510]
print(sorted(list,key=lambda num:num%10))


st='we are students'
list=st.split()
print(sorted(st.split(),key=lambda word=[len(word),word]))
print(''.join(list))

list=[12,9,24,10]
print(min(list,key=lambda num:num/10))

lst=['lasya','is','good','girl']
m=list(map(len,lst))
print(m)

m=list(map(lambda num:num+10,range(2,9)))
print(m)
