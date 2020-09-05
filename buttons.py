#This program illustrates the use of buttons , in tkinter, gf and bf are used to color the button

from tkinter import *

root = Tk()

def click():
	label = Label(root,text="Pressed a button").pack()

myButton = Button(root,text="Press me!",command=click , fg="white" , bg ="black")
myButton.pack()

root.mainloop()
