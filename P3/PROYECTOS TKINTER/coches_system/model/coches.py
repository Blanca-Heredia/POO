from conexionBD import *
from tkinter import messagebox

class Autos:
  def insertar(marca,color,modelo,velocidad,caballaje,plazas):
    try:
      cursor.execute(
        "insert into coches values(null,%s,%s,%s,%s,%s, %s)",
        (marca,color,modelo,velocidad,caballaje,plazas))
      conexion.commit()
      return True
    except:
      return False       
  @staticmethod
  def consultar():
    try:
      cursor.execute(
        "select * from coches"
      )
      return cursor.fetchall()
    except:    
      return []
  @staticmethod
  def actualizar(marca, color, modelo,velocidad,caballaje,plazas,id):
    try:
      cursor.execute(
        "update coches set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s where id=%s",
        (marca, color, modelo,velocidad,caballaje,plazas,id)
      )
      conexion.commit()
      return True
    except: 
      return False
  @staticmethod
  def eliminar(id):
    try:
      cursor.execute(
        "delete from coches where id=%s",
        (id,)
      ) 
      conexion.commit() 
      return True  
    except:    
      return False   

  def buscar(id):
    try:
      cursor.execute(
        "select * from coches where id=%s",
        (id,)
      )
      return cursor.fetchall()
    except: 
      return []


class Camiones: 
  @staticmethod
  def insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
    try:
      cursor.execute(
        "insert into camiones values(null,%s,%s,%s,%s,%s, %s,%s,%s)",
        (marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
      )
      conexion.commit()
      return True
    except:
      return False
    
  @staticmethod
  def consultar():
    try:
      cursor.execute(
        "select * from camiones"
      )
      return cursor.fetchall()
    except:    
      return []

  @staticmethod
  def actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id):
    try:
      cursor.execute(
        "update camiones set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,eje=%s,capacidadCarga=%s where id=%s",
        (marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
      )
      conexion.commit()
      return True
    except: 
      return False

  @staticmethod
  def eliminar(id):
    try:
      cursor.execute(
        "delete from camiones where id=%s",
        (id,)
      ) 
      conexion.commit() 
      return True  
    except:    
      return False     

  def buscar(id):
    try:
      cursor.execute(
        "select * from camiones where id=%s",
        (id,)
      )
      return cursor.fetchall()
    except: 
      return []


class Camionetas:  
  @staticmethod
  def insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
    try:
      cursor.execute(
        "insert into camionetas values(null,%s,%s,%s,%s,%s, %s,%s,%s)",
        (marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
      )
      conexion.commit()
      return True
    except:
      return False
    
  @staticmethod
  def consultar():
    try:
      cursor.execute(
        "select * from camionetas"
      )
      return cursor.fetchall()
    except:    
      return []

  @staticmethod
  def actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id):
    try:
      cursor.execute(
        "update camionetas set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,traccion=%s,cerrada=%s where id=%s",
        (marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
      )
      conexion.commit()
      return True
    except: 
      return False

  @staticmethod
  def respuesta_sql(respuesta):
        if respuesta:
            mensaje=messagebox.showinfo(message=f"¡ Accion realizada con Éxito !",icon="info")
        else:
            mensaje=messagebox.showinfo(message=f"¡ No fue posible realizar la acción, vuelva a intentar por favor !",icon="info")  
  
  @staticmethod
  def eliminar(id):
    try:
      cursor.execute(
        "delete from camionetas where id=%s",
        (id,)
      ) 
      conexion.commit() 
      return True  
    except:    
      return False  

  def buscar(id):
    try:
      cursor.execute(
        "select * from camionetas where id=%s",
        (id,)
      )
      return cursor.fetchall()
    except: 
      return []
    