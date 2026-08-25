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
