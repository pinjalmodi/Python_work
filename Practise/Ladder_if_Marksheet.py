rno=int(input("Enter Student RollNo"))
sname=input("Enter Student name")
m1=int(input("Enter Marks1"))
m2=int(input("Enter Marks2"))
m3=int(input("Enter Marks3"))

total=m1+m2+m3

per=total/3

print("RollNo:",rno)
print("Student Name:",sname)
print("Marks for Sub1:",m1)
print("Marks for Sub2:",m2)
print("Marks for Sub3:",m3)
print("Total:",total)
print("Percentage:",per)
if per>=70:
    print("Distinction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass Class")
else:
    print("Fail")
