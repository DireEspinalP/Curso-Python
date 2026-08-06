# Encapsulamiento

class MicClase:
    def __init__(self, valor):
        self.__atributo_privado = "valor"  # Atributo privado "__nombre de atributo"
    def __hablar(self):  # Método privado "__nombre de metodo"
        print("Hola, soy un método privado")

objeto=MicClase()
print(objeto.__atributo_privado)
 # Esto generará un error, ya que el atributo es privado 
 # y no se puede acceder directamente desde fuera de la clase.