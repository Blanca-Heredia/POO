import os
os.system("cls")
class Profesores:
    def __init__(self, nombre_pro, experiencia, num_profesor):
        self.nombre_pro = nombre_pro
        self.experiencia = experiencia
        self.num_profesor = num_profesor

    def getNomPro(self):
        return self.nombre_pro

    def setNomPro(self, nombre_pro):
        self.nombre_pro = nombre_pro

    def getExp(self):
        return self.experiencia

    def setExp(self, experiencia):
        self.experiencia = experiencia

    def getNumPro(self):
        return self.num_profesor

    def setNumPro(self, num_profesor):
        self.num_profesor = num_profesor

class Alumnos:
    def __init__(self, nombre_alu, edad, matricula):
        self.nombre_alu = nombre_alu
        self.edad = edad
        self.matricula = matricula

    def getNomAlu(self):
        return self.nombre_alu

    def setNomAlu(self, nombre_alu):
        self.nombre_alu = nombre_alu

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getMatri(self):
        return self.matricula

    def setMatri(self, matricula):
        self.matricula = matricula

class Cursos:
    def __init__(self, nombre_cur, codigo, creditos):
        self.nombre_cur = nombre_cur
        self.codigo = codigo
        self.creditos = creditos

    def getNomCur(self):
        return self.nombre_cur

    def setNomCur(self, nombre_cur):
        self.nombre_cur = nombre_cur

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCreditos(self):
        return self.creditos

    def setCreditos(self, creditos):
        self.creditos = creditos

print("Datos de Profesores")
pro1 = Profesores("Ana Torres Guzman", 40, 123)
pro2 = Profesores("Daniel Contreras", 40, 14)
print(f"Nombre: {pro1.getNomPro()}, Experiencia: {pro1.getExp()}, Num. Profesor: {pro1.getNumPro()}")
print(f"Nombre: {pro2.getNomPro()}, Experiencia: {pro2.getExp()}, Num. Profesor: {pro2.getNumPro()}")

print("\nDatos de Alumnos")
alu1 = Alumnos("Juan Correa Simental", 25, 100123)
alu2 = Alumnos("Maria Serrano Mata", 22, 100124)
print(f"Nombre: {alu1.getNomAlu()}, Edad: {alu1.getEdad()}, Matricula: {alu1.getMatri()}")
print(f"Nombre: {alu2.getNomAlu()}, Edad: {alu2.getEdad()}, Matricula: {alu2.getMatri()}")

print("\nDatos de Cursos")
cur1 = Cursos("POO", 100, 6)
cur2 = Cursos("FOSO", 101, 4)
print(f"Nombre: {cur1.getNomCur()}, Código: {cur1.getCodigo()}, Créditos: {cur1.getCreditos()}")
print(f"Nombre: {cur2.getNomCur()}, Código: {cur2.getCodigo()}, Créditos: {cur2.getCreditos()}")