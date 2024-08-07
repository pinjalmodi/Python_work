 #Write a Python program to create a tuple.

t=tuple((1,2,3,4,5,6))
print(t)

#Tuple with different data types

t=tuple(("Tuple",False,12.3,2))
print(t)

print("-------------------------")

p = 5, 10, 15, 20, 25
print(p)


#Write a Python program to unpack a tuple into several variables.
t=(1,2,3,4,5)

a,b,c,d,e=t

print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)
print("e:",e)

# Write a Python program to add an item to a tuple.then add 3 items to it then output should be first 5 digits and last five digit same with middle value of new tuple

tup=(1,2,3,4,5)

tup=tup+(6,)
print(tup)

tup=tup[:5]+(10,20,30)+tup[:5]

print(tup)

# Write a Python program to convert a tuple to a string.

tup=("P","I","N","J","A","L")

s=' '.join(tup)

print(s)

#First and last 4th element to print

tup=(1,2,3,4,5,6,7,8)

t1=tup[4]
t2=tup[-4]

print(t1)
print(t2)


#Print colon ... Create a tuple with a list as element and add value to that list


from copy import deepcopy

t=("H",2,[],True)

t1=deepcopy(t)

t1[2].append(50)

print(t)
print(t1)

print("--------------------------------")

#Write a Python program to find repeated items in a tuple.

t=(1,2,3,4,1,2,6,7,5)

frequency={}

for i in t:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
        
repeated_v=[i for i,count in frequency.items() if count>1]

print(t)
print(repeated_v)


#Write a Python program to check whether an element exists within a tuple.

n=int(input("Enter N"))

t=(1,2,3,4,5,6)

result=False
for i in t:
    if n in t:
        result=True
    else:
        result=False
if result==True:
    print("Exist")


print("-------------------------")

tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print("r" in tuplex)
print(5 in tuplex)


#Convert a list to a tuple

l1=[1,2,3,4,5]

t1=tuple(l1)

print(t1)

#Write a Python program to remove an item from a tuple

tup="P","i","n","j","a","l"
print(tup)

tup=tup[:2]+tup[3:]
print(tup)

print("-----------------------")
l1=list(tup)
l1.remove("l")
t1=tuple(l1)
print(t1)


#Write a Python program to find the index of an item in a tuple.
tup=tuple("index tuple")

print(tup)

i=tup.index("p")
print(i)

#Write a Python program to find the length of a tuple.
tup=("Pinjal")
t1=len(tup)
print(t1)


# Write a Python program to convert a tuple to a dictionary.
tuplex = ((2, "w"), (3, "r"))
result_dict = dict((y, x) for x, y in tuplex)
print(result_dict)

#Write a Python program to unzip a list of tuples into individual lists.
l = [(1, 2), (3, 4), (8, 9)]
result = list(zip(*l))
print(result)

# Write a Python program to reverse a tuple.
x = ("w3resource")
y = reversed(x)
print(tuple(y))

x = (5, 10, 15, 20)
y = reversed(x)
print(tuple(y))


#Write a Python program to convert a list of tuples into a dictionary.
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print(d)

# Write a Python program to print a tuple with string formatting.
#Sample tuple : (100, 200, 300)
#Output : This is a tuple (100, 200, 300)

t = (100, 200, 300)
print('This is a tuple {0}'.format(t))


#Replace last value of tuples in a list
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])



#Remove an empty tuple(s) from a list of tuples
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)


#Write a Python program to sort a tuple by its float element.
#Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
#Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sorted_price = sorted(price, key=lambda x: float(x[1]), reverse=True)

print(sorted_price)


















































































































































