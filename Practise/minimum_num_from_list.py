#Write a Python program to get the smallest number from a list.

l=[1,2,3,5,4]

mINI=l[0]

for i in l:
    if i<mINI:
        mINI=i
print(mINI)


print("---------------")

l=[1,2,3,5,4]

s=sorted(l)
print (s[0])

print("-----------------------")

l=[1,2,3,5,4]
print(min(l))
