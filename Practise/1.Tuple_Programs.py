#Write a Python program to create a tuple with different data types.
t1=("P",True,1,12.3)
t1=tuple(t1)
print(t1)

# Write a Python program to create a tuple with numbers.

t1=(1,2,3)
t1=tuple(t1)
print(t1)

# Write a Python program to convert a tuple to a string.

t1=("a","b","c")
t2="".join(t1)
print(t2)

# Write a Python program to check whether an element exists within a tuple

t1=(1,2,3,4,5)
ele=7

if ele in t1:
    print("Exist")
else:
    print("Doesn't Exist")


# Write a Python program to find the length of a tuple.
t1=(1,2,3,4,5)
t2=len(t1)
print(t2)

print("----------------")

t1=(1,2,3,4,5)
count=0

for i in t1:
    count+=1
print(count)



# Write a Python program to convert a list to a tuple.

l1=[1,2,3]
l2=tuple(l1)
print(l2)


# Write a Python program to reverse a tuple.

t1=(1,2,3)
t2=tuple(reversed(t1))
print(t2)


print("--------------------")

t1=(1,2,3)
t2=t1[::-1]
print(t2)

# Write a Python program to replace last value of tuples in a list.

l1=[(1,2,3),(4,5,6)]

new=0

l1=([tup[:-1]+(new,)for tup in l1])
print(l1)


print("------------------")


new_list = []
for tup in l1:
    new_tup = tup[:-1] + (new,)
    new_list.append(new_tup)
l1 = new_list


# Write a Python program to find the repeated items of a tuple.

tup=(1,2,3,3,4,5,5,5)
s=()
for i in tup:
    count=tup.count(i)
    if count>1 and i not in s:
        print(i,":",count)
        s=s+(i,)

print("-----------------")


# Write a Python program to remove an empty tuple(s) from a list of tuples.


tup=[(1,2,3),(4,5,6),()]
tup=[i for i in tup if i!=()]
print(tup)

# Write a Python program to unzip a list of tuples into individual lists.

list1=[(1,2),(4,5),(10,12)]

list2=[i for i,j in list1]
list3=[j for i,j in list1]

print(list2)
print(list3)

# Write a Python program to convert a list of tuples into a dictionary.

l=[('x',1),('y',2),('z',3)]

d={}

for i,j in l:
    d.setdefault(i,[]).append(j)
print(d)

print("----------------------------")

l=[('x',1),('y',2),('z',3)]

d=dict(l)

print(d)



















































