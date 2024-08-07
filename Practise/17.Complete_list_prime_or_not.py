#Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.


l1=[1,2,3,4,5,6]
l2=[3,5,7]
l3=[11,13,17]

for lst in (l1,l2,l3):
    for i in lst:
        if int(i)%2!=0:
            result=True
            for j in range(3,int(i/2)+1,2):
                if i%j==0:
                    result=False
                    break
            else:
                result=True
                print(i)
        else:
            result=False
            
