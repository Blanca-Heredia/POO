from tkinter import *
from tkinter import ttk

ventana=Tk()
ventana.title("ProgressBar")
ventana.geometry("500x500")

def progreso():
    barrapro['value']=0
    ventana.update()
    for i in range(101):
        barrapro['value']=i
        ventana.update()
        ventana.after(20)

barrapro=ttk.Progressbar(ventana,mode="determinate",length=200)
barrapro.pack()

btn1=Button(ventana,text="Iniciar progreso",command=progreso)
btn1.pack()
etiq=Label(ventana,text="")
etiq.pack()

ventana.mainloop()