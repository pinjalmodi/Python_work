s="abcd"
p=len(s)
print(p)

print("--------------------")

s="abcd"
count=0
for i in s:
    count+=1
print(count)
        
print("-----------------------")

#Write a Python program to count the number of characters (character
#frequency) in a string

s="abcdab"
p={ }
for i in s:
    if i in p:
        p[i]=p[i]+1
    else:
        p[i]=1
print("Total characters",p)


# Write a Python program to count occurrences of a substring in a string.
s="abcxyzxyz"
sub="xyz"
print(s.count(sub))

#Write a Python program to count the occurrences of each word in a given sentence
import re
s="This is me"
word=r'\w+'
substring=re.findall(word,s)
print("Words are",len(substring))


#Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.

a="Pinjal"
b="Modi"

x=b[:2]+a[2:]
y=a[:2]+b[2:]

print(x," ",y)

#Write a Python program to add 'ing' at the end of a given string (length
#should be at least 3). If the given string already ends with 'ing' then add
#'ly' instead if the string length of the given string is less than 3, leave it
#unchanged.

a="Pinjaling"

if len(a)>=3 and a.endswith('ing')==False:
    print(a+'ing')
elif a.endswith('ing')==True:
    print(a+'ly')

else:
    print(a)

#Write a Python program to find the first appearance of the substring
#'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
#whole 'not'...'poor' substring with 'good'. Return the resulting string.
"""
p="This poor lession is not interesting"

b1=p.find("poor")
c1=p.find("not")

if (b1>c1) and (b1>0) and (c1>0):
    p=p.replace(p[c1:(b1+4)],'good')
    print(p)"""

#Write a Python function that takes a list of words and returns the length
#of the longest one.

    
























