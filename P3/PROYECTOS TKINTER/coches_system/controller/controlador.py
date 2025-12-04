from tkinter import *
from tkinter import messagebox
from model import coches 
from view import vista 


class Coches:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            mensaje = messagebox.showinfo(message=f"¡ Accion realizada con Éxito !", icon="info")
        else:
            mensaje = messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !", icon="info")
    
    @staticmethod
    def crear(marca, color, modelo, velocidad, caballaje, plazas):
        resultado = coches.Autos.insertar(marca, color, modelo, velocidad, caballaje, plazas)
        Coches.respuesta_sql(resultado)

    @staticmethod
    def mostrar():
        registro = coches.Autos.consultar()
        return registro 
    
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, id):
        resultado = coches.Autos.actualizar(marca, color, modelo, velocidad, caballaje, plazas, id)
        Coches.respuesta_sql(resultado)

    @staticmethod
    def eliminar(id):
        respuesta = coches.Autos.eliminar(id)
        Coches.respuesta_sql(respuesta)

    @staticmethod
    def buscar(id):
        respuesta = coches.Autos.buscar(id)
        if len(respuesta) > 0:
            Coches.eliminar(id)
        else:
            messagebox.showinfo(message=f"¡ El coche no existe , vuelva a intentar por favor !", icon="info")
            return 
            
class Camiones:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            mensaje = messagebox.showinfo(message=f"¡ Accion realizada con Éxito !", icon="info")
        else:
            mensaje = messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !", icon="info")

    @staticmethod
    def crear(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        resultado = coches.Camiones.insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga)
        Camiones.respuesta_sql(resultado)

    @staticmethod
    def mostrar():
        registro = coches.Camiones.consultar()
        return registro 
    
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id):
        resultado = coches.Camiones.actualizar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id)
        Camiones.respuesta_sql(resultado)

    @staticmethod
    def eliminar(id):
        respuesta = coches.Camiones.eliminar(id)
        Camiones.respuesta_sql(respuesta)

    @staticmethod
    def buscar(id):
        respuesta = coches.Camiones.buscar(id)
        if len(respuesta) > 0:
            Camiones.eliminar(id)
        else:
            messagebox.showinfo(message=f"¡ El camión no existe , vuelva a intentar por favor !", icon="info")
            return 
        
class Camionetas:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            mensaje = messagebox.showinfo(message=f"¡ Accion realizada con Éxito !", icon="info")
        else:
            mensaje = messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !", icon="info")
    
    @staticmethod
    def crear(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        resultado = coches.Camionetas.insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
        Camionetas.respuesta_sql(resultado)

    @staticmethod
    def mostrar():
        registro = coches.Camionetas.consultar()
        return registro 
    
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id):
        resultado = coches.Camionetas.actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id)
        Camionetas.respuesta_sql(resultado)

    @staticmethod
    def eliminar(id):
        respuesta = coches.Camionetas.eliminar(id)
        Camionetas.respuesta_sql(respuesta)

    @staticmethod
    def buscar(id):
        respuesta = coches.Camionetas.buscar(id)
        if len(respuesta) > 0:
            Camionetas.eliminar(id)
        else:
            messagebox.showinfo(message=f"¡ La camioneta no existe , vuelva a intentar por favor !", icon="info")
            return