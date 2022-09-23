from tkinter import *

root = Tk()
root.title('Calculator')
root.resizable(1,1)
# root.geometry('400x500')

MyFrame= Frame(root)
# MyFrame.config(background='Black')
MyFrame.pack()

#------------NumberInWindow------------
numberIntro=StringVar()

#--------------Window----------------
numberWindow = Entry(MyFrame, textvariable=numberIntro)
numberWindow.grid(row=1, column=1, padx= 10, pady= 10, columnspan=4) 
numberWindow.config(background='Black', fg='#85E747', justify='right')

#------------PressButton-----------------

def pressButton(num):
    numberIntro.set(numberWindow.get() + num)


#------------Buttons----------------
button7= Button(MyFrame, text='7',width=3, command= lambda:pressButton('7'))
button7.grid(row=2, column=1)

button8= Button(MyFrame, text='8', width=3, command= lambda:pressButton('8'))
button8.grid(row=2, column=2)

button9= Button(MyFrame, text='9', width=3, command= lambda:pressButton('9'))
button9.grid(row=2, column=3)

buttonMultiply= Button(MyFrame, text='X', width=3)
buttonMultiply.grid(row=3, column=4)

buttonDiv= Button(MyFrame, text='/',width=3)
buttonDiv.grid(row=2,column=4)

#--------------SecondColumn------------
button4= Button(MyFrame, text='4',width=3, command= lambda:pressButton('4'))
button4.grid(row=3, column=1)

button5= Button(MyFrame, text='5', width=3, command= lambda: pressButton('5'))
button5.grid(row=3, column=2)

button6= Button(MyFrame, text='6', width=3, command= lambda: pressButton('6'))
button6.grid(row=3, column=3)

buttonSubstract= Button(MyFrame, text='-', width=3)
buttonSubstract.grid(row=4, column=4)

#------------third Column-----------
button1= Button(MyFrame, text='1',width=3, command= lambda: pressButton('1'))
button1.grid(row=4, column=1)

button2= Button(MyFrame, text='2', width=3, command=  lambda: pressButton('2'))
button2.grid(row=4, column=2)

button3= Button(MyFrame, text='3', width=3, command= lambda: pressButton('3'))
button3.grid(row=4, column=3)

buttonAdd= Button(MyFrame, text='+', width=3)
buttonAdd.grid(row=5, column=4)

#------------fourth Column-------------

button0= Button(MyFrame, text='0', width=3, command= lambda: pressButton('0'))
button0.grid(row=5, column=1)

buttonPoint= Button(MyFrame, text='.', width=3, command= lambda: pressButton('.'))
buttonPoint.grid(row=5, column=2)

buttonEqual= Button(MyFrame, text='=', width=3)
buttonEqual.grid(row=5, column=3)


root.mainloop()