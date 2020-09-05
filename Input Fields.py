#in this program we are using text fields to handle the inputs

from tkinter import *

root = Tk()

inp = Entry(root, width = 50)
inp.pack()
inp.insert(0,"Enter your year of brith : ")

def click():
	out = "You are " + str(2020-int(inp.get())) + " years old."
	label = Label(root,text=out)
	label.pack()

myButton = Button(root,text="Press me!",command=click , fg="white" , bg ="black")
myButton.pack()

root.mainloop()
