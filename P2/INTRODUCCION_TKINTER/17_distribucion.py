from tkinter import *

ventana=Tk()
ventana.title("Distribución de widgets en pantalla")
#ventana.geometry("600x400")



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