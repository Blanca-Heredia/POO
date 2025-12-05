from conexionBD import cursor, conexion

class Autos:
    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas):
        try:
            cursor.execute("INSERT INTO autos VALUES(NULL,%s,%s,%s,%s,%s,%s)",(marca,color,modelo,velocidad,caballaje,plazas))
            conexion.commit()
            return True
        except: return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM autos")
            return cursor.fetchall()
        except: return []

    @staticmethod
    def consultarID(id):
        try:
            cursor.execute("SELECT * FROM autos WHERE id=%s",(id,))
            return cursor.fetchall()
        except: return []

    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,id):
        try:
            cursor.execute("UPDATE autos SET marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s WHERE id=%s",(marca,color,modelo,velocidad,caballaje,plazas,id))
            conexion.commit()
            return True
        except: return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM autos WHERE id=%s",(id,))
            conexion.commit()
            return True
        except: return False


class Camionetas:
    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion):
        try:
            cursor.execute("INSERT INTO camionetas VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,0)",(marca,color,modelo,velocidad,caballaje,plazas,traccion))
            conexion.commit()
            return True
        except: return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camionetas")
            return cursor.fetchall()
        except: return []

    @staticmethod
    def consultarID(id):
        try:
            cursor.execute("SELECT * FROM camionetas WHERE id=%s",(id,))
            return cursor.fetchall()
        except: return []

    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,id):
        try:
            cursor.execute("UPDATE camionetas SET marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,traccion=%s WHERE id=%s",(marca,color,modelo,velocidad,caballaje,plazas,traccion,id))
            conexion.commit()
            return True
        except: return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM camionetas WHERE id=%s",(id,))
            conexion.commit()
            return True
        except: return False



class Camiones:
    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad):
        try:
            cursor.execute("INSERT INTO camiones VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)",(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad))
            conexion.commit()
            return True
        except: return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camiones")
            return cursor.fetchall()
        except: return []

    @staticmethod
    def consultarID(id):
        try:
            cursor.execute("SELECT * FROM camiones WHERE id=%s",(id,))
            return cursor.fetchall()
        except: return []

    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad,id):
        try:
            cursor.execute("UPDATE camiones SET marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,eje=%s,capacidadcarga=%s WHERE id=%s",(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad,id))
            conexion.commit()
            return True
        except: return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM camiones WHERE id=%s",(id,))
            conexion.commit()
            return True
        except: return False
