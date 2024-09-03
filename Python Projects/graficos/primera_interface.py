#Si se cambia el archivo py a pyw se abre sin abrir por detras el cmd

from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas") #Para colocar el titulo

#raiz.resizable(0,0) #Dos parámetros booleanos (para permitir o no redimensionar)

#Para cambiar el icono se necesita un archivo de tipo .ico
#raiz.iconbitmap("[Ruta]")

raiz.geometry("650x350") #Para cambiar el tamaño de la ventana

raiz.config(bg = "black") #Permite configurar varias cosas de la raiz 

miFrame = Frame()

#miFrame.pack() #Si solo se le da así no aparece nada se debe dar un tamaño

miFrame.pack(side = "right")

miFrame.config(bg="red")

miFrame(width = "650", height="350")

raiz.mainloop()
