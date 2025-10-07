import os
os.system("cls")

class coches:
 #metodo constructor, con este metodo se inicializa un objeto cuando es creado con valores iniciales
  def __init__(self):
    self.__marca=""
    self.__color=""
    self.__modelo=""
    self.__velocidad=0
    self.__caballaje=0 
    self.__plazas=0

  def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
    self.__marca=marca
    self.__color=color
    self.__modelo=modelo
    self.__velocidad=velocidad
    self.__caballaje=caballaje
    self.__plazas=plazas


#1ra forma de crear set y get
def getMarca(self):
    return self.__marca

def setMarca(self, marca):
    self.__marca=marca

#2da forma de crear set y get
@property
def marca(self):
    return self.__marca

@marca.setter
def marca(self,marca):
    self.__marca=marca

###########################

def getColor(self):
    return self.__color

def setColor(self, color):
    self.__color=color

def getModelo(self):
    return self.__modelo

def setModelo(self, modelo):
    self.modelo=modelo

def getVelocidad(self):
    return self.__velocidad

def setVelocidad(self, velocidad):
    self.__velocidad=velocidad

def getCaballaje(self):
    return self.__caballaje

def setCaballaje(self, caballaje):
    self.__caballaje=caballaje

def getPlazas(self):
    return self.__plazas

def setPlazas(self, plazas):
    self.__plazas=plazas


def acelerar():
    pass

def frenar():
    pass

coche1=coches()
coche2=coches()
coche3=coches()

#multiples objetos
coche1=coches("VW","Blanco","2022",220,150,5,"XERHHAHE%")
coche2=coches("Nissan","Azul","2020",180,150,6)
coche3=coches("Honda","","",0,0,0 )


print(f"Datos del vehiculo: \n Marca: {coche1.getMarca()} \n Color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n Velocidad: {coche1.getVelocidad()} \n Caballaje: {coche1.getCaballaje()} \n Plazas: {coche1.getPlazas()}")
print(f"Datos del vehiculo: \n Marca: {coche2.getMarca()} \n Color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n Velocidad: {coche2.getVelocidad()} \n Caballaje: {coche2.getCaballaje()} \n Plazas: {coche2.getPlazas()}")
print(coche3.marca)



""""
crear los metodos setters y getters estos metodos son importantes y necesarios
en todas las clases para que el programador interactue con los valores de los atributos a traves
de estos metodos... digamos que es la menera mas adecuada y recomendada para solicitar un vatlor(get) y/o para
ingresar o cambiar un valor(set) a un atributo en particular de la clase a traves de un objeto

En teoria se deberia de crear un metodo getters y setter por cada atributo que contenga la clase

Los metodos get siempre regresan valor de la propiedad a traves del return
Por otro lado el metodo del set siempre recibe parametros para cambiar o modificar el valor del atributo
o propiedsd en cuestion 

Metodos o acciones o funciones que hace el objeto 
"""