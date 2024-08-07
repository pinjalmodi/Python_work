#1. Write a Python script to sort (ascending and descending) a dictionary by value.

import operator
d={1:4,4:0,5:1,6:8}

sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1)))
print(sorted_d)


sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print(sorted_d)

#2. Write a Python script to add a key to a dictionary.

#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}


d={0: 10, 1: 20}

d.update({2:30})

print(d)

# Write a Python script to concatenate the following dictionaries to create a new one.

#Sample Dictionary :
#dic1={1:10, 2:20}
#ic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic4 = {}

for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)

#Write a Python script to check whether a given key already exists in a dictionary.
d1={1:10,2:20,3:30}
n=1

if n in d1:
    print("Exist")
else:
    print("Does not Exist")

#Write a Python program to iterate over dictionaries using for loops.

d = {'x': 10, 'y': 20, 'z': 30}

for dict_key, dict_value in d.items():
    print(dict_key, '->', dict_value)	
#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n=int(input("Enter N"))
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)

#PRINT 1 TO 15 WITH SQUARE AS Value
d={}
for i in range(1,15+1):
    d[i]=i*i
print(d)

#Write a Python script to merge two Python dictionaries.
d1={1:1,2:2,3:3}
d2={4:4,5:5}

d1.update(d2)
#d = d1.copy()

#d.update(d2)
#print(d) 

print(d1)


#Write a  Python program to iterate over dictionaries using for loops.

d = {'Red': 1, 'Green': 2, 'Blue': 3}

for color_key, value in d.items():
    print(color_key, 'corresponds to ', d[color_key])



# Write a Python program to sum all the items in a dictionary.
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
result = sum(my_dict.values())
print(result)

# Write a Python program to multiply all the items in a dictionary.

d3={2:1,6:2,3:3,4:4,5:5}

result=1

for values in d3:
    result=result*d3[values]
print(result)

print("----------------------")

import math

d3 = {5: 5, 3: 3, 4: 4}

result = math.prod(d3.values())
print(result)


#Write a Python program to remove a key from a dictionary.


myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
if 'a' in myDict:
    del myDict['a']
print(myDict)



#Write a Python program to map two lists into a dictionary.
k=[1,2,3]
v=[4,5,6]

d=dict(zip(k,v))
print(d)

# Write a Python program to sort a given dictionary by key.

a={5:2,3:1,6:2}

for key in sorted(a):
    print(key,a[key])

#15. Write a Python program to get the maximum and minimum values of a dictionary.
my_dict = {'x': 500, 'y': 5874, 'z': 560}
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
print('Maximum Value: ', my_dict[key_max])
print('Minimum Value: ', my_dict[key_min])



































































































