import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#se crea la interfaz
ventana = tk.Tk()
ventana.title ("Ups...error")
ventana.geometry('400x450')
img = Image.open('pollo1.jpg')
new_img = img.resize ((300,256))
render = ImageTk.PhotoImage(new_img)
img1 = Label(ventana, image= render)
img1.image = render
img1.place(x=45, y=38)
miEtiqueta1 = Label(ventana, text="Datos incorrectos panzona", font=("Times New Roman", 13), fg="gray1")
miEtiqueta1.pack()

#se crean los botones
boton = tk.Button(ventana,command=ventana.quit, text='Ok entiendo', height=2, width=10)
boton.place(x=160, y=350)

ventana.mainloop()
