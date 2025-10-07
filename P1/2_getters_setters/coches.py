import os
os.system("cls")

class Coches:
    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0

#Crear los metodos setter y getter. Estos metodos son importantes y necesarios en todas las clases para que el programador interactue con los valores de los atributos a traves de estos metodos. Digamos que es la manera mas adecuada y recomendada para solicitar un velor (get) y/o para ingresar o cmabiar un valor (set) a un atributo en particular de la clase a taves de un objeto.
#En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
#Los metodos get siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion


#1era forma de crear Set y Get
    def getMarca(self):
        return self.__marca
    
    def setMarca(self,marca):
        self.__marca=marca

#2da forma de crear Set y Get
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self,marca):
        self.__marca

    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color=color

    def getModelo(self):
        return self.__modelo
    
    def setModelo(self,modelo):
        self.__modelo=modelo

    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad
        
    def getCaballaje(self):
        return self.__caballaje
    
    def setCaballaje(self,caballaje):
        self.__caballaje=caballaje

    def getPlazas(self):
        return self.__plazas
    
    def setPlazas(self,plazas):
        self.__plazas=plazas

    def acelerar(self):
        pass
    def frenar(self):
        pass

coche1=Coches()
coche1.setMarca("VMW")
coche1.setColor("Blanco")
coche1.setModelo("2007")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)

print(f"Datos del vehiculo: Marca:{coche1.marca()}, Color:{coche1.getColor()}, Modelo:{coche1.getModelo()}, Velocidad:{coche1.getVelocidad()}, Caballaje:{coche1.getCaballaje()}, Plazas:{coche1.getPlazas()}")


coche2=Coches()
coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)

print(f"Datos del vehiculo: Marca:{coche2.getMarca()}, Color:{coche2.getColor()}, Modelo:{coche2.getModelo()}, Velocidad:{coche2.getVelocidad()}, Caballaje:{coche2.getCaballaje()}, Plazas:{coche2.getPlazas()}")



