from tkinter import *
from tkinter import messagebox
from model import coches
from view import vista

class coches:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            mensaje=messagebox.showinfo(message=f"¡ Accion realizada con Éxito !",icon="info")
        else:
            mensaje=messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !",icon="info")
    
    @staticmethod
    def crear(marca,color,modelo,velocidad,caballaje,plazas):
        resultado=coches.Autos.insertar(marca,color,modelo,velocidad,caballaje,plazas)
        coches.respuesta_sql(resultado)

    @staticmethod
    def mostrar():
        registro=coches.Autos.consultar()
        return registro 
    
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,id):
        resultado=coches.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
        coches.respuesta_sql(resultado)

    @staticmethod
    def eliminar(id):
        respuesta=coches.Autos.eliminar(id)
        coches.respuesta_sql(id)

    @staticmethod
    def buscar(id):
        respuesta=coches.Autos.buscar(id)
        if len(respuesta)>0:
            if respuesta:
                coches.eliminar(id)
            else:
                mensaje=messagebox.showinfo(message=f"¡ hubo un error , vuelva a intentar por favor !",icon="info")
                return  
        else:
            mensaje=messagebox.showinfo(message=f"¡ La nota no existe , vuelva a intentar por favor !",icon="info")
            return
              
class camiones:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            mensaje=messagebox.showinfo(message=f"¡ Accion realizada con Éxito !",icon="info")
        else:
            mensaje=messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !",icon="info")

    @staticmethod
    def crear(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
        resultado=coches.Camiones.insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
        camiones.respuesta_sql(resultado)

    @staticmethod
    def mostrar():
        registro=coches.Camiones.consultar()
        return registro 
    
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id):
        resultado=coches.Camiones.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
        camiones.respuesta_sql(resultado)

    @staticmethod
    def eliminar(id):
        respuesta=coches.Camiones.eliminar(id)
        camiones.respuesta_sql(id)

    @staticmethod
    def buscar(id):
        respuesta=coches.Camiones.buscar(id)
        if len(respuesta)>0:
            if respuesta:
                camiones.eliminar(id)
            else:
                mensaje=messagebox.showinfo(message=f"¡ Hubo un error , vuelva a intentar por favor !",icon="info")
                return  
        else:
            mensaje=messagebox.showinfo(message=f"¡ La nota no existe , vuelva a intentar por favor !",icon="info")
            return
        
class camionetas:
    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            mensaje=messagebox.showinfo(message=f"¡ Accion realizada con Éxito !",icon="info")
        else:
            mensaje=messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !",icon="info")
    
    @staticmethod
    def crear(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        resultado=coches.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
        camionetas.respuesta_sql(resultado)

    @staticmethod
    def mostrar():
        registro=coches.Camionetas.consultar()
        return registro 
    
    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id):
        resultado=coches.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
        camionetas.respuesta_sql(resultado)

    @staticmethod
    def eliminar(id):
        respuesta=coches.Camionetas.eliminar(id)
        camionetas.respuesta_sql(id)
   



    