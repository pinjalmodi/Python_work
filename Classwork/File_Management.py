#File Management

file=open("tops2.txt","w")
file.write("This is file management demo using python")
file.close()
print("File written Successfully")

print("********************************************")

file=open("tops2.txt","r")
print(file.read())
file.close()

print("**********************************************")

file=open("tops2.txt","a")
file.write("This file is now appended")
file.close()

print("**********************************************")

file=open("tops3.txt","w+")
file.write("This is W+ Mode using Python****")
print("Current Position",file.tell())
file.seek(0)
print("File Data:",file.read())
file.close()

print("*********************************************")
