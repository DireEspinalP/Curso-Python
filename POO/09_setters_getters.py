## SETTERS Y GETTERS ###

# SET : Es un método que permite modificar el valor de un atributo de una clase.
# GET : Es un método que permite obtener el valor de un atributo de una clase.
class Persona:
    #Primera forma
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    def get_edad(self):
        return self.__edad
    def set_edad(self, new_edad):
        self.__edad = new_edad
dalto=Persona("Dire", 18)
print("GETTERS")
nombre=dalto.get_nombre()
edad=dalto.get_edad()
print(nombre)
print(edad)

print("\nSETTERS")
dalto.set_nombre("Daniel")
dalto.set_edad(20)
nombre=dalto.get_nombre()
edad=dalto.get_edad()
print(nombre)
print(edad) 