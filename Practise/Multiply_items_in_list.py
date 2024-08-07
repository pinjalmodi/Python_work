#python program to multiply all the items in a list

from functools import reduce

l=[1,2,3,4,5]

s=reduce(lambda x,y:x*y, l)

print(s)

print("-------------------------")

l=[1,2,3,4,5]

s=1
for i in l:
    s=s*i

print(s)

print("---------------------------")


