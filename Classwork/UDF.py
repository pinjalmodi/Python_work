def oddeven(n):
    if n%2==0:
        print(n,"Is Even")
    else:
        print(n,"is odd")

def maxoftwo(a,b):
    if a>b:
        print(a,"is max")
    else:
        print(b,"is max")

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print(a,"is max")
        else:
            print(c,"is max")
    elif b>c:
        print(b,"is max")

    else:
        print(c,"is max")

def fibonacci(n):
    a,b=0,1
    print(a,end=" ")
    while b<n:
        print(b,end=" ")
        a,b=b,a+b

def prime(n):
    if n%2!=0:
        for j in range(1,int(n/2)+1,2):
            if n%j==0:
                print("It's not prime")
                break
        else:
            print("It's prime")
    else:
        print("Not Prime")


                
