### ABSTRACCION ###
 
#En la programación orientada a objetos, la abstracción es un principio que permite representar conceptos del mundo real en términos de clases y objetos, ocultando los detalles complejos y mostrando solo la información esencial. Esto facilita la comprensión y el uso de los objetos, ya que los usuarios pueden interactuar con ellos sin preocuparse por su implementación interna.

#IDEA DE ABSTRACION
"""
class Auto():
    def __init__(self):
        self.estado="apagado"
    def encender(self):
        self.estado="encendido"
        print("El auto esta encendido")
    def apagar(self):
        self.estado="apagado"
        print("El auto esta apagado")
    def conducir(self):
        if self.estado=="apagado":
            self.encender()
        print("Conduciendo el auto")

mi_auto=Auto()
mi_auto.conducir()
"""

#CREACION DE CLASES ABSTRACTAS: 
# Es una clase que no puede ser instanciada directamente,
# sino que sirve como base para otras clases. Se utiliza 
# para definir una interfaz común y establecer métodos que 
# deben ser implementados por las subclases.
from abc import ABC, abstractmethod
class Persona(ABC):
#Plantilla de clase abstracta que define los atributos y métodos
    @abstractmethod
    def __init__(self,nombre,edad,sexo, actividad):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.actividad=actividad

    @abstractmethod
    def hacer_actividad(self):
        pass
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.sexo}. Mi actividad es {self.actividad}.")

# persona1=Persona("Dire", 18, "masculino", "programador", "estudiante") 
# # Esto generará un error, ya que no se puede instanciar una clase abstracta.

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    def hacer_actividad(self):
        print(f"Estoy trabajando en: {self.actividad}")



persona1=Estudiante("Dire", 18, "masculino", "programacion") 
persona2=Trabajador("Juan", 30, "masculino", "enseñar python")
#Ya se puede instanciar la clase Estudiante, ya que implementa todos los métodos abstractos de la clase Persona.
persona1.presentarse()
persona1.hacer_actividad()
persona2.presentarse()
persona2.hacer_actividad()