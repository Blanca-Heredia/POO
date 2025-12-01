from tkinter import messagebox
from model import usuario, nota
from view import interfaz 

class Controlador:

    @staticmethod
    def registrar(nombre, apellidos, email, password):
        resultado = usuario.Usuario.registrar(nombre, apellidos, email, password)
        Controlador.respuesta_sql("Registrar usuario", resultado)

    @staticmethod
    def login(email, password, ventana):
        registro = usuario.Usuario.iniciar_sesion(email, password)
        if registro:
            id_user = registro[0] 
            nombre = registro[1]
            apellidos = registro[2]
            
            messagebox.showinfo(icon="info",
            message=f"{nombre} {apellidos} Haz iniciado sesion correctamente")
            
            interfaz.Vistas.menu_notas(ventana, id_user, nombre, apellidos)
        else:
            messagebox.showinfo(icon="info",
            message="Credenciales incorrectas, por favor intenta de nuevo")

    @staticmethod
    def crear(id_usuario, titulo, descripcion):
        resultado = nota.Nota.crear(id_usuario, titulo, descripcion) 
        Controlador.respuesta_sql("Crear Notas", resultado)

    @staticmethod
    def eliminar(id_nota):
        resultado = nota.Nota.eliminar(id_nota)
        Controlador.respuesta_sql("Eliminar Notas", resultado)

    @staticmethod
    def actualizar(id_nota, titulo, descripcion):
        resultado = nota.Nota.actualizar(id_nota, titulo, descripcion)
        Controlador.respuesta_sql("Actualizar Nota", resultado)

    @staticmethod
    def mostrar(id_usuario):
        registros = nota.Nota.mostrar(id_usuario)
        return registros if registros else []

    @staticmethod
    def respuesta_sql(titulo, respuesta):
        if respuesta:
            messagebox.showinfo(title=titulo, message="Acción realizada con éxito", icon="info")
        else:
            messagebox.showinfo(title=titulo, message="No fue posible realizar la acción.", icon="info")