# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:06:26 2023

@author: FORMACION
"""

class Persona:

    # Atributos
    edad = None
    nombre = None

    # Métodos
    def saludar(self):
        print(f"Hola, soy {self.nombre}")


class Empleado(Persona):

    # Atributos
    sueldo = None

    # Métodos
    def trabajar(self):
        print(f"Estoy trabajando y ganando {self.sueldo} euros")


class Estudiante(Persona):

    # Atributos
    materias = []

    # Métodos
    def estudiar(self):
        print(f"Estoy estudiando {self.materias}")


# Crear instancias
empleado = Empleado()
empleado.nombre = "Juan"
empleado.sueldo = 2000

estudiante = Estudiante()
estudiante.nombre = "María"
estudiante.materias = ["Matemáticas", "Física", "Química"]

# Acceder a los atributos y métodos
print(empleado.saludar())
print(empleado.trabajar())
print(estudiante.saludar())
print(estudiante.estudiar())