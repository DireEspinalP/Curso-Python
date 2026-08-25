#----------------Principio de segrecacion de interfaz----------------
from abc import ABC, abstractclassmethod
"""
class Trabajador(ABC):
    @abstractclassmethod
    def comer(self):
        pass
    @abstractclassmethod
    def trabajar(self):
        pass
    @abstractclassmethod
    def dormir(self):
        pass

class Humano(Trabajador):
    def comer(self):
        print("El humano esta comiendo")
    def trabajar(self):
        print("El humano esta trabajando")
    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):
    def trabajar(self):
        print("El humano esta trabajando")

robot=Robot()
"""

class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass
class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
         pass
class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass
class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print("El humano esta comiendo")
    def trabajar(self):
        print("El humano esta trabajando")
    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):
    def trabajar(self):
        print("El humano esta trabajando")

robot=Robot()
robot.trabajar()
humano=Humano()
humano.trabajar()
humano.dormir()
"""
Este código muestra el Principio de Segregación de Interfaz: es mejor 
tener varias interfaces pequeñas que una sola interfaz enorme que 
obligue a implementar cosas innecesarias. Arriba, en la parte comentada, 
Robot está obligado a heredar comer() y dormir(), aunque no los use, 
solo porque pertenecen a la misma interfaz que trabajar(). Abajo, se 
soluciona dividiendo esa interfaz en tres más pequeñas y específicas: 
Trabajador, Comedor y Durmiente. Así, cada clase hereda solo lo que 
realmente necesita: Humano usa las tres, y Robot usa solo Trabajador.
"""