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
        btn1=Button(ventana,text="1.-Coches",command=lambda:self.menu_crud("Coche",ventana))
        btn1.pack(pady=7)
        btn2=Button(ventana,text="2.-Camiones", command=lambda:self.menu_crud("Camion",ventana))
        btn2.pack(pady=7)
        btn3=Button(ventana,text="3.-Camionetas",command=lambda:self.menu_crud("Camioneta",ventana))
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

    def datos_coches(self,tipo,ventana):
        ventana.geometry("1000x1000")
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f"Agregar {tipo}")
        lbl_titulo.pack(pady=7)
        lbl_marca=Label(ventana,text="Ingrese la marca: ")
        lbl_marca.pack(pady=7)
        txt_marca=Entry(ventana,width=25,justify="left")
        txt_marca.pack(pady=7) 
        lbl_color=Label(ventana,text="Ingrese el color: ")
        lbl_color.pack(pady=7)
        txt_color=Entry(ventana,width=25,justify="left")
        txt_color.pack(pady=7)
        lbl_modelo=Label(ventana,text="Ingrese el modelo: ")
        lbl_modelo.pack(pady=7)
        txt_modelo=Entry(ventana,width=25,justify="left")
        txt_modelo.pack(pady=7)
        lbl_velocidad=Label(ventana,text="Ingrese la velocidad: ")
        lbl_velocidad.pack(pady=7)
        txt_velocidad=Entry(ventana,width=25,justify="left")
        txt_velocidad.pack(pady=7)
        lbl_caballaje=Label(ventana,text="Ingrese el caballaje: ")
        lbl_caballaje.pack(pady=7)
        txt_caballaje=Entry(ventana,width=25,justify="left")
        txt_caballaje.pack(pady=7)
        lbl_plazas=Label(ventana,text="Ingrese las plazas: ")
        lbl_plazas.pack(pady=7)
        txt_plazas=Entry(ventana,width=25,justify="left")
        txt_plazas.pack(pady=7)
        if tipo=="Coche":
            btnen=Button(ventana,text="Agregar",command=lambda:controlador.Controlador_coches.crear(txt_marca.get(),txt_color.get(),txt_modelo.get(),int(txt_velocidad.get()),int(txt_caballaje.get()),int(txt_plazas.get())))
            btnen.pack(pady=7)
            btnregr = Button(ventana, text="Regresar", command=lambda:self.menu_crud(ventana))
            btnregr.pack()
        elif tipo=="Camion":
            #eje,capacidadCarga
            lbl_eje=Label(ventana,text="Ingrese el eje: ")
            lbl_eje.pack(pady=7)
            txt_eje=Entry(ventana,width=25,justify="left")
            txt_eje.pack(pady=7)
            lbl_capacidadCarga=Label(ventana,text="Ingrese la capacidad de Carga: ")
            lbl_capacidadCarga.pack(pady=7)
            txt_capacidadCarga=Entry(ventana,width=25,justify="left")
            txt_capacidadCarga.pack(pady=7)
            #declaracion de variables:
            btnen=Button(ventana,text="Agregar",command=lambda:controlador.Controlador_camiones.crear(txt_marca.get(),txt_color.get(),txt_modelo.get(),int(txt_velocidad.get()),int(txt_caballaje.get()),int(txt_plazas.get()),int(txt_eje.get()),int(txt_capacidadCarga.get())))
            btnen.pack(pady=7)
            btnregr = Button(ventana, text="Regresar", command=lambda:self.menu_crud(ventana))
            btnregr.pack()
        elif tipo=="Camioneta":
            lbl_traccion=Label(ventana,text="Ingrese el traccion: ")
            lbl_traccion.pack(pady=7)
            txt_traccion=Entry(ventana,width=25,justify="left")
            txt_traccion.pack(pady=7)
            lbl_cerrada=Label(ventana,text="Ingrese si la camioneta es cerrada: ")
            lbl_cerrada.pack(pady=7)
            txt_cerrada=Entry(ventana,width=25,justify="left")
            txt_cerrada.pack(pady=7)
            btnen=Button(ventana,text="Agregar",command=lambda:controlador.Controlador_camiones.crear(txt_marca.get(),txt_color.get(),txt_modelo.get(),int(txt_velocidad.get()),int(txt_caballaje.get()),int(txt_plazas.get()),txt_traccion.get(),txt_cerrada.get()))
            btnen.pack(pady=7)
            btnregr = Button(ventana, text="Regresar", command=lambda:self.menu_crud(ventana))
            btnregr.pack()

    def actualizar(self,tipo,ventana):
        ventana.geometry("1000x1000")
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f"Actualizar {tipo}")
        lbl_titulo.pack(pady=7)
        lbl_id=Label(ventana,text=f"Ingrese el id de {tipo}: ")
        lbl_id.pack(pady=7)
        txt_id=Entry(ventana,width=25,justify="left")
        txt_id.pack(pady=7) 
        lbl_marca=Label(ventana,text="Ingrese la nueva marca: ")
        lbl_marca.pack(pady=7)
        txt_marca=Entry(ventana,width=25,justify="left")
        txt_marca.pack(pady=7) 
        lbl_color=Label(ventana,text="Ingrese el nuevo color: ")
        lbl_color.pack(pady=7)
        txt_color=Entry(ventana,width=25,justify="left")
        txt_color.pack(pady=7)
        lbl_modelo=Label(ventana,text="Ingrese el nuevo modelo: ")
        lbl_modelo.pack(pady=7)
        txt_modelo=Entry(ventana,width=25,justify="left")
        txt_modelo.pack(pady=7)
        lbl_velocidad=Label(ventana,text="Ingrese la nueva velocidad: ")
        lbl_velocidad.pack(pady=7)
        txt_velocidad=Entry(ventana,width=25,justify="left")
        txt_velocidad.pack(pady=7)
        lbl_caballaje=Label(ventana,text="Ingrese el nuevo caballaje: ")
        lbl_caballaje.pack(pady=7)
        txt_caballaje=Entry(ventana,width=25,justify="left")
        txt_caballaje.pack(pady=7)
        lbl_plazas=Label(ventana,text="Ingrese la nueva cantidad de plazas: ")
        lbl_plazas.pack(pady=7)
        txt_plazas=Entry(ventana,width=25,justify="left")
        txt_plazas.pack(pady=7)
        if tipo=="Coche":
            btnen=Button(ventana,text="Actualizar",command=lambda:controlador.Controlador_coches.actualizar(txt_marca.get(),txt_color.get(),txt_modelo.get(),int(txt_velocidad.get()),int(txt_caballaje.get()),int(txt_plazas.get()),txt_id.get()))
            btnen.pack(pady=7)
            btnregr = Button(ventana, text="Regresar", command=lambda:self.menu_crud(ventana))
            btnregr.pack()
        elif tipo=="Camion":
            #eje,capacidadCarga
            lbl_eje=Label(ventana,text="Ingrese el eje: ")
            lbl_eje.pack(pady=7)
            txt_eje=Entry(ventana,width=25,justify="left")
            txt_eje.pack(pady=7)
            lbl_capacidadCarga=Label(ventana,text="Ingrese la capacidad de Carga: ")
            lbl_capacidadCarga.pack(pady=7)
            txt_capacidadCarga=Entry(ventana,width=25,justify="left")
            txt_capacidadCarga.pack(pady=7)
            #declaracion de variables:
            btnen=Button(ventana,text="Actualizar",command=lambda:controlador.Controlador_camiones.actualizar(txt_marca.get(),txt_color.get(),txt_modelo.get(),int(txt_velocidad.get()),int(txt_caballaje.get()),int(txt_plazas.get()),int(txt_eje.get()),int(txt_capacidadCarga.get()),txt_id.get()))
            btnen.pack(pady=7)
            btnregr = Button(ventana, text="Regresar", command=lambda:self.menu_crud(ventana))
            btnregr.pack()
        elif tipo=="Camioneta":
            lbl_traccion=Label(ventana,text="Ingrese el traccion: ")
            lbl_traccion.pack(pady=7)
            txt_traccion=Entry(ventana,width=25,justify="left")
            txt_traccion.pack(pady=7)
            lbl_cerrada=Label(ventana,text="Ingrese si la camioneta es cerrada: ")
            lbl_cerrada.pack(pady=7)
            txt_cerrada=Entry(ventana,width=25,justify="left")
            txt_cerrada.pack(pady=7)
            btnen=Button(ventana,text="Actualizar",command=lambda:controlador.Controlador_camiones.actualizar(txt_marca.get(),txt_color.get(),txt_modelo.get(),int(txt_velocidad.get()),int(txt_caballaje.get()),int(txt_plazas.get()),txt_traccion.get(),txt_cerrada.get(),txt_id.get()))
            btnen.pack(pady=7)
            btnregr = Button(ventana, text="Regresar", command=lambda:self.menu_crud(ventana))
            btnregr.pack()

    def tabla(self,tipo,ventana):
        self.borrarPantalla(ventana)
        ventana.geometry("1000x700")
        titulos=""
        print(tipo)
        if tipo=="Coche":
            titulos=("id","marca","color","modelo","velocidad","caballaje","plazas")
            registros=controlador.Controlador_coches.mostrar()

        elif tipo=="Camion":
            titulos=("id","marca","color","modelo","velocidad","caballaje","plazas","eje","capacidad")
            registros=controlador.Controlador_camiones.mostrar()

        elif tipo=="Camioneta":
            titulos=("id","marca","color","modelo","velocidad","caballaje","plazas","traccion","cerrada")
            registros=controlador.Controlador_camionetas.mostrar()

        self.tabla = ttk.Treeview(ventana, columns=titulos, show='headings')
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for fila in registros:
            self.tabla.insert("", "end", values=fila)
        
        for col in titulos:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=150,anchor="center")
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)
        btnregr = Button(ventana, text="Regresar", command=lambda:self.menu_crud(ventana))
        btnregr.pack()


