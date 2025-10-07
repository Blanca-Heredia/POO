'''  Practica #1 Implementar paradigma estructurado VS 00  
     Crear un programa que obtenga el area de un rectangulo
'''
import os
os.system("cls")

#1-.Estructurado
def area(base, altura):
    return base * altura
base=float(input("Escribe la base: "))
altura=float(input("Escribe la altura: "))
print(f"El área es: {area(base, altura)}")

#2-.OO
class AreaRectangulo:
  def area(self, base, altura):
    return base * altura  

rectangulo=AreaRectangulo()  #Instanciar un objeto de la clase "AreaRectangulo"
print(f"El área es: {rectangulo.area(base, altura)}")

class AreaRectangulo:
  def __init__(self, base, altura):
    self.base=base
    self.altura=altura

  def area(self):
    return self.base * self.altura  

rectangulo=AreaRectangulo(base, altura)  #Instanciar un objeto de la clase "AreaRectangulo"
print(f"El área es: {rectangulo.area}")