import os
os.system("cls")

class Coches:
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._caballaje = caballaje
        self._plazas = plazas

    # Metodos set y get
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def caballaje(self):
        return self._caballaje

    @caballaje.setter
    def caballaje(self, caballaje):
        self._caballaje = caballaje

    @property
    def plazas(self):
        return self._plazas

    @plazas.setter
    def plazas(self, plazas):
        self._plazas = plazas

    def acelerar(self):
        return "Estoy acelerando el coche"

    def frenar(self):
        return "Estoy frenando el coche"

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self._eje = eje
        self._capacidadCarga = capacidadCarga

    @property
    def eje(self):
        return self._eje

    @eje.setter
    def eje(self, eje):
        self._eje = eje

    @property
    def capacidadCarga(self):
        return self._capacidadCarga

    @capacidadCarga.setter
    def capacidadCarga(self, capacidadCarga):
        self._capacidadCarga = capacidadCarga

    # metodos
    def cargar(self, tipo_carga):
        self._tipo_carga = tipo_carga
        return self._tipo_carga

class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self._traccion = traccion
        self._cerrada = cerrada

    @property
    def traccion(self):
        return self._traccion

    @traccion.setter
    def traccion(self, traccion):
        self._traccion = traccion

    @property
    def cerrada(self):
        return self._cerrada

    @cerrada.setter
    def cerrada(self, cerrada):
        self._cerrada = cerrada

    # metodos
    def transportar(self, num_pasajeros):
        self._num_pasajeros = num_pasajeros
        return self._num_pasajeros