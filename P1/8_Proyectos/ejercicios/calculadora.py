'''
class Calculadora:
    def __init__(self,num1,num2):
        num1=int(input("Numero 1: "))
        num2=int(input("Numero 2: "))
        self.num1
        self.num2

def suma(num1,num2):
    suma=self.num1=+self.num2
    print(f"La suma es: {suma}")
        
def resta(num1,num2):
   resta=self.num1-num2
   print(f"La resta es: {resta}")
        
def multi(num1,num2):
   multi=self.num1*self.num2
   print(f"La multiplicación es: {multi}")

def divi(num1,num2):
   divi=self.num1/self.num2
   print(f"La división es: {divi}")

    @property
    def suma(self):
        return self.num1
   
    @suma.setter(num1)
    self.num1=num1

    @property
    def resta(self,num1):
      self.num1=num1

    @suma.setter(num1)
   return self.num1
'''

class Calculadora:
    def __init__(self):
        self._numero1=int(input("Numero 1:"))
        self._numero2=int(input("Numero 2:"))

    @property
    def numero1(self):
        return self.numero1

    numero1.setter
    def numero1(self,numero1):
        self.numero1=numero1

    @property
    def numero2(self):
        return self.numero2

    numero2.setter
    def numero2(self,numero2):
        self.numero2=numero2

    def sumar(self):
        return self._numero1+self._numero2

    def restar(self):
        return self._numero1-self._numero2

    def multiplicar(self):
        return self._numero1*self._numero2

    def dividir(self):
        return self._numero1/self._numero2

operacion=Calculadora()
print(f"{operacion.numero1}+{operacion.numero2}={operacion.sumar()}")
print(f"{operacion.numero1}+{operacion.numero2}={operacion.restar()}")
print(f"{operacion.numero1}+{operacion.numero2}={operacion.multiplicar()}")
print(f"{operacion.numero1}+{operacion.numero2}={operacion.dividir()}")



