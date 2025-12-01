from tkinter import *

ventana=Tk()
ventana.title("List Box")
ventana.geometry("500x500")

def notificacion():
    seleccion=lista.get(lista.curselection())
    etiq.config(text=f"Seleccionaste: {seleccion}")

lista=Listbox(ventana,width=10,height=5,selectmode='single' )
lista.pack()

opciones=['Amarillo', 'Rojo', 'Azul', 'Verde',]
for i in opciones:
    lista.insert(END, i)


btn1=Button(ventana,text="Mostrar seleccion del usuario",command=notificacion)
btn1.pack()
etiq=Label(ventana,text="")
etiq.pack()

ventana.mainloop()