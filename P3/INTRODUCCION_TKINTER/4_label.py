from tkinter import *

ventana=Tk()
ventana.title("Ventana mainloop")
ventana.geometry("600x400")
marco1=Frame(ventana,width=600,height=50,bg="green",border=2,relief="raised")
marco1.pack_propagate(False)
marco1.pack()
marco2=Frame(ventana,width=600,height=50,bg="#FFE100",border=2,relief="raised")
marco2.pack_propagate(False)
marco2.pack()
marco3=Frame(ventana,width=600,height=50,bg="#1EFF00",border=2,relief="raised")
marco3.pack_propagate(False)
marco3.pack()
marco4=Frame(ventana,width=600,height=50,bg="#001AFF",border=2,relief="raised")
marco4.pack_propagate(False)
marco4.pack()


#Etiquetas
etiqueta1=Label(marco1,text="Blanca Marlene Heredia Nuñez").pack(pady=10,bg="green")
etiqueta2=Label(marco2,text="Universidad Tecnologica de Durango").pack(pady=10)
etiqueta3=Label(marco3,text="Tecnologias de la Informacion").pack(pady=10)
etiqueta4=Label(marco4,text="Desarrollo de SW multiplataforma").pack(pady=10)



ventana.mainloop()