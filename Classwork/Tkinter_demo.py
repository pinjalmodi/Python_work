from tkinter import *

def insert_data():
    print("Insert Called")
def search_data():
    print("Search called")
def update_data():
    print("Update called")
def delete_data():
    print("Delete Called")


root=Tk()
root.geometry("300x370")
root.title("My Tkinter CRUD Operation")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="First Name")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="last Name")
l_lname.place(x=50,y=150)

l_email=Label(root,text="Email")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="Mobile")
l_mobile.place(x=50,y=250)


e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_lname.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Arial"),command=insert_data)
insert.place(x=20,y=300)


search=Button(root,text="Search",bg="black",fg="white",font=("Arial"),command=search_data)
search.place(x=80,y=300)

update=Button(root,text="Update",bg="black",fg="white",font=("Arial"),command=update_data)
update.place(x=148,y=300)

delete=Button(root,text="Delete",bg="black",fg="white",font=("Arial"),command=delete_data)
delete.place(x=214,y=300)


