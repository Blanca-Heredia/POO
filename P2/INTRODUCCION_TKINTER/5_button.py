from tkinter import *


def cambiar_texto():
    nombre.config(text="Marlene Heredia")
    contraseña.config(text="1234")

def regresar_texto():
    nombre.config(text="Nombre:    ")
    contraseña.config(text="Contraseña:   ")

ventana=Tk()
ventana.title("Uso de botones, marcos y etiquetas")
ventana.geometry("800x600")

marco=Frame(ventana)
marco.config(
    width=800,
    height=100,
    border=2,
    relief=SOLID,
    bg="green"
)
marco.pack_propagate(False)
marco.pack(pady=10)

label_titulo=Label(marco,text="Inicio de sesion")
label_titulo.config(
    bg="green",
    height=50,
    font="Arial"
)
label_titulo.pack()
nombre=Label(ventana,text="Nombre:   ")
nombre.pack(pady=10)
contraseña=Label(ventana,text="Contraseña:   ")
contraseña.pack(pady=10)

boton_aceptar=Button(ventana, text="Aceptar",command=cambiar_texto).pack(pady=10)
regresar=Button(ventana,text="Regresar", command=regresar_texto).pack(pady=10)

ventana.mainloop()

'''inicio sesion
usuario
contraseña
boton entrar'''
