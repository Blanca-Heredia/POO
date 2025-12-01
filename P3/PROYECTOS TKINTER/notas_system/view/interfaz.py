from tkinter import *
from model import *
from tkinter import messagebox
from controller import controlador

id_usuario_activo = None
nombre_activo = None
apellidos_activos = None


class Vistas:
    def __init__(self, ventana):
        ventana.title("Gestion de notas")
        ventana.geometry("700x500")
        ventana.resizable(False, False)
        self.interfaz(ventana)

    @staticmethod
    def interfaz(ventana):
        Vistas.borrarPantalla(ventana)
        txt_mp = Label(ventana, text="Menu Principal")
        txt_mp.pack(pady=7)
        btn1 = Button(ventana, text="1.-Registro", command=lambda: Vistas.registro(ventana))
        btn1.pack(pady=7)
        btn2 = Button(ventana, text="2.-Login", command=lambda: Vistas.login(ventana))
        btn2.pack(pady=7)
        btn3 = Button(ventana, text="3.-Salir", command=ventana.quit)
        btn3.pack(pady=7)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def registro(ventana):
        Vistas.borrarPantalla(ventana)
        txt_re = Label(ventana, text="Registro")
        txt_re.pack(pady=7)

        lbl_n = Label(ventana, text="¿Cual es tu nombre?")
        lbl_n.pack(pady=7)
        txt_n = Entry(ventana, width=25, justify="left")
        txt_n.pack(pady=7)

        lbl_a = Label(ventana, text="¿Cuales son tus apellidos?")
        lbl_a.pack(pady=7)
        txt_a = Entry(ventana, width=25, justify="left")
        txt_a.pack(pady=7)

        lbl_e = Label(ventana, text="Ingresa tu email")
        lbl_e.pack(pady=7)
        txt_e = Entry(ventana, width=25, justify="left")
        txt_e.pack(pady=7)

        lbl_c = Label(ventana, text="Ingresa tu contraseña")
        lbl_c.pack(pady=7)
        txt_c = Entry(ventana, width=25, justify="left", show="*")
        txt_c.pack(pady=7)

        btnre = Button(ventana, text="Registrar", command=lambda: controlador.Controlador.registrar(txt_n.get(), txt_a.get(), txt_e.get(), txt_c.get()))
        btnre.pack(pady=7)

        btnreg = Button(ventana, text="Regresar", command=lambda: Vistas.interfaz(ventana))
        btnreg.pack()

    @staticmethod
    def login(ventana):
        Vistas.borrarPantalla(ventana)
        txt_in = Label(ventana, text="Inicio de Sesion")
        txt_in.pack(pady=7)

        lbl_em = Label(ventana, text="Ingresa tu email")
        lbl_em.pack(pady=7)
        txt_em = Entry(ventana, width=25, justify="left")
        txt_em.pack(pady=7)

        lbl_con = Label(ventana, text="Ingresa tu contraseña")
        lbl_con.pack(pady=7)
        txt_con = Entry(ventana, width=25, justify="left", show="*")
        txt_con.pack(pady=7)

        btnen = Button(ventana, text="Entrar", command=lambda: controlador.Controlador.login(txt_em.get(), txt_con.get(), ventana))
        btnen.pack(pady=7)

        btnregr = Button(ventana, text="Regresar", command=lambda: Vistas.interfaz(ventana))
        btnregr.pack()


    @staticmethod
    def menu_notas(ventana, id_user, nombre, apellidos):
        Vistas.borrarPantalla(ventana)
        
        global id_usuario_activo, nombre_activo, apellidos_activos
        id_usuario_activo = id_user
        nombre_activo = nombre
        apellidos_activos = apellidos

        txt_ti = Label(ventana, text=f"Bienvenido {nombre} {apellidos} has iniciado sesion")
        txt_ti.pack(pady=7)

        btnc = Button(ventana, text="1.-Crear", command=lambda: Vistas.crear_nota(ventana))
        btnc.pack(pady=7)
        btnm = Button(ventana, text="2.-Mostrar", command=lambda: Vistas.mostrar(ventana))
        btnm.pack(pady=7)
        btncam = Button(ventana, text="3.-Cambiar", command=lambda: Vistas.cambiar_nota(ventana))
        btncam.pack(pady=7)
        btne = Button(ventana, text="4.-Eliminar", command=lambda: Vistas.borrar_nota(ventana))
        btne.pack(pady=7)
        btnv = Button(ventana, text="5.-Regresar", command=lambda: Vistas.login(ventana))
        btnv.pack(pady=7)

    @staticmethod
    def crear_nota(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_cn = Label(ventana, text="Crear nota")
        lbl_cn.pack(pady=7)

        lbl_tit = Label(ventana, text="Titulo")
        lbl_tit.pack(pady=7)
        txt_tit = Entry(ventana, width=25, justify="left")
        txt_tit.pack(pady=7)

        lbl_de = Label(ventana, text="Descripcion")
        lbl_de.pack(pady=7)
        txt_de = Entry(ventana, width=25, justify="left")
        txt_de.pack(pady=7)

        btngr = Button(ventana, text="Guardar", command=lambda: controlador.Controlador.crear(id_usuario_activo, txt_tit.get(), txt_de.get()))
        btngr.pack(pady=7)

        btnregre = Button(ventana, text="Regresar",command=lambda: Vistas.menu_notas(ventana, id_usuario_activo, nombre_activo, apellidos_activos))
        btnregre.pack()

    @staticmethod
    def mostrar(ventana):
        Vistas.borrarPantalla(ventana)

        txtm = Label(ventana, text=f"{nombre_activo} {apellidos_activos} tus notas son")
        txtm.pack(pady=7)

        filas = ""
        registros = controlador.Controlador.mostrar(id_usuario_activo)

        if registros and len(registros) > 0:
            num_notas = 1
            for fila in registros:
                filas += f"Nota: {num_notas}\nID: {fila[0]} Titulo: {fila[2]}\nFecha: {fila[4]} Descripcion: {fila[3]}\n\n"
                num_notas += 1
        else:
            filas = "No existen notas para este usuario"

        lblr = Label(ventana, text=f"{filas}", justify="left")
        lblr.pack(pady=7)

        btnv = Button(ventana, text="5.-Regresar",command=lambda: Vistas.menu_notas(ventana, id_usuario_activo, nombre_activo, apellidos_activos))
        btnv.pack(pady=7)
    @staticmethod
    def cambiar_nota(ventana):
        Vistas.borrarPantalla(ventana)
        lbl_cn = Label(ventana, text=f"{nombre_activo} {apellidos_activos} vamos a modificar una nota")
        lbl_cn.pack(pady=7)
        
        lbl_id = Label(ventana, text="ID de la nota a modificar ")
        lbl_id.pack(pady=7)
        txt_id = Entry(ventana, width=25, justify="left")
        txt_id.pack(pady=7)

        lbl_tit = Label(ventana, text="Nuevo Titulo")
        lbl_tit.pack(pady=7)
        txt_tit = Entry(ventana, width=25, justify="left")
        txt_tit.pack(pady=7)

        lbl_de = Label(ventana, text="Nueva Descripcion")
        lbl_de.pack(pady=7)
        txt_de = Entry(ventana, width=25, justify="left")
        txt_de.pack(pady=7)

        btnact = Button(ventana, text="Actualizar", command=lambda: controlador.Controlador.actualizar(txt_id.get(), txt_tit.get(), txt_de.get()))
        btnact.pack(pady=7)

        btnregre = Button(ventana, text="Regresar", command=lambda: Vistas.menu_notas(ventana, id_usuario_activo, nombre_activo, apellidos_activos))
        btnregre.pack()

    @staticmethod
    def borrar_nota(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_cn = Label(ventana, text=f"{nombre_activo} {apellidos_activos} vamos a eliminar una nota")
 
        lbl_cn.pack(pady=7)
        lbl_id = Label(ventana, text="ID de la nota a eliminar")
        lbl_id.pack(pady=7)
        txt_id = Entry(ventana, width=25, justify="left")
        txt_id.pack(pady=7)

        btneli = Button(ventana, text="Eliminar", command=lambda: controlador.Controlador.eliminar(txt_id.get()))
        btneli.pack(pady=7)

        btnregre = Button(ventana, text="Regresar", command=lambda: Vistas.menu_notas(ventana, id_usuario_activo, nombre_activo, apellidos_activos))
        btnregre.pack()


