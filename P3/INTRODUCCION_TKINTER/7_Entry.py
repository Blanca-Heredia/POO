from tkinter import *

def acceso():
    lbl_resultado.config(text=f"Hola {nombre.get()} bienvenid@")

def borrar():
    txt_nombre.delete(0,END)
    txt_contraseña.delete(0,END)
    txt_nombre.focus()
    lbl_resultado.config(text="")
    lbl_resultado.destroy()

def salir():
    ventana.quit()

ventana=Tk()
ventana.title("Entry")
ventana.geometry("800x600")
from tkinter import *

ventana=Tk()
ventana.title("Distribución de widgets en pantalla")
ventana.geometry("600x400")

'''
#Con pack()  con side=EFT o RIGHT"
Label(ventana,text="Nombre").pack(anchor="nw",side="top",padx=5,pady=5)
Entry(ventana).pack(anchor="nw",side="top",padx=5,pady=5)
Label(ventana,text="Contraseña").pack(anchor="nw",side="top",padx=5,pady=5)
Entry(ventana).pack(anchor="nw",side="top",padx=5,pady=5)
'''

#Con grid 
Label(ventana,text="Nombre").grid(row=0,column=0,padx=5,pady=5)
Entry(ventana).grid(row=0,column=1,padx=5,pady=5)
Label(ventana,text="Contraseña").grid(row=1,column=0,padx=5,pady=5)
Entry(ventana).grid(row=1,column=1,padx=5,pady=5)






ventana.mainloop()

marco=Frame(ventana)
marco.config(
    width=800,
    height=300,
    bg="silver",
)
marco.pack_propagate(False)
marco.pack()

marco_botones=Frame(ventana)
marco_botones.config(
    width=800,
    height=300,
    bg="silver",
)
marco_botones.pack_propagate(False)
marco_botones.pack()



lbl_nombre=Label(marco,text="Ingresar su nombre:")
lbl_nombre.config(
    bg="silver"
)
lbl_nombre.grid(row=0,column=0,padx=5,pady=5)

nombre=StringVar()
txt_nombre=Entry(marco,textvariable=nombre)
txt_nombre.focus()
txt_nombre.grid(row=0,column=1,padx=5,pady=5)

lbl_contraseña=Label(marco,text="Contraseña")
lbl_contraseña.config(
    bg="silver"
)
lbl_contraseña.grid(row=1,column=2,padx=5,pady=5)
contraseña=StringVar()
txt_contraseña=Entry(marco,textvariable=contraseña,show="*")

lbl_contraseña.grid(row=1,column=2,padx=5,pady=5)
lbl_contraseña.pack()


btn_saludar=Button(marco_botones,text="Aceptar",command=acceso)
btn_saludar.grid(row=0,column=0,padx=5,pady=5)

lbl_resultado=Label(ventana,text="")
lbl_resultado.pack()

btn_borrar=Button(marco_botones,text="Borrar",command=borrar)
btn_borrar.grid(row=0,column=1,padx=5,pady=5)


btn_cerrar=Button(marco_botones,text="Salir",command=salir)
btn_cerrar.grid(row=0,column=2,padx=5,pady=5)








ventana.mainloop()



