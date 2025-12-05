from tkinter import messagebox
from model.cochesBD import Autos, Camionetas, Camiones

class Controlador:

    @staticmethod
    def insertar_auto(marca,color,modelo,velocidad,caballaje,plazas):
        r=Autos.insertar(marca,color,modelo,velocidad,caballaje,plazas)
        Controlador.respuesta_sql("Insertar Auto",r)

    @staticmethod
    def consultar_auto(id):
        if id=="all": return Autos.consultar()
        else: return Autos.consultarID(id)

    @staticmethod
    def modificar_auto(marca,color,modelo,velocidad,caballaje,plazas,id):
        r=Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
        Controlador.respuesta_sql("Modificar Auto",r)

    @staticmethod
    def eliminar_auto(id):
        r=Autos.eliminar(id)
        Controlador.respuesta_sql("Eliminar Auto",r)



    @staticmethod
    def insertar_camioneta(marca,color,modelo,velocidad,caballaje,plazas,traccion):
        r=Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion)
        Controlador.respuesta_sql("Insertar Camioneta",r)

    @staticmethod
    def consultar_camioneta(id):
        if id=="all": return Camionetas.consultar()
        else: return Camionetas.consultarID(id)

    @staticmethod
    def modificar_camioneta(marca,color,modelo,velocidad,caballaje,plazas,traccion,id):
        r=Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,id)
        Controlador.respuesta_sql("Modificar Camioneta",r)

    @staticmethod
    def eliminar_camioneta(id):
        r=Camionetas.eliminar(id)
        Controlador.respuesta_sql("Eliminar Camioneta",r)



    @staticmethod
    def insertar_camion(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad):
        r=Camiones.insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad)
        Controlador.respuesta_sql("Insertar Camión",r)

    @staticmethod
    def consultar_camion(id):
        if id=="all": return Camiones.consultar()
        else: return Camiones.consultarID(id)

    @staticmethod
    def modificar_camion(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad,id):
        r=Camiones.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad,id)
        Controlador.respuesta_sql("Modificar Camión",r)

    @staticmethod
    def eliminar_camion(id):
        r=Camiones.eliminar(id)
        Controlador.respuesta_sql("Eliminar Camión",r)



    @staticmethod
    def respuesta_sql(t,res):
        if res: messagebox.showinfo(t,"Acción realizada con éxito")
        else: messagebox.showerror(t,"No se pudo completar la acción")
