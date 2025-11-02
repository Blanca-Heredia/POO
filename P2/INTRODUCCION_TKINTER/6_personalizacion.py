from tkinter import *

ventana=Tk()

def cambiar_texto():
    etiqueta.config(text="POO con Python",
    cursor="spider",
    state='disabled'
    )

def regresar():
    etiqueta.config(text="Bienvenidos a Tkinter")

ventana.title("Personalizar widgets u objetos")
ventana.geometry("500x500")

etiqueta=Label(ventana,text="Bienvenidos a Tkinter")
etiqueta.config(
    bg="lightgreen",
    fg="darkgreen",
    width=50,
    height=4,
    font=("Helvetica",30,"italic"),
    relief=SOLID,
    border=2
)
etiqueta.pack(pady=25)

btn1=Button(ventana,text="Haz clic...",command=cambiar_texto)
btn1.config(
    fg="darkgreen",
    #width=50,
    #height=4,
    font=("Arial", 20, "bold"),
    relief=GROOVE,
    border=2,
    activeforeground="black",
    activebackground="lightgreen"
)
btn1.pack(pady=5)

btn2=Button(ventana,text="Regresar valores",command=regresar)
btn2.config(
    fg="black",
    #width=50,
    #height=4,
    font=("Arial", 20, "bold"),
    relief=GROOVE,
    border=2,
    activeforeground="red",
    activebackground="black"
)
btn2.pack(pady=5)

ventana.mainloop()