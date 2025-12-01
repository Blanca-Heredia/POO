from tkinter import *
# ...existing code...
from PIL import Image, ImageTk

ventana=Tk()
ventana.title("Imagenes Pillow")
ventana.geometry("650x500")

# Obtener la ruta absoluta del directorio donde está este archivo .py
#ruta_base = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo de imagen
#ruta_imagen = os.path.join(ruta_base, "logo_utd.png")


def mensaje(tipo):
    resul.config(text=f"{tipo}")

# ruta de la imagen
path = r"C:\Users\Gustavo\OneDrive\Documentos\PROGRAMACION OBJETOS\P3\INTRODUCCION_TKINTER\logo_utd.png"

# usar Pillow correctamente
pil_img = Image.open(path)
imagen = ImageTk.PhotoImage(pil_img)

#incluir o mostrar la imagen dentro de un label y button
etiq=Label(ventana,image=imagen)
etiq.pack()

btn=Button(ventana,image=imagen,command=lambda: mensaje("Hola Python"))
btn.pack()
resul=Label(ventana,text="")
resul.pack()

ventana.mainloop()