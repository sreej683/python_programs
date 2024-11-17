import re
s='We are waiting for the food'
re.match('we',s)
print(re.match('we',s))

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

import re
txt="The rain in spain"
x=re.findall("[a-m]",txt)
print(x)

import re
txt="The rain in spain"
x=re.findall("[A-M]",txt)
print(x)

import re
txt="There are 99 dollars"
x=re.findall("\d",txt)
print(x)

import re
txt="yash is intelligent"
x=re.findall("y...",txt)
print(x)

import re
txt="Yash and lasya are frnds"
x=re.findall("^Y",txt)
if x:
    print("The string is starting with Y")
else:
    print("not matching")

import re
txt="Lasya is good girl"
x=re.findall("girl$",txt)
if x:
    print("The string is ending with girl")
else:
    print("not matching")


import re
txt="hello yash"
x=re.findall("he.*h",txt)
print(x)

import re
txt="hello yashshree"
x=re.findall("ya.*e",txt)
print(x)

import re
txt="hello everyone"
x=re.findall("he.+l",txt)
print(x)


import re
txt="hello planet"
x=re.findall("he.?o", txt)
print(x)
