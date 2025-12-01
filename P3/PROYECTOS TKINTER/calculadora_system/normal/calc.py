'''Crear una calculadora:
1.-Dos campos de texto
2.- Cuatro botones para las operaciones
3.- Mostrar el resultado en una alerta 
'''

from tkinter import *
from tkinter import messagebox

ventana=Tk()
ventana.title("Calculadora")
ventana.geometry("500x500")
ventana.resizable(False,False)

#Controler
def operaciones(titulo,num1,num2,signo):
    if signo=="+":
        resultado=num1+num2
    elif signo=="-":
        resultado=num1-num2
    elif signo=="x":
        resultado=num1*num2
    elif signo=="/":
        resultado=num1/num2
    messagebox.showinfo(icon="info",title=titulo,message=f"{num1}+{num2}={resultado}")


#Interfaz
num1=IntVar()
num2=IntVar()
txt_caja1=Entry(ventana,textvariable=num1,width=5,justify="right")
txt_caja1.pack(side="top",anchor="center")

txt_caja2=Entry(ventana,textvariable=num2,width=5,justify="right")
txt_caja2.pack(side="top",anchor="center")

# NO sobrescribir el nombre de la función con la variable del botón
btn_suma=Button(ventana,text="+",command=lambda: operaciones("Suma",num1.get(),num2.get(),"+"))
btn_suma.pack()

btn_resta=Button(ventana,text="-",command=lambda: operaciones("Resta",num1.get(),num2.get(),"-"))
btn_resta.pack()

btn_multi=Button(ventana,text="x",command=lambda: operaciones("Multiplicacion",num1.get(),num2.get(),"x"))
btn_multi.pack()

btn_divi=Button(ventana,text="/",command=lambda: operaciones("Division",num1.get(),num2.get(),"/"))
btn_divi.pack()

btn_salir=Button(ventana,text="Salir",command=ventana.quit)
btn_salir.pack()

etiqueta=Label(ventana,text="")
etiqueta.pack()

ventana.mainloop()