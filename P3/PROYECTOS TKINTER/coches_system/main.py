from tkinter import *
from view import vista



class App:
    def __init__(self,ventana):
        view=vista.Vistas(ventana)
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()