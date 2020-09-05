#This time was have used grids to format the output of the text on the screen . Pretty Basic :-)
from tkinter import *
root = Tk()

myLabel = Label(root,text="Hello Sparsh")
myLabel.grid(row=0,column=0)

myLabel1= Label(root,text="What a time to be alive")
myLabel1.grid(row=1,column=1)


#label=Label(root,text="123").grid(row=2,column=2) is also valid. 

root.mainloop()
