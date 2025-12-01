from tkinter import *
from controller import funciones

#interfaz o view
def interfaz():
    ventana=Tk()
    ventana.title("Calculadora")
    ventana.geometry("600x400")
    ventana.resizable(False,False) #para que la pantalla este fija

    n1=IntVar()
    n2=IntVar()
    txt_numero1=Entry(ventana,textvariable=n1, width=5,justify="right")
    txt_numero1.pack(side="top", anchor="center")

    txt_numero2=Entry(ventana,textvariable=n2, width=5,justify="right")
    txt_numero2.pack(side="top", anchor="center")

    btn_sum=Button(ventana,text="+",command=lambda: funciones.operaciones("Suma",n1.get(),n2.get(),"+"))
    btn_sum.pack()

    btn_resta=Button(ventana,text="-", command=lambda: funciones.operaciones("Resta",n1.get(),n2.get(),"-"))
    btn_resta.pack()

    btn_multi=Button(ventana, text="*", command=lambda: funciones.operaciones("Multiplicacion",n1.get(),n2.get(),"x"))
    btn_multi.pack()

    btn_division=Button(ventana,text="/",command=lambda: funciones.operaciones("Division",n1.get(),n2.get(),"/"))
    btn_division.pack()

    btn_salir=Button(ventana,text="Salir", command=ventana.quit)
    btn_salir.pack()

    ventana.mainloop()