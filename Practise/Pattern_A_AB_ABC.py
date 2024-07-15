j=1
for i in range(65,73):       
    print(chr(i)+chr(65+j))
    j=j+1

print("---------------------")

for i in range(1, 4):  # Loop from 1 to 3
    line = ""
    for j in range(i):
        line += chr(65 + j)  # Append characters from 'A' to 'C'
    print(line)


print("-----------------")
j=i
for i in range(65,73):
    print(" "+chr(65+j))
    j=j+1

print("-----------------")

for i in range(65,73):
    for j in range(i):
        print(chr(65+j))`
              


