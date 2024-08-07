s = input("Enter String:")


cons=0
cap=0
sml=0
sp=0
lettr=0

for i in s:
    if (s=='A' or s=='E' or s=='I' or s=='O' or s=='U'):
        cap=cap+1
    elif (s=='a' or s=='e' or s=='i' or s=='o' or s=='u'):
        sml=sml+1
    elif(s==" "):
        sp=sp+1
    elif(s=='0' or s=='1' or s=='2' or s=='3' or s=='4' or s=='5' or s=='6' or s=='7' or s=='8' or s=='9'):
        lettr=lettr+1
    else:
         cons=cons+1
print("Consonants",cons)
print("cap:",cap)
print("Small:",sml)
print("Space",sp)
print("letters",lettr)


print("-------------------------")


s=input("Enter String:")
al=0
nm=0
sp=0
uc=0
lc=0

for i in s:
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1

print("Total Alphabets:",al)
print("Total Numeric:",nm)
print("Total space:",sp)
print("Total Uppercase",uc)
print("Total Lowercase",lc)
      
      
