# Write a Python program to convert a list of tuples into a dictionary.
t1=[(1,2),(4,5),(7,8)]
t1=dict(t1)
print(t1)
print("--------------------")
l=[('x',1),('y',2),('z',3)]

d={}#Wrong

for i,j in l:
    d.setdefault(i,[]).append(j)
print(d)

print("--------------------")
l=[('x',1),('y',2),('z',3)]
d={}
for i,j in l:
    d.setdefault(i,j)
print(d)

#Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1, 'elderberry': 6}

# Sort dictionary by value in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted dictionary by value in ascending order:")
print(sorted_dict_asc)

# Sort dictionary by value in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("\nSorted dictionary by value in descending order:")
print(sorted_dict_desc)

#Write a Python script to concatenate following dictionaries to create a new one
d1={1:2,2:3,3:4}
d2={4:5,5:6,6:7}
d3={ }
for d in (d1,d2):
    d3.update(d)
print(d3)


print("------------")

#Write a Python script to check if a given key already exists in a dictionary
d1={1:2,2:3,3:4}
k=5

if k in d1:
    print("Exist")
else:
    print("Doesnot Exist")

    
#Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
d={}

for i in range(1,15+1):
    d[i]=None
print(d)

# Write a Python program to check multiple keys exists in a dictionary

d1={1:2,2:3,3:4}

k=1,7

for i in k:
    if i in d1:
        print("Exist")
    else:
        print("Doesnot exist")


# Write a Python script to merge two Python dictionaries

d={1:2,3:4}
l={4:5,5:6}
p={}
p=d.copy()
p.update(l)
print(p)


d1={1:2,2:3,3:4}
d2={4:5,5:6,6:7}
d3={ }
for d in (d1,d2):
    d3.update(d)
print(d3)


# Write a Python program to map two lists into a dictionary

k=[1,2,3]
p=["A","B","C"]

d=dict(zip(k,p))
print(d)

#Write a Python program to combine two dictionary adding values for
#common keys.
#d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
#Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,'d':400}


d=Counter(d1)+Counter(d2)

print(d)

#Write a Python program to print all unique values in a dictionary.

d={1:2,1:3,2:2,2:3,3:4,3:5}

d1={}
for i,j in d.items():
    if i not in d1:
        d1[i]=j
print(d1)


#Write a Python program to create and display all combinations of letters,
#selecting each letter from a different key in a dictionary.
#Sample data: {'1': ['a','b'], '2': ['c','d']}
#Expected Output:
#ac ad bc bd

from itertools import product

d={'1':['a','b','c'],'2':['c','d','a']}

for x,y in product(*d.values()):
    print(x+y)

print("--------------------------------------------")

import itertools

# Define the dictionary with letters
letter_dict = {
    'key1': ['a', 'b', 'c'],
    'key2': ['d', 'e', 'f'],
    'key3': ['g', 'h', 'i']
}

# Get the values from the dictionary as a list of lists
letter_lists = list(letter_dict.values())

# Use itertools.product to create all combinations of letters
combinations = itertools.product(*letter_lists)

# Display the combinations
for combination in combinations:
    print(''.join(combination))



# Write a Python program to find the highest 3 values in a dictionary

d={'a':32,'b':45,'c':12,'d':89}

values=list(d.values())

values.sort(reverse=True)

print(values[:3])

#Write a Python program to combine values in python list of dictionaries.
#Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
#300}, o {'item': 'item1', 'amount': 750}]
#Expected Output:
#Counter ({'item1': 1150, 'item2': 300})
from collections import Counter

l1=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, {'item': 'item1', 'amount': 750}]

result=Counter()

for d in l1:
      result[d['item']]=result[d['item']]+d['amount']
print(result)



#Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string: 'w3resource'
#Expected output:
#{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

from collections import defaultdict,Counter
s1='w3resource'
d={}

for i in s1:
    d[i]=d.get(i,0)+1
print(d)






































































