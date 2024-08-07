
import random

#print(random.randint(1,100))

data=open("data.txt","w")
for i in range(10):
    data.write(str(random.randint(1,100))+",")
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")

l=data.read().split(",")[:-1]
for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")
data.close()
even.close()
odd.close()

print("Data File Content")
data=open("data.txt","r")
print(data.read())
data.close()


print("Even File Content")
data=open("even.txt","r")
print(data.read())
data.close()

print("Odd File Content")
data=open("odd.txt","r")
print(data.read())
data.close()
