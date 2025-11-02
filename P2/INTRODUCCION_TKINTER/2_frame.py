from tkinter import *


ventana=Tk()
ventana.title("Marcos en tkinter")
#ventana.resizable(False,False) # Que no se pueda modificar el tamaño de la ventana
ventana.geometry("800x600")
marco1=Frame(ventana,width=600,height=400,bg="green", relief=SOLID, border=2)
marco2=Frame(marco1,width=300,height=150,bg="red", relief=SOLID, border=10)
marco1.pack_propagate(False)
marco2.pack(pady=17)
marco1.pack(pady=200)
ventana=mainloop()

