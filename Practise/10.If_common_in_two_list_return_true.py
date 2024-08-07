#Write a Python function that takes two lists and returns True if they have at least one common member.

l=[1,2,3,4,5]
l2=[1,6,8,9,4]

if any(i in l2 for i in l):
    print("True")

print("---------------")

l=[1,2,3,4,5]
l2=[1,6,8,9,4]
result= False

for i in l:
    for j in l2:
        if(i==j):
            result=True
print(result)
