for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print()

print("------------------")

for i in range(1,6):
    print("* "*i)
print("-------------------")

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print("--------------------")

"""
j=1
for i in range(1,5):
    print(i,j,end=" ")
    print() 
    j=j+1

"""

    
print("------------------")

for i in range(1,5):
    for j in range (1,i+1):
        print(i,end=" ")
    print()

print("-----------------------")


for i in range(1,5):
    for k in range(4-i,0,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(" *",end=" ")
    print()


print("-**--------------------")

for i in range (1,5):
    for k in range(4-i,0,-1):
        print(" ",end=" ")
    for j in range(0,2*(i)-1):
        print("*",end=" ")
    print()

print("/////------------")

for i in range(1,5):
    for k in range(4-i,0,-1):
        print(" ",end=" ")
    for j in range(1,1+i):
        print(j,end=" ")
    print()

print("----------------------")

for i in range(1,5):
    for k in range(4-i,0,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(" ",i,end=" ")
    print()

print("--------------------")

j=1
for i in range(1,6):
    print(" "*(5-i),str(i)*j)
    j=j+1
print()

print("------------------------")

j=1
for i in range(65,73):
    print(" "*(73-i),chr(i)*j)
    j=j+1


print("--------------------------")

j = 1
for i in range(65, 70):
    print(" " * (70 - i), end='')
    for k in range(65, i + 1):
        print(chr(k), end='')
    print()
    j = j + 1
