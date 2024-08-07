
for i in range(1,6):
    print(" "*(5-i)+" ".join(str(j) for j in range(1,i+1)))
    
print("--------------------------")


for i in range (1,6):
    for j in range((5-i),0,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()

print("-----------------------------")

for i in range(1,6):
    print(" "*(5-i)+(str(j)*j))
    str(j)==1
    j=j+1

print("-----------------")
j=1
for i in range(65,72):
    print(" "*(9-j),chr(i)*j)
    j=j+1
print("-----------------")

j=1
j=str(j)
for i in range(1,10):
    print(" "*(9-i),j*i)
    j=int(j)+1
    j=str(j)
print("----------------")

j=1
j=str(j)
for i in range(1,10):
    print(" "*(9-i),f" {j}"*i)
    j=int(j)+1
    j=str(j)
print("------------------------")
j=1
for i in range(1,6):
    print(str(j)*(i))
    j=j+1
    
print("----------------------")

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("------------------------")

for i in range (1,6):
    for j in range(5-i,0,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
    
print("----------------------")
