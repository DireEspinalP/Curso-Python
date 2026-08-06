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