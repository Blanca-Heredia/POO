from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controller import controlador


class Vistas:
    def __init__(self,ventana):
        ventana.title("Coches")
        ventana.geometry("700x500")
        self.interfaz(ventana)

    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def interfaz(self,ventana):
        self.borrarPantalla(ventana)
        ventana.geometry("700x500")
        txt_mp=Label(ventana,text="Menu Principal")
        txt_mp.pack(pady=7)
        btn1=Button(ventana,text="1.-Coches",command=lambda:self.menu("autos",ventana))
        btn1.pack(pady=7)
        btn2=Button(ventana,text="2.-Camiones", command=lambda:"")
        btn2.pack(pady=7)
        btn3=Button(ventana,text="3.-Camionetas",command=lambda:"")
        btn3.pack(pady=7)
        btn4=Button(ventana,text="4.-Salir",command=ventana.quit)
        btn4.pack(pady=7)

    def menu(self,tipo,ventana):
        self.borrarPantalla(ventana)
        ventana.geometry("700x500")
        txt_mp=Label(ventana,text=f"Menu de {tipo}")
        txt_mp.pack(pady=7)
        btn_add=Button(ventana,text="1.-Agregar",command=lambda:self.datos_coches(tipo,ventana))
        btn_add.pack(pady=7)
        btn_show=Button(ventana,text="2.-Consultar", command=lambda:self.mostrarTabla(tipo,ventana))
        btn_show.pack(pady=7)
        btn_update=Button(ventana,text="3.-Modificar",command=lambda:self.actualizar(tipo,ventana))
        btn_update.pack(pady=7)
        btn_delete=Button(ventana,text="4.-Eliminar",command=lambda:self.datos_coches(tipo,ventana))
        btn_delete.pack(pady=7)
        btn_back=Button(ventana,text="5.-Volver",command=lambda:self.interfaz(ventana))
        btn_back.pack(pady=7)
