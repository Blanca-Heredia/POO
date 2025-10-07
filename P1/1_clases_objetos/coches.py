import os
os.system("cls")

class Coches:
    marca=""
    color=""
    modelo=""
    velocidad=""
    caballaje=""
    plazas=""

   # def acelerar(self,incremento):
        #self.velocidad=self.velocidad+incremento
        #return self.velocidad
    
    #def frenar(self,decremento):
        #self.velocidad=self.velocidad-decremento
        #return self.velocidad
    
    def acelerar(self):
        pass
    def frenar(self):
        pass


coche1=Coches()
coche1.marca="VMW"
coche1.color="Blanco"
coche1.modelo="2007"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5

print(f"Datos del primer coche: Marca:{coche1.marca}, Color:{coche1.color}, Modelo:{coche1.modelo}, Velocidad:{coche1.velocidad}, Caballaje:{coche1.caballaje}, Plazas:{coche1.plazas}")

coche2=Coches()
coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6

print(f"Datos del segundo coche: Marca:{coche2.marca}, Color:{coche2.color}, Modelo:{coche2.modelo}, Velocidad:{coche2.velocidad}, Caballaje:{coche2.caballaje}, Plazas:{coche2.plazas}")


print(coche1.acelerar(30))
print(coche1.frenar(100))
print(coche2.acelerar(30))
print(coche2.frenar(100))
