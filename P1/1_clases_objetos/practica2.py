''' Ejercicio Practico #2 Modelar y Diagramar en POO '''

import os
os.system("cls")

#Clase coches 
class Coches:
    #Metodo constructor que inicializa los valores cuando se instancia un objeto de la clase
    def __init__(self, color, marca, velocidad):
        self.__color=color #atributos del objeto
        self.__marca=marca
        self.__velocidad=velocidad

#Metodos del objeto
    def acelerar(self,incremento):
        self.__velocidad=self.__velocidad+incremento
        return self.__velocidad
    
    def frenar(self,decremento):
        self.__velocidad=self.__velocidad-decremento
        return self.__velocidad
    
    def tocar_claxon(self):
        print("piii")

#Instanciar o crear objetos de la clase coches
coche1=Coches("Blanco", "Toyota", 220)
coche2=Coches("Amarillo","Nissan",180)

print(f"Los valores del objeto 1 son: {coche1.marca}, {coche1.color}, {coche1.velocidad}")
print(f"El coche 1 acelero de {coche1.velocidad} a {coche1.acelerar(50)}")
print(f"Los valores del objeto 2 son: {coche2.marca}, {coche2.color}, {coche2.velocidad}")
print(f"El coche 2 acelero de {coche2.velocidad} a {coche2.frenar(100)}")

''' 
Ejercicio Practico #2 Modelar y Diagramar en POO 
'''
import os
os.system("cls")

#Clase coches 
class Coches:
    #Metodo constructor que inicializa los valores cuando se instancia un objeto de la clase
    def _init_(self, color, marca, velocidad):
        self.__color=color #atributos del objeto
        self.__marca=marca
        self.__velocidad=velocidad

#Metodos del objeto
    def acelerar(self,incremento):
        self.__velocidad=self.__velocidad+incremento
        return self.__velocidad

    def frenar(self,decremento):
        self.__velocidad=self.__velocidad-decremento
        return self.__velocidad
    
    def tocar_claxon(self):
        print("Beep Beep")

#Instanciar o crear objetos de la clase coches
coche1=Coches("Blanco", "Toyota", 220)
coche2=Coches("Amarillo","Nissan",180)

print(coche1.acelerar(50))
print(coche1.tocar_claxon())
print(coche2.frenar(100))
 
#print(f"Los valores del objeto 1 son: {coche1.__marca}, {coche1.__color}, {coche1.__velocidad}")
#print(f"El coche 1 acelero de {coche1.__velocidad} a {coche1.__acelerar(50)}")
#print(f"Los valores del objeto 2 son: {coche2.__marca}, {coche2.__color}, {coche2.__velocidad}")
#print(f"El coche 2 acelero de {coche2.__velocidad} a {coche2.__frenar(100)}")