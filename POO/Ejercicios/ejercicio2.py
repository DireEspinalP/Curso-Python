"""
HERENCIA EJERCICIO 2
a)
Crear un sistema para una escuela. En este sistema, vamos a tener dos
clases principales: Persona y Estudiante. La clase Persona tendra los
atributos de nombre y edad y un metodo que imprima el nombre y la edad
de la persona. La clase Estudiante heredara de la clase Persona y tambien
tendra un atributo adicional: grado y un metodo que imprima el grado del 
estudiante.

Deberas utilizar super en el metodo de inicializacion (init) para reutilizar
el codigo de la clase padre. Luego crea una instancia de la clase Estudiante
e imprime sus atributos y utiliza sus metodos para asegurar que todo
funciona correctamente.

"""
#Mi solucion:
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
    def imprimir_grado(self):
        print(f"Grado: {self.grado}")

"""

HERENCIA EJERCICIO 2
b)
Imagina que estas modelando animales en un zoo. Crea tres clases:
"Animal", "Mamifero" y "Ave". La clase " Animal" debe tener un 
metodo llamado "comer". La clase "Mamifero" debe tener un metodo 
llamado "amamantar" y la clase "Ave" un metodo llamado "volar"

Ahora crea una clase "Murcielago" que herede de Mamifero y "Ave",
en ese orden, y por lo tanto ser capaz de "amamantar" y "volar",
ademas de "correr"

(FORMA PRACTICA)
Finalmente, juega con el orden de herencia de la clase "Murcielago"
y observa como cambia el MRO y el comportamiento de los meotodos al usar
super().
"""
#Mi solucion
class Animal:
    def comer(self):
        print("El animal esta comiendo")
class Mamifero(Animal):
    def amamantar(self):
        print("El mamifero esta amamantando")
class Ave(Animal):
    def volar(self):
        print("El ave esta volando")
class Murcielago(Mamifero,Ave):
    def __init__(self):
        super().__init__()
    def correr(self):
        print("El murcielago esta corriendo")

elefante = Mamifero()
elefante.comer()
paloma = Ave()
paloma.volar()
print(f"{Murcielago.mro()}\n")