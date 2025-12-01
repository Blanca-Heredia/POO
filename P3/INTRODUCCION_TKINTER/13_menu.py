from tkinter import *

def notificacion(tipo):
    etiq.config(text=tipo)   

ventana=Tk()
ventana.title("Menu")
ventana.geometry("500x500")

menubar=Menu(ventana)
ventana.config(menu=menubar)

archivoMenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label="Archivo",menu=archivoMenu)
archivoMenu.add_command(label="Nuevo archivo",command=lambda: notificacion("Nuevo archivo"))
archivoMenu.add_command(label="Guardar archivo",command=lambda: notificacion("Guardar archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=ventana.quit)

edicionMenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label="Edicion",menu=edicionMenu)
edicionMenu.add_command(label="Copiar",command=lambda: notificacion("Copiado"))
edicionMenu.add_command(label="Pegar",command=lambda: notificacion("Pegado"))
edicionMenu.add_separator()
edicionMenu.add_command(label="Salir",command=ventana.quit)

etiq=Label(ventana,text="")
etiq.pack()

ventana.mainloop()