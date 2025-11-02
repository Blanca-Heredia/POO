from tkinter import *

ventana=Tk()
ventana.title("Ventana mainloop")
ventana.geometry("600x400")
marco1=Frame(ventana,width=600,height=50,bg="#FF0000",border=2,relief="raised")
marco2=Frame(ventana,width=600,height=50,bg="#FF7B00",border=2,relief="raised")
marco3=Frame(ventana,width=600,height=50,bg="#FFE100",border=2,relief="raised")
marco4=Frame(ventana,width=600,height=50,bg="#1EFF00",border=2,relief="raised")
marco5=Frame(ventana,width=600,height=50,bg="#001AFF",border=2,relief="raised")
marco6=Frame(ventana,width=600,height=50,bg="#A203AA",border=2,relief="raised")

marco1.pack()
marco2.pack()
marco3.pack()
marco4.pack()
marco5.pack()
marco6.pack()
ventana=mainloop()