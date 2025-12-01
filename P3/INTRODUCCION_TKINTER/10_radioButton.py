from tkinter import *

ventana=Tk()
ventana.title("Radio Button")
ventana.geometry("500x500")


def notificacion():
    etiq.config(text=f"Opcion seleccionada {opcion.get()}")



opcion=StringVar()
radiobutton=Radiobutton(ventana,text="Opcion 1",variable=opcion,value="Opcion 1")
radiobutton.pack()
radiobutton2=Radiobutton(ventana,text="Opcion 2",variable=opcion,value="Opcion 2")
radiobutton2.pack()
radiobutton3=Radiobutton(ventana,text="Opcion 3",variable=opcion,value="Opcion 3")
radiobutton3.pack()

btn1=Button(ventana,text="Mostrar seleccion",command=notificacion)
btn1.pack()
etiq=Label(ventana,text="")
etiq.pack()

ventana.mainloop()