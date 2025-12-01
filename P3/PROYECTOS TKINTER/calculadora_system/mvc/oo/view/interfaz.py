from tkinter import *
from tkinter import messagebox
from controller import funciones
from model import operaciones

#interfaz o view
class Vistas:
    def __init__(self,ventana):
        ventana.title("Calculadora")
        ventana.geometry("700x500")
        ventana.resizable(False,False) #para que la pantalla este fija
        self.interfaz(ventana)
    
    def interfaz(self,ventana):
        self.borrarPantalla(ventana)
        self.menu(ventana)
        n1=IntVar()
        n2=IntVar()
        txt_numero1=Entry(ventana,textvariable=n1, width=5,justify="right")
        txt_numero1.pack(side="top", anchor="center",pady=10)
        txt_numero2=Entry(ventana,textvariable=n2, width=5,justify="right")
        txt_numero2.pack(side="top", anchor="center",pady=10)

        btn_sum=Button(ventana,text="+",command=lambda: funciones.Controladores.operaciones("Suma",n1.get(),n2.get(),"+"))
        btn_sum.pack(pady=5)
        btn_resta=Button(ventana,text="-", command=lambda: funciones.Controladores.operaciones("Resta",n1.get(),n2.get(),"-"))
        btn_resta.pack(pady=5)
        btn_multi=Button(ventana, text="*", command=lambda: funciones.Controladores.operaciones("Multiplicacion",n1.get(),n2.get(),"x"))
        btn_multi.pack(pady=5)
        btn_division=Button(ventana,text="/",command=lambda: funciones.Controladores.operaciones("Division",n1.get(),n2.get(),"/"))
        btn_division.pack(pady=5)
        btn_salir=Button(ventana,text="Salir", command=ventana.quit)
        btn_salir.pack(pady=10)

    def menu(self,ventana):
        menubar=Menu(ventana)  
        ventana.config(menu=menubar)
        archivoMenu=Menu(menubar,tearoff=False)
        menubar.add_cascade(label="Operaciones",menu=archivoMenu)
        archivoMenu.add_command(label="Agregar",command=lambda: self.interfaz(ventana))
        archivoMenu.add_command(label="Consultar",command=lambda: self.consultar(ventana))
        archivoMenu.add_command(label="Cambiar",command=lambda: self.cambiar(ventana))
        archivoMenu.add_command(label="Borrar",command=lambda: self.borrar(ventana))
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir",command=ventana.quit)

    def borrar(self, ventana):
        self.borrarPantalla(ventana)
        self.menu(ventana)
        eti1 = Label(ventana, text="Borrar una Operacion")
        eti1.pack(pady=8)
        eti2 = Label(ventana, text="ID de la Operacion: ")
        eti2.pack(pady=8)
        oper_id = IntVar()
        txt_ope = Entry(ventana, textvariable=oper_id, justify="right", width=5)
        txt_ope.pack()
        btnbuscar=Button(ventana,text="Buscar", command=lambda: operaciones.Operaciones.buscar_id(oper_id.get()))
        btnbuscar.pack()
        btn_eliminar = Button(ventana, text="Eliminar", command=lambda: operaciones.Operaciones.eliminar(oper_id.get()))
        btn_eliminar.pack(pady=7)
        btn2 = Button(ventana, text="Volver", command=lambda: self.interfaz(ventana))
        btn2.pack()


    def borrarPantalla(self, ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def consultar(self, ventana):
        self.borrarPantalla(ventana)
        self.menu(ventana)

        lbl_titulo = Label( ventana, text=".:: Listado de las Operaciones ::.")
        lbl_titulo.pack(pady=10)

        registros = operaciones.Operaciones.consultar()

        if len(registros) == 0:
           Label(ventana, text="No hay operaciones registradas").pack(pady=20)
        else:
            for fila in registros:
                etiqueta_ope=(f"Operacion: {fila[0]} ID: {fila[0]} Fecha de Creacion: {fila[1]}\n"f"Operacion: {fila[2]}{fila[4]}{fila[3]}={fila[5]}")
                
                lbl_ope = Label(ventana,text=etiqueta_ope)
                lbl_ope.pack(pady=0)
                
        btn_volver = Button(ventana, text="Volver", width=10,command=lambda: self.interfaz(ventana))
        btn_volver.pack(pady=20)


    def cambiar(self, ventana):
        self.borrarPantalla(ventana)
        self.menu(ventana)
        Label(ventana, text="Cambiar una Operacion").pack(pady=5)
        Label(ventana, text="ID de la Operacion").pack(pady=5)
        num_id = IntVar()
        Entry(ventana, textvariable=num_id).pack(pady=5)

        Label(ventana, text="Nuevo numero 1").pack(pady=5)
        num1 = IntVar()
        Entry(ventana, textvariable=num1).pack(pady=5)

        Label(ventana, text="Nuevo numero 2").pack(pady=5)
        num2 = IntVar()
        Entry(ventana, textvariable=num2).pack(pady=5)

        Label(ventana, text="Nuevo signo").pack(pady=5)
        signo = StringVar()
        Entry(ventana, textvariable=signo).pack(pady=5)

        Label(ventana, text="Nuevo resultado").pack(pady=5)
        resu = StringVar()
        Entry(ventana, textvariable=resu).pack(pady=5)
        btn1 = Button(ventana, text="Guardar", command=lambda: funciones.Controladores.cambiar(num1.get(),num2.get(),signo.get(),resu.get(), num_id.get()))
        btn1.pack(pady=5)
        btn2 = Button(ventana, text="Volver", command=lambda: self.interfaz(ventana))
        btn2.pack(pady=5)
