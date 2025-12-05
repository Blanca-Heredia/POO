from tkinter import *
from view import vista

class App:
    def __init__(self, ventana):
        view = vista.Vistas()
        view.interfaz(ventana)

if __name__ == "__main__":
    ventana = Tk()
    ventana.geometry("1000x1000")
    ventana.title("Coches")
    app = App(ventana)
    ventana.mainloop()

