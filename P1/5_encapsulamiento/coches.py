import os
os.system("cls")

class Coches:
   def _init_(self):
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


def acelerar(self):
    return "Estoy acelerando el coche"

def frenar(self):
    return "Estoy frenando el coche"

