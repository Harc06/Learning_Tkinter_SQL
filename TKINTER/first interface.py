from tkinter import *


root = Tk()

#window title
root.title('Window test')

#Modify window size
root.resizable(1,1)

icon = r'c:/Users/harc6/Visual Studio Code/Tkinter and sql/Learning_Tkinter_SQL/TKINTER/coding.ico'
#add window icon (extension.ico)
root.iconbitmap(icon)

#change window size
root.geometry('650x350')

#Change bg color
root.config(bg = 'blue') 

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
root.mainloop()
