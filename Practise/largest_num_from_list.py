#3. Write a Python program to get the largest number from a list.


l=[1,2,3,5,4]

maxI=l[0]

for i in l:
    if i>maxI:
        maxI=i
print(maxI)


print("---------------")

l=[1,2,3,5,4]

s=sorted(l)
print (s[-1])

print("-----------------------")

l=[1,2,3,5,4]
print(max(l))

