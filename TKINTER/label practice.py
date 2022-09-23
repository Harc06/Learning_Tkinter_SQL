from tkinter import *

root = Tk()

myFrame = Frame(root, width=500, height=400)   
myFrame.pack()  

myName= StringVar()
# to place the label where we want
mylabel= Label(myFrame, fg='Black', font=("Comic Sans MS", 18)).grid(row= 2, column=2)

textBoxName = Entry(myFrame, textvariable=myName)
# grid for create row and columns
textBoxName.grid(row=1, column=1)
textBoxName.config(fg='Black', justify='center')

textBoxPass = Entry(myFrame)
textBoxPass.grid(row=2, column=1)
textBoxPass.config(fg='Black', justify='center')
textBoxPass.config(show='*')

textBoxLName = Entry(myFrame)
textBoxLName.grid(row=3, column=1)
textBoxLName.config(fg='Black', justify= 'center')

textBoxAdress = Entry(myFrame)
textBoxAdress.grid(row=4, column=1)
textBoxAdress.config(fg='Black', justify= 'center')

textBoxComments = Text(myFrame, width=16, height=5)
textBoxComments.grid(row=5, column=1, padx = 10, pady = 10)

#Scroll Bar
scrollbar= Scrollbar(myFrame, command=textBoxComments.yview)
scrollbar.grid(row=5, column=2, sticky='nsew')
textBoxComments.config(yscrollcommand=scrollbar.set)

#to put a label to the text box
labelName = Label(myFrame, text = 'Name', fg ='Black', padx = 10, pady = 10)
labelName.grid(row=1, column=0)

labelLName = Label(myFrame, text = 'LastName', fg ='Black',padx = 10, pady = 10)
labelLName.grid(row=3, column=0)

labelpass = Label(myFrame, text = 'PassWord', fg ='Black', padx = 10, pady = 10)
labelpass.grid(row=2, column=0)

labelAdress = Label(myFrame, text = 'Adress', fg ='Black',padx = 10, pady = 10)
labelAdress.grid(row=4, column=0)

labelComment = Label(myFrame, text = 'Comments', fg ='Black',padx = 10, pady = 10)
labelComment.grid(row=5, column=0)

#BUTTON
def buttonCode():
    myName.set('Hugo')

buttonSend = Button(root, text = 'Send', command=buttonCode)
buttonSend.pack()

root.mainloop()
