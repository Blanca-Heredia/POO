import conexionBD as db
from tkinter import messagebox

class Operaciones:
    @staticmethod
    def insertar(numero1, numero2, signo, resultado):
            sql = "INSERT INTO operaciones (id, fecha, numero1, numero2, signo, resultado) VALUES (NULL, NOW(), %s, %s, %s, %s)"
            db.cursor.execute(sql, (numero1, numero2, signo, resultado))
            db.conexion.commit()
    
            print(f"Error insertar: ")
            return False

    @staticmethod
    def consultar(id=None):
        try:
            if id is None:
                db.cursor.execute("SELECT * FROM operaciones")
            else:
                db.cursor.execute("SELECT * FROM operaciones WHERE id = %s", (id,))
            return db.cursor.fetchall()
        except Exception as e:
            print(f"Error consultar: {e}")
            return []

    @staticmethod
    def actualizar(numero1, numero2, signo, resultado, id):
        try:
            sql = """
                UPDATE operaciones
                SET numero1 = %s, numero2 = %s, signo = %s, resultado = %s, fecha = NOW()
                WHERE id = %s
            """
            db.cursor.execute(sql, (numero1, numero2, signo, resultado, id))
            db.conexion.commit()
            return True
        except Exception as e:
            messagebox.showinfo(message="Error actualizar: ")
            return False


    @staticmethod
    def eliminar(id):
            if id:
                db.cursor.execute("DELETE FROM operaciones WHERE id = %s", (id,))
                db.conexion.commit()
            else:
                messagebox.showinfo(message="No fue posible realizar la acción.", icon="info")
    
    @staticmethod
    def buscar_id(id):
            db.cursor.execute("SELECT * FROM operaciones WHERE id = %s", (id,))
            registro = db.cursor.fetchone() 
            if registro:
                return registro
            else:
                messagebox.showinfo(message="No hay ningun id", icon="info")

   