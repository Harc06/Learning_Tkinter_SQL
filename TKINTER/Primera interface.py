from tkinter import *

raiz = Tk()

#Titulo de la ventana
raiz.title('Ventana de pruebas')

#Modificar tamano de la ventana
raiz.resizable(1,1)

#agregar icono para la ventana(extension.ico)
raiz.iconbitmap('C:\Users\harc6\Visual Studio Code\Tkinter y Sql\Learning_Tkinter_SQL\coding.ico')

#Cambiar tamano de la ventana
raiz.geometry('650x350')

#Cambiar color de fondo
raiz.config(bg = 'blue')

#Crear un frame
miFrame = Frame()

#Para empaquetarlo dentro de la raiz
miFrame.pack()

#Dar color de fondo a frame
miFrame.config(bg='Red')

#Cambiar tamano del frame, wid-ancho height-alto
miFrame.config(wid='650', height='350')

#Cambiar tamano del borde
miFrame.config(bd='35')

#Agregar borde al frame
miFrame.config(relief= 'sunken')


#Cambiar el cursor al posicionarse en el frame
miFrame.config(cursor= 'hand2')

#Main loop siempre debe estar al final del codigo
raiz.mainloop()