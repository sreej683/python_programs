lst=[1,2,3,9]
new_lst=[num*10 for num in lst]
print(new_lst)


lst=[1,2,3,4]
new_lst=[num+10 for num in lst]
print(new_lst)


lst=[0,11,4,0,5,0,10,0,7,0]
final_lst=[num for num in lst if num!=0]+[num for num in lst if num==0]
print(final_lst)


lst=[2,9,3,8]
new_lst=[num for num in lst if num%2==0]
print(new_lst)


st1='mno'
st2='abc'
lst=[i+j for i in st1 for j in st2]
print(lst)



res=(num*2 for num in range(1,8))
print(res)
print(list(res))


st='jayashree'
d={ch:st.count(ch)for ch in st}
print(d)
