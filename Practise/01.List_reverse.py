#Reverse a list

l1=[1,2,3,4,5]
print(list(reversed(l1)))

print(l1[::-1])


print("-----------------------")

#Remove last object from a list

l1=[1,2,3,4,5]
l1.pop()
print(l1)

del l1[-1]
print(l1)


l1 = [1, 2, 3, 4, 5]
l2 = l1[:-1]
print(l1)  # prints: [1, 2, 3, 4, 5]
print(l2)  # prints: [1, 2, 3, 4]

print("--------------------------------")

#Difference between append and extend
l1=[1,2,3,4,5]

l1.append(6)

print(l1)


l2=[10,20,30]

l1.extend(l2)

print(l1)

print("---------------------------------")

#Write a Python function to get the largest number, smallest num and sum
#of all from a list

l1=[1,2,3,4,5,6]

max=l1[0]
min=l1[1]
sum=0

for i in l1:
    if i>max:
        max=i
    elif i<min:
        min=i
    sum=sum+i
print(max)
print(min)
print(sum)

#Write a function

def longe(l1):
    max=l1[0]
    min=l1[0]
    sum=0
    

    for i in l1:
        if i>max:
            max=i
        elif i<min:
            min=i
        sum=sum+i
    return max,min,sum
print(longe([1,2,3,4,5]))
    

#Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character are same from a given
#list of strings.

l1=['abc','abc','abcab','pqrpq']
count=0
for i in l1:
    if len(i)>=2 and i[:2]==i[-2:]:
        count=count+1
print(count)
        

#Write a Python program to remove duplicates from a list.
l4=[]
l3=[1,2,3,4,5,1,2,3]
for i in l3:
    if i not in l4:
        l4.append(i)
print(l4)

print("--------------------------")

p=[1,2,3,4,1,2]
l=list(dict.fromkeys(p))
print(l)

print("-------------------")

l1=[1,2,3,4,1,2,3]
l1=list(set(l1))
print(l1)

# Write a Python program to check a list is empty or not.


l1=[1,2]
if not l1:
    print("Empty")
else:
    print("Not Empty")



l1 = []
if len(l1) == 0:
    print("Empty")
else:
    print("Not Empty")

#Write a Python function that takes two lists and returns true if they have
#at least one common member.
def comm(list1,list2):


    for i in list1:
        for j in list2:
            if i==j:
                return True
print(comm([1,2],[1,2,3]))
    
    
#Write a Python program to generate and print a list of first and last 5
#elements where the values are square of numbers between 1 and 30.
x=[]
for i in range (1,31):
    x.append(i*i)
print(x[:5],x[-5:])

#Write a Python function that takes a list and returns a new list with unique
#elements of the first list.

def newlist(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2
print(newlist([1,2,3,1,2,3]))

#Write a Python program to convert a list of characters into a string.
l=["a","b","c"]
l1="".join(l)
print(l1)

#Write a Python program to select an item randomly from a list.
import random
l1=[1,2,3,4,5]

print(random.choice(l1))

#Write a Python program to find the second smallest number in a list.

h=[1,2,3,4,5]

max=h[0]
second_max=h[0]

for i in h:
    if i>max:
        second_max=max
        max=i
        
    elif i>second_max and i!=max:
        second_max=i
    print(second_max)

#Write a Python program to check whether a list contains a sub list

list1=[1,2,3,4,5,6]
sub_list=[2,3,4,6,7]

for i in range(len(list1)-len(sub_list)+1):
    if list1[i:i+len(sub_list)]==sub_list:
        print("True")
        break
    else:
        print("False")
        break
print("--------------------")

#Write a Python program to split a list into different variables.


list1=[1,2,3]
a,b,c=list1

print("A:",a)
print("B:",b)
print("C:",c)






































