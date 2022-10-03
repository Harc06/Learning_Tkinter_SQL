from tkinter import *

root=Tk()

myframe=Frame(root)

myframe.pack()

operation=""

window_reset=False

result=0

#-------------window---------------------------------------

numberWindow=StringVar()

window=Entry(myframe, textvariable=numberWindow)
window.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
window.config(background="black", fg="#03f943", justify="right")

#-------------------press number--------------------------

def pressButton(num):

	global operation

	global window_reset

	if window_reset!=False:

		numberWindow.set(num)

		window_reset=False

	else:
	
		numberWindow.set(numberWindow.get() + num)

#----------------addition function----------------------------------

def addition(num):

	global operation

	global result

	global window_reset

	result+=int(num) #result=result+int(num)

	operation="addition"

	window_reset=True

	numberWindow.set(result)

#---------------substraction function------------------------------
num1=0

substraction_count=0

def substraction(num):

	global operation

	global result

	global num1

	global substraction_count

	global window_reset

	if substraction_count==0:

		num1=int(num)

		result=num1

	else:

		if substraction_count==1:

			result=num1-int(num)

		else:

			result=int(result)-int(num)	

		numberWindow.set(result)

		result=numberWindow.get()


	substraction_count=substraction_count+1

	operation="substraction"

	window_reset=True

#-------------Multiply function---------------------
multiply_count=0

def multiply(num):

	global operation

	global result

	global num1

	global multiply_count

	global window_reset
	
	if multiply_count==0:

		num1=int(num)
		
		result=num1

	else:

		if multiply_count==1:

			result=num1*int(num)

		else:

			result=int(result)*int(num)	

		numberWindow.set(result)
		
		result=numberWindow.get()


	multiply_count=multiply_count+1

	operation="multiply"

	window_reset=True

#-----------------div function---------------------

div_count=0

def division(num):

	global operation

	global result

	global num1

	global div_count

	global window_reset
	
	if div_count==0:

		num1=float(num)
		
		result=num1

	else:

		if div_count==1:

			result=num1/float(num)

		else:

			result=float(result)/float(num)	

		numberWindow.set(result)
		
		result=numberWindow.get()

	div_count=div_count+1

	operation="division"

	window_reset=True

#----------------Result function----------------

def FinalResult():

	global result

	global operation

	global substraction_count

	global multiply_count

	global div_count
	
	if operation=="addition":

		numberWindow.set(result+int(numberWindow.get()))

		result=0

	elif operation=="substraction":

		numberWindow.set(int(result)-int(numberWindow.get()))

		result=0

		substraction_count=0

	elif operation=="multiply":

		numberWindow.set(int(result)*int(numberWindow.get()))

		result=0

		multiply_count=0

	elif operation=="division":

		numberWindow.set(int(result)/int(numberWindow.get()))

		result=0

		div_count=0

#-------------fila 1---------------------------------------------

button7=Button(myframe, text="7", width=3, command=lambda:pressButton("7"))
button7.grid(row=2, column=1)
button8=Button(myframe, text="8", width=3, command=lambda:pressButton("8"))
button8.grid(row=2, column=2)
button9=Button(myframe, text="9", width=3, command=lambda:pressButton("9"))
button9.grid(row=2, column=3)
buttonDiv=Button(myframe, text="/", width=3, command=lambda:division(numberWindow.get()))
buttonDiv.grid(row=2, column=4)

#-------------file 2---------------------------------------------

button4=Button(myframe, text="4", width=3, command=lambda:pressButton("4"))
button4.grid(row=3, column=1)
button5=Button(myframe, text="5", width=3, command=lambda:pressButton("5"))
button5.grid(row=3, column=2)
button6=Button(myframe, text="6", width=3, command=lambda:pressButton("6"))
button6.grid(row=3, column=3)
buttonMultiply=Button(myframe, text="x", width=3, command=lambda:multiply(numberWindow.get()))
buttonMultiply.grid(row=3, column=4)

#-------------fila 3---------------------------------------------

button1=Button(myframe, text="1", width=3, command=lambda:pressButton("1"))
button1.grid(row=4, column=1)
button2=Button(myframe, text="2", width=3, command=lambda:pressButton("2"))
button2.grid(row=4, column=2)
button3=Button(myframe, text="3", width=3, command=lambda:pressButton("3"))
button3.grid(row=4, column=3)
buttonSubstract=Button(myframe, text="-", width=3, command=lambda:substraction(numberWindow.get()))
buttonSubstract.grid(row=4, column=4)

#-------------file 4---------------------------------------------

button0=Button(myframe, text="0", width=3, command=lambda:pressButton("0"))
button0.grid(row=5, column=1)
buttoncomma=Button(myframe, text=",", width=3, command=lambda:pressButton("."))
buttoncomma.grid(row=5, column=2)
buttonEqual=Button(myframe, text="=", width=3, command=lambda:FinalResult())
buttonEqual.grid(row=5, column=3)
buttonAdd=Button(myframe, text="+", width=3, command=lambda:addition(numberWindow.get()))
buttonAdd.grid(row=5, column=4)

root.mainloop()
