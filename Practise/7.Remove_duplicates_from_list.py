#7. Write a Python program to remove duplicates from a list.
l=[1,2,3,4,1,2,3,4]
p=[]
for i in l:
    if i not in p:
        p.append(i)
print(p)
print(l)

print("--------------------------")

test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The original list is:", test_list)
test_list = list(set(test_list))
print("The list after removing duplicates:", test_list)

print("---------------------------------")

test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The original list is:", test_list)
seen = set()
test_list = [x for x in test_list if x not in seen and not seen.add(x)]
print("The list after removing duplicates:", test_list)

print("------------------------------------------")
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The original list is:", test_list)
seen = set()
new_list = []
for x in test_list:
    if x not in seen:
        new_list.append(x)
        seen.add(x)
test_list = new_list
