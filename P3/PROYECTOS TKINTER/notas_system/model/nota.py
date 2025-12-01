from conexionBD import *

class Nota:  
    @staticmethod
    def crear(usuario_id, titulo, descripcion):
        try:
            cursor.execute(
                "INSERT INTO notas (usuario_id, titulo, descripcion, fecha) VALUES (%s,%s,%s,NOW())",
                (usuario_id, titulo, descripcion)
            )
            conexion.commit()
            return True
        except Exception as e:
            print("ERROR AL CREAR NOTA:", e)
            return False

    @staticmethod
    def mostrar(usuario_id):
        try:
            cursor.execute(
                "SELECT * FROM notas WHERE usuario_id=%s",
                (usuario_id,)
            )
            return cursor.fetchall()
        except Exception as e:    
            print("ERROR AL MOSTRAR:", e)
            return []

    @staticmethod
    def actualizar(id, titulo, descripcion):
        try:
            cursor.execute(
                "UPDATE notas SET titulo=%s,descripcion=%s WHERE id=%s",
                (titulo,descripcion,id)
            )
            conexion.commit()
            return True
        except Exception as e: 
            print("ERROR AL ACTUALIZAR:", e)
            return False
    
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "DELETE FROM notas WHERE id=%s",
                (id,)
            ) 
            conexion.commit() 
            return True  
        except Exception as e:    
            print("ERROR AL ELIMINAR:", e)
            return False
