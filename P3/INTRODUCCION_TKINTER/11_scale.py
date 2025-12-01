from tkinter import *

ventana=Tk()
ventana.title("Scale")
ventana.geometry("500x500")


def notificacion():
    etiq.config(text=f"Valor seleccionado por el usuario:  {valor.get()}")

valor=IntVar()
escala=Scale(ventana,from_=0,to=100,orient='horizontal',variable=valor)
escala.pack()



btn1=Button(ventana,text="Mostrar valor",command=notificacion)
btn1.pack()
etiq=Label(ventana,text="")
etiq.pack()

ventana.mainloop()