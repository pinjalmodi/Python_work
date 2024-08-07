# Write a Python program to find the list of words that are longer than n from a given list of words.
l=["Pinjal","Hetal","Hiya","Megha","Mona"]
n=int(input("Enter n"))


for i in l:
    if len(str(i))>n:
        print("Longer words",i)

print("--------------------------")

l=["This flower is beautiful"]
n=int(input("Enter n"))
l=l[0].split( )

for i in l:
    if len(str(i))>n:
        print("Longer words",i)
