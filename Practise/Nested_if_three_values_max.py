a=int(input("Enter Value for A"))
b=int(input("Enter value for B"))
c=int(input("Enter value for c"))

if a>b:
    if a>c:
        print("A is Max")
    else:
        print("C is Max")
elif b>c:
    print("B is Max")
else:
    print("C is Max")
