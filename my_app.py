from tkinter import *
import my_app_back as bk

window= Tk()

window.wm_title("Stock Analysis App")

def stock_command():

    f=bk.stock_data(e1var.get(),e3var.get(),e4var.get())
    e1.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    bk.show(f)


l1=Label(window,text="Stock Symbol",width=20)
l1.grid(row=0,column=0)



e1var=StringVar()
e1=Entry(window,textvariable=e1var)
e1.grid(row=0,column=1,columnspan=2)

#l2=Label(window,text="Data Source(Google/Yahoo)",width=25)
#l2.grid(row=0,column=3)

#e2var=StringVar()
#e2=Entry(window,textvariable=e2var)
#e2.grid(row=0,column=4,columnspan=5)

l3=Label(window,text="Start Date(DD/MM/YYY)",width=20)
l3.grid(row=1,column=0)

e3var=StringVar()
e3=Entry(window,textvariable=e3var)
e3.grid(row=1,column=1,columnspan=2)

l4=Label(window,text="End Date(DD/MM/YYY)",width=20)
l4.grid(row=2,column=0)

e4var=StringVar()
e4=Entry(window,textvariable=e4var)
e4.grid(row=2,column=1,columnspan=2)

b1=Button(window,text="Submit",width=10,command=stock_command)
b1.grid(row=3,column=0)

b2=Button(window,text="Close",width=10,command=window.destroy)
b2.grid(row=3,column=2)

window.mainloop()