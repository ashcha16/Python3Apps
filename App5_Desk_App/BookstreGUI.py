"""
Application for collecting and maintaining Book information:
Title
Author
Year
ISBN -> Book Identification Number

Button options:
View All
Search Entry
Add Entry
Update selected
Delete selected
Close
"""
from tkinter import *
import BookstreBackend

def get_selected_info(event):    
    try:
        global selected_tuple # Don't need to return in this as global variable can be used in program
        index = list1.curselection()[0] #(2,)--> 2 will give 2 as we have used [0]
        selected_tuple=list1.get(index) # will get the entire tuple value or selected line
        e_title.delete(0,END)
        e_title.insert(END,selected_tuple[1])
        e_auth.delete(0,END)
        e_auth.insert(END,selected_tuple[2])
        e_year.delete(0,END)
        e_year.insert(END,selected_tuple[3])
        e_isbn.delete(0,END)
        e_isbn.insert(END,selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0,END)
    for rows in BookstreBackend.viewAll():
        list1.insert(END,rows)

def search_command():
    list1.delete(0,END)
    for rows in BookstreBackend.search(etitle.get(),eauth.get(),eyr.get(),eisbn.get()):
        list1.insert(END,rows)

def add_command():
    BookstreBackend.Add(etitle.get(),eauth.get(),eyr.get(),eisbn.get())
    clear_command()

def delete_command():
    BookstreBackend.delete(selected_tuple[0])
    clear_command()

def update_command():
    BookstreBackend.update(selected_tuple[0],etitle.get(),eauth.get(),eyr.get(),eisbn.get())
    clear_command()

def clear_command():
    list1.delete(0,END)
    e_auth.delete(0,END)
    e_year.delete(0,END)
    e_isbn.delete(0,END)
    e_title.delete(0,END)
    

window = Tk()

window.wm_title("Book Store") # For the title in the window box

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

etitle=StringVar()
e_title = Entry(window,textvariable=etitle)
e_title.grid(row=0,column=1)

eauth=StringVar()
e_auth = Entry(window,textvariable=eauth)
e_auth.grid(row=0,column=3)

eyr=StringVar()
e_year = Entry(window,textvariable=eyr)
e_year.grid(row=1,column=1)

eisbn=StringVar()
e_isbn = Entry(window,textvariable=eisbn)
e_isbn.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=7,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#This piece of code will use bind function which is used to call a function based on event at a specific widget
#In this case we are getting selected values from listbox and extract the deatils to use in delete and update button
#to bind we pass event and a fucntion to execute
list1.bind('<<ListboxSelect>>',get_selected_info)

b1=Button(window,text="View All",width="12",command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width="12",command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width="12",command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Selected",width="12",command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Selected",width="12",command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Clear All",width="12",command=clear_command)
b6.grid(row=7,column=3)

b7=Button(window,text="Close",width="12",command=window.destroy)
b7.grid(row=8,column=3)



window.mainloop()
