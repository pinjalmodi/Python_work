#Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
list1=  ['abc', 'xyz', 'aba', '1221']
cot=0
for i in list1:
    if len(i)>=2 and i[0] == i[-1]:
        cot=cot+1
print(cot)
