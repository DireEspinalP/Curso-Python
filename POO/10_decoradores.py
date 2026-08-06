### DECORADORES  ###

#  Un decorador es una función que recibe otra función
#  como argumento y devuelve una nueva función que
#  generalmente extiende o modifica el comportamiento
#  de la función original.

def decorator(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    return funcion_modificada

#def saludo():
#    print("Hola Dire")

#saludo_modificado=decorador(saludo)
#saludo_modificado()

@decorator #
def saludo():
    print("Hola Dire")

saludo()

## Propiedades ##
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    @property #GETTER 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter #SETTER
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @property #GETTER
    def edad(self):
        return self.__edad

    @nombre.deleter #DELETER
    def nombre(self):
        del self.__nombre #Elimina el atributo privado de la clase

#Uso de get
dalto=Persona("Dire", 18)
nombre=dalto.nombre # ocultamos el nombre real de la variable y accedemos al atributo privado de la clase
edad=dalto.edad

#Uso de set
dalto.nombre="Pepe"
nombre=dalto.nombre
print(nombre)

#Uso de deleter
del dalto.nombre
#print(dalto.nombre) # Esto generará un error, ya que el atributo ha sido eliminado.

"""
OLBSERVACION SI HACES UN "del" sin usar el deleter, generará un error, ya que el atributo es privado y no se puede 
acceder directamente desde fuera de la clase.
"""