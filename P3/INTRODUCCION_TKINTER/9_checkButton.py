from tkinter import *

ventana=Tk()
ventana.title("Check Button")
ventana.geometry("500x500")

def notificacion():
    if opcion.get()==1:
        etiq.config(text="Notificaciones activadas")
    else:
        etiq.config(text="Notificaciones desactivadas")




opcion=IntVar()
checkbutton=Checkbutton(ventana, text="Deseas recibir notificaciones? ",variable=opcion,onvalue=1,offvalue=0)
checkbutton.pack()

btn1=Button(ventana,text="Confirmar",command=notificacion)
btn1.pack()
etiq=Label(ventana,text="")
etiq.pack()





ventana.mainloop()