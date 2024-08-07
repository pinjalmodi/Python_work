#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

tuples_list = [(1, 3), (3, 1), (2, 2), (4, 4), (5, 0)]

sorted_tup = sorted(tuples_list,key=lambda x:x[-1])

print(sorted_tup)

print("--------------------")

l=[3,4,2]

so=sorted(l,key=lambda x:x[-1])

print(so)
