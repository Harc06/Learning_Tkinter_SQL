from tkinter import *

raiz = Tk()

#window title
raiz.title('Window test')

#Modify window size
raiz.resizable(1,1)

#add window icon (extension.ico)
raiz.iconbitmap('coding.ico')

#change window size
raiz.geometry('650x350')

#Change bg color
raiz.config(bg = 'blue')

#Create a frame
myFrame = Frame()

#To pack it inside the root
myFrame.pack()

#Give background color to frame
myFrame.config(bg='Red')

#Change frame size, width height
myFrame.config(wid='650', height='350')

#Change border size
myFrame.config(bd='35')

#add border to frame
myFrame.config(relief= 'sunken')

#Change the cursor when positioned in the frame
myFrame.config(cursor= 'hand2')

#Main loop must always be at the end of the code
raiz.mainloop()
