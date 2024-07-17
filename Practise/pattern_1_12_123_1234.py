
for i in range(1,6):
    print(" " * (5-i),end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
    

print("----------------------")

for i in range (1,6):
    print("*"*(6-i),end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
    
print("----------------------")

for i in range(1,6):
    for j in range(5-i,0,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(" ",k,end=" ")
    print()
