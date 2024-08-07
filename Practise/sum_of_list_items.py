#Write a  Python program to sum all the items in a list.

l=[1,2,3,4.5,6]

s=sum(l)
print("Sum is:",s)


print("------------------")

l=[1,2,3,4.5,6]
s=0

for i in l:
    s=s+i
print(s)

print("---------------------")

from functools import reduce

l=[1,2,3,4,5]
s= reduce(lambda x,y:x+y , l)
print(s)
