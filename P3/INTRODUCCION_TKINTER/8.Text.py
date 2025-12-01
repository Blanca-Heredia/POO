from tkinter import *

ventana=Tk()
ventana.title("Text")
ventana.geometry("600x400")


def comentario():
    comentarioObtenido=txt_comentario.get("1.0",END).strip()
    lbl_resultado.config(text=f"{comentarioObtenido}")

lbl_comentario=Label(ventana,text="Escriba su comentario: ").pack()
txt_comentario=Text(ventana)
txt_comentario.config(
    width=20,
    height=3,
    wrap='word'
)
txt_comentario.pack()

btn_comentario=Button(ventana,text="Mostrar contenido",command=comentario)
btn_comentario.pack()

lbl_resultado=Label(ventana,text="")
lbl_resultado.pack()

ventana.mainloop()