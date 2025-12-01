from tkinter import messagebox

def suma(numero1, numero2):
    resultado = numero1 + numero2
    messagebox.showinfo(icon="info", title="Suma", message=f"{numero1} + {numero2} = {resultado}")

def resta(numero1, numero2):
    resultado = numero1 - numero2
    messagebox.showinfo(icon="info", title="Resta", message=f"{numero1} - {numero2} = {resultado}")

def divi(numero1, numero2):
    resultado = numero1 / numero2
    messagebox.showinfo(icon="info", title="División", message=f"{numero1} / {numero2} = {resultado}")

def multi(numero1, numero2):
    resultado = numero1 * numero2
    messagebox.showinfo(icon="info", title="Multiplicación", message=f"{numero1} x {numero2} = {resultado}")

    
