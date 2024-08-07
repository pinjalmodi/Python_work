import UDF

while True:
    print("*"*40)

    print("1.OddEven")
    print("2.MaxOfTwo")
    print("3.MaxOfThree")
    print("4.Fibonaccii")
    print("5.Prime")
    print("6.Exit")
    print("*"*40)
    
    choice=int(input("Enter your choice"))

    if choice==1:
        a=int(input("Enter Value:"))
        UDF.oddeven(a)
        print("*"*40)

    elif choice==2:
        a=int(input("Enter Value:"))
        b=int(input("Enter Value:"))
        UDF.maxoftwo(a,b)
        print("*"*40)
    elif choice==3:
        a=int(input("Enter Value:"))
        b=int(input("Enter Value:"))
        c=int(input("Enter Value:"))
        UDF.maxofthree(a,b,c)
        print("*"*40)
    elif choice==4:
        n=int(input("Enter Value:"))
        UDF.fibonacci(n)
        print("*"*40)
    elif choice==5:
        n=int(input("Enter Value:"))
        UDF.prime(n)
        print("*"*40)
    elif choice==6:
        print("Thnak you for using our services")
        print("*"*40)
        break
    else:
        print("Invalid choice..Please try again")
        print("*"*40)
        
        
        




