#Encapsular Es un pilar de la POO que permite indicar cual es la manera de como poder utilizar los atributos y metodos de una clase a la hora de usar en objetos o en herencia

import os
os.system("cls")

class Clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="Soy un atrubuto protegido"
    __atributo_privado="Soy un atributo privado"

def __init__(self,color,tamanio):
    self._color=color
    self._tamanio=tamanio

@property
def color(self):
    return self._color

@color.setter
def color(self,color):
    self._color=color
 
@property
def tamanio(self):
    return self._tamanio

@tamanio.setter
def tamanio(self,tamanio):
    self._tamanio=tamanio

@property
def atributopublico(self):
    return self.atributo_publico 

@atributopublico.setter
def atributopublico(self,atributo_publico):
    self.atributo_publico=atributo_publico

@property
def atributo_protegido(self):
    return self.atributo_protegido 

@atributo_protegido.setter
def atributo_protegido(self,atributo_protegido):
    self.atributo_protegido=atributo_protegido


@property
def atributo_privado(self):
    return self.atributo_privado 

@atributo_privado.setter
def atributo_privado(self,atributo_privado):
    self.atributo_privado=atributo_privado

#Utilizar la clase
objeto=Clase("Rojo","Grande")
print(objeto.colo,objeto.tamanio)
#No es una buena practica acceder a los valores directamente print(objeto.atributo_publico)
#print(objeto._atributo_protegido)
print(objeto.__atributo_privado)
print(objeto.atributopublico)
print(objeto._atributo_protegido)
objeto.color="Amarillo"
print(objeto.color)




