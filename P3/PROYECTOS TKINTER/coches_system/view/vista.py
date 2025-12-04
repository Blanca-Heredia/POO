from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controller import controlador 


class Vistas:
    def __init__(self, ventana):
        ventana.title("Coches")
        ventana.geometry("1000x1000")
        self.interfaz(ventana)

    def borrarPantalla(self, ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def interfaz(self, ventana):
        self.borrarPantalla(ventana)
        ventana.geometry("1000x1000")
        txt_mp = Label(ventana, text="Menu Principal")
        txt_mp.pack(pady=7)
        btn1 = Button(ventana, text="1.-Coches", command=lambda: self.menu("Coches", ventana))
        btn1.pack(pady=7)
        btn2 = Button(ventana, text="2.-Camiones", command=lambda: self.menu("Camiones", ventana))
        btn2.pack(pady=7)
        btn3 = Button(ventana, text="3.-Camionetas", command=lambda: self.menu("Camionetas", ventana))
        btn3.pack(pady=7)
        btn4 = Button(ventana, text="4.-Salir", command=ventana.quit)
        btn4.pack(pady=7)

    def menu(self, tipo, ventana):
        self.borrarPantalla(ventana)
        ventana.geometry("1000x1000")
        txt_mp = Label(ventana, text=f"Menu de {tipo}")
        txt_mp.pack(pady=7)
        btn_add = Button(ventana, text="1.Agregar", command=lambda: self.datos(tipo, ventana))
        btn_add.pack(pady=7)
        btn_show = Button(ventana, text="2.Consultar", command=lambda: self.consultar(ventana, tipo))
        btn_show.pack(pady=7)
        btn_update = Button(ventana, text="3.Modificar", command=lambda: self.actualizar(tipo, ventana))
        btn_update.pack(pady=7)
        btn_delete = Button(ventana, text="4.Eliminar", command=lambda: self.borrar(ventana, tipo))
        btn_delete.pack(pady=7)
        btn_back = Button(ventana, text="5.Volver", command=lambda: self.interfaz(ventana))
        btn_back.pack(pady=7)

    def obtener_controlador(self, tipo):
        if tipo == "Coches":
            return controlador.Coches
        elif tipo == "Camiones":
            return controlador.Camiones
        elif tipo == "Camionetas":
            return controlador.Camionetas
        return None

    def datos(self, tipo, ventana):
        ventana.geometry("1000x1000")
        self.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text=f"Agregar {tipo}")
        lbl_titulo.pack(pady=7)
        lbl_marca = Label(ventana, text="Marca: ")
        lbl_marca.pack(pady=7); txt_marca = Entry(ventana, width=25, justify="left"); txt_marca.pack(pady=7)
        lbl_color = Label(ventana, text="Color: ")
        lbl_color.pack(pady=7); txt_color = Entry(ventana, width=25, justify="left"); txt_color.pack(pady=7)
        lbl_modelo = Label(ventana, text="Modelo: ")
        lbl_modelo.pack(pady=7); txt_modelo = Entry(ventana, width=25, justify="left"); txt_modelo.pack(pady=7)
        lbl_velocidad = Label(ventana, text="Velocidad: ")
        lbl_velocidad.pack(pady=7); txt_velocidad = Entry(ventana, width=25, justify="left"); txt_velocidad.pack(pady=7)
        lbl_caballaje = Label(ventana, text="Caballaje: ")
        lbl_caballaje.pack(pady=7); txt_caballaje = Entry(ventana, width=25, justify="left"); txt_caballaje.pack(pady=7)
        lbl_plazas = Label(ventana, text="Plazas: ")
        lbl_plazas.pack(pady=7); txt_plazas = Entry(ventana, width=25, justify="left"); txt_plazas.pack(pady=7)
        controlador_obj = self.obtener_controlador(tipo)
        
        btn_command = lambda: controlador_obj.crear(
            txt_marca.get(), 
            txt_color.get(), 
            txt_modelo.get(), 
            int(txt_velocidad.get()), 
            int(txt_caballaje.get()), 
            int(txt_plazas.get())
        )
        
        btn_en = Button(ventana, text="Agregar", command=btn_command)
        btn_en.pack(pady=7)
        
        btn_back = Button(ventana, text="Regresar", command=lambda: self.menu(tipo, ventana))
        btn_back.pack(pady=7)

    def consultar(self, ventana, tipo):
        self.borrarPantalla(ventana)
        lblTitulo = Label(ventana, text=f"Consultar {tipo}")
        lblTitulo.pack(pady=5)
        controlador_obj = self.obtener_controlador(tipo)
        registros = controlador_obj.mostrar() if controlador_obj else []

        filas = ""
        if len(registros) > 0:
            num_autos = 1
            for fila in registros:
                if tipo == "Coches":
                    filas = filas + f"\n{tipo} #{num_autos} ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Velocidad: {fila[4]} Potencia: {fila[5]} Plazas: {fila[6]}"
                elif tipo == "Camiones":
                    filas = filas + f"\n{tipo} #{num_autos} ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Vel: {fila[4]} Pot: {fila[5]} Plazas: {fila[6]} Eje: {fila[7]} Carga: {fila[8]}"
                elif tipo == "Camionetas":
                    filas = filas + f"\n{tipo} #{num_autos} ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Vel: {fila[4]} Pot: {fila[5]} Plazas: {fila[6]} Tracción: {fila[7]} Cerrada: {fila[8]}"
                num_autos += 1
        else:
            messagebox.showinfo(message=f"No hay {tipo.lower()} en el sistema")
        lblNote = Label(ventana, text=filas, justify=LEFT) 
        lblNote.pack(pady=5)
        btn_back = Button(ventana, text="Regresar", command=lambda: self.menu(tipo, ventana))
        btn_back.pack(pady=7)

    def actualizar(self, tipo, ventana):
        ventana.geometry("1000x1000")
        self.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text=f"Actualizar {tipo}")
        lbl_titulo.pack(pady=7)
        
        controlador_obj = self.obtener_controlador(tipo)
        
        lbl_id = Label(ventana, text=f"Id de {tipo}: ")
        lbl_id.pack(pady=7); txt_id = Entry(ventana, width=25, justify="left"); txt_id.pack(pady=7)
        lbl_marca = Label(ventana,text="Nueva marca: "); lbl_marca.pack(pady=7); txt_marca=Entry(ventana,width=25,justify="left"); txt_marca.pack(pady=7)
        lbl_color = Label(ventana,text="nuevo color: "); lbl_color.pack(pady=7); txt_color=Entry(ventana,width=25,justify="left"); txt_color.pack(pady=7)
        lbl_modelo = Label(ventana,text="Nuevo modelo: "); lbl_modelo.pack(pady=7); txt_modelo=Entry(ventana,width=25,justify="left"); txt_modelo.pack(pady=7)
        lbl_velocidad = Label(ventana,text="Nueva velocidad: "); lbl_velocidad.pack(pady=7); txt_velocidad=Entry(ventana,width=25,justify="left"); txt_velocidad.pack(pady=7)
        lbl_caballaje = Label(ventana,text="Nuevo caballaje: "); lbl_caballaje.pack(pady=7); txt_caballaje=Entry(ventana,width=25,justify="left"); txt_caballaje.pack(pady=7)
        lbl_plazas = Label(ventana,text="Nuevas plazas: "); lbl_plazas.pack(pady=7); txt_plazas=Entry(ventana,width=25,justify="left"); txt_plazas.pack(pady=7)
        btn_command = lambda: controlador_obj.actualizar(
            txt_marca.get(),
            txt_color.get(),
            txt_modelo.get(),
            int(txt_velocidad.get()),
            int(txt_caballaje.get()),
            int(txt_plazas.get()),
            txt_id.get()
        )
        
        btn_en = Button(ventana, text="Actualizar", command=btn_command)
        btn_en.pack(pady=7)
        btn_back = Button(ventana, text="Regresar", command=lambda: self.menu(tipo, ventana))
        btn_back.pack(pady=7)

    def borrar(self, ventana, tipo):
        self.borrarPantalla(ventana)
        lblTitulo = Label(ventana, text=f"Eliminar {tipo.lower()}")
        lblTitulo.pack(pady=5)
        lblId = Label(ventana, text="Ingresar ID:")
        lblId.pack(pady=5)
        txtId = Entry(ventana)
        txtId.pack()
        controlador_obj = self.obtener_controlador(tipo)
        btnEliminar = Button(ventana, text="Eliminar", command=lambda: controlador_obj.buscar(txtId.get()))
        btnEliminar.pack(pady=5)
        
        btn_back = Button(ventana, text="Regresar", command=lambda: self.menu(tipo, ventana))
        btn_back.pack(pady=7)