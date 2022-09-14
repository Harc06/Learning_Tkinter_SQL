
from tkinter import *
import path

root = Tk()

myFrame = Frame(root, width=500, height=400)   

myFrame.pack()  

image = r'c:/Users/harc6/Visual Studio Code/Tkinter and sql/Learning_Tkinter_SQL/TKINTER/pika.gif'

myimage=PhotoImage(file=image)

# to place the label where we want
mylabel= Label(myFrame,  image =myimage, text="Hello python", fg='Red', font=("Comic Sans MS", 18)).grid(row= 1, column=2)

textBoxName = Entry(myFrame)
# grid for create row and columns
textBoxName.grid(row=1, column=1)
textBoxName.config(fg='Red', justify='center')

textBoxPass = Entry(myFrame)
textBoxPass.grid(row=2, column=1)
textBoxPass.config(fg='Red', justify='center')
textBoxPass.config(show='*')

textBoxLName = Entry(myFrame)
textBoxLName.grid(row=3, column=1)

textBoxAdress = Entry(myFrame)
textBoxAdress.grid(row=4, column=1)

#to put a label to the text box
labelName = Label(myFrame, text = 'Name', fg ='Black', padx = 10, pady = 40)
labelName.grid(row=1, column=0)

labelLName = Label(myFrame, text = 'LastName', fg ='Blue',padx = 10, pady = 60)
labelLName.grid(row=3, column=0)

labelpass = Label(myFrame, text = 'PassWord', fg ='Black', padx = 10, pady = 80)
labelpass.grid(row=2, column=0)

labelAdress = Label(myFrame, text = 'Adress', fg ='Red',padx = 10, pady = 10)
labelAdress.grid(row=4, column=0)

root.mainloop()
