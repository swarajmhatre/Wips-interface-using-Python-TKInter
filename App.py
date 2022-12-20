from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("320x550")
root.title("Window")
root.config(background="white")

# Adding top image
from PIL import ImageTk, Image
img = ImageTk.PhotoImage(Image.open("img1.jpg"));
my_label = Label(image=img)
my_label.place(relx = 0,
                   rely = 0,
                   anchor = 'center')
my_label.pack()

#frame for buttons
frameb = Frame(root,width=350)
frameb= LabelFrame(root,padx=0, pady=0, height=50, width=350)
frameb.pack()
frameb.config(bg="white")
#Radio_Buttons
RadioVar = IntVar()
RadioVar.set(0)
r1 = Radiobutton(frameb, text="Prepaid", variable = RadioVar, value=1)
r1.grid(column=0, row=0)
r2 = Radiobutton(frameb, text="Postpaid", variable = RadioVar, value=2)
r2.grid(column=1, row=0)
frameb.place( relx=0.5, rely=0.20,anchor= CENTER)

# # frames
e = Entry(root )
e.pack()
e.config(highlightbackground ="blue")
e.insert(0, "Enter Mobile Number")
e.place (relx=0.5 , y=160,anchor= CENTER)

#frame for dropdowns
framed = Frame(root,width=300)
framed= LabelFrame(root,padx=20, pady=20, height=250, width=300)
framed.pack()
framed.config(bg="white")
#Dropdowns
selected1 = StringVar()
selected1.set("Select Operator")
dlist1 =[
    "Jio",
    "Airtel",
    "VI"
]
dropdn1 = OptionMenu(framed, selected1, *dlist1)
dropdn1.grid(row=0, column=0)
# dropdn1.place(x=70, y=200)

SampleLabel = Label(framed, text=" ", bg="white")
SampleLabel.grid(row=1 , column=0)

selected2 = StringVar()
selected2.set("Select Pack")
dlist2 =[
    "179",
    "259",
    "329",
    "489"
]
dropdn2 = OptionMenu(framed, selected2, *dlist2)
dropdn2.grid(row=2, column=0)
framed.place(relx=0.5, rely=0.47, anchor= CENTER)

#PayNow_Button
def btnclicked():
   
    if(RadioVar.get() == 1):
        new_window = Tk()
        newlabel = Label(new_window, text="You have recharged Successfully on your " + selected1.get()+ " no. " +  e.get() + " of Rs. " + selected2.get() )
        newlabel.pack()
        newlabel.pack(padx=100, pady=100)
        new_window.mainloop()
    elif(RadioVar.get() == 2):
        new_window = Tk()
        newlabel = Label(new_window, text= "Rs. " + selected2.get() + " will be debited from your next recharge on your " + selected1.get()+ " no. " +  e.get())
        newlabel.pack()
        newlabel.pack(padx=100, pady=100)
        new_window.mainloop()

b= Button(root, text="Pay Now", width=10, command=btnclicked, bg="#01579B", fg="white")
b.pack()
b.place(y=355, relx=0.5, anchor= CENTER)


# Adding Bottom image
from PIL import ImageTk, Image
img2 = ImageTk.PhotoImage(Image.open("img4.jpg"));
my_label = Label(image=img2)
my_label.pack(side=BOTTOM)
root.mainloop()

