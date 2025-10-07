#Instanciar los objetos para posteriormente implementarlos 

from coches import Coches, Camionetas, Camiones

coche=Coches("VW","Blanco","2020",220,200,5)
print(coche.marca, coche.acelerar())

camioneta=Camionetas("Nissan","Amarillo","2025",180,200,4,"trasera",False)
print(camioneta.marca, coche.acelerar())



'''
num_objeto=int(input("Cuantos coches deseas?"))


for i in range(0,num_objeto):
    print(f"...Datos del coche {i+1}...")
    marca=input("Ingresa la marca: ").upper()
    color=input("Ingresa el color: ").upper()
    modelo=input("Ingresa el modelo: ").upper()
    velocidad=int(input("Ingresa la velocidad: "))
    potencia=int(input("Ingresa la potencia: "))
    plazas=int(input("Ingresa las plazas: "))

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)


    print(f"Datos del vehiculo: \n Marca: {coche1.__marca()} \n Color: {coche1.__color()} \n Modelo: {coche1.__modelo()} \n Velocidad: {coche1.__velocidad()} \n Caballaje: {coche1.__caballaje()} \n Plazas: {coche1.__plazas()}")

#coche1=Coches("VW","Blanco","2022",220,150,5,"XERHHAHE%")
#coche2=Coches("Nissan","Azul","2020",180,150,6)
#coche3=Coches("Honda","","",0,0,0 )
'''
