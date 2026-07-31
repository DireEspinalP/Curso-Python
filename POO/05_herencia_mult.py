## HERENCIA MULTIPLE ##

class Persona:
    def __init__(self, nombre,edad, nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):

        print("Hola, estoy hablando un poco")

class Artista:
    def __init__(self, habilidad):
        self.habilidad=habilidad
    def mostrar_habilidad(self):
        return (f"Mi habilidad es {self.habilidad}")

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario=salario
        self.empresa=empresa

    def presentarse(self):
         # return f'Hola, soy: {self.nombre},{self.mostrar_habilidad()} y trabajo en {self.empresa}' #Heredo a EmpleadoArtista (clase hijo)
          print(f'Hola, soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}') #Heredo a Artista (clase padre)

dire=EmpleadoArtista("Dire",18,"peruano","aprender rapido",1000,"Github")
dire.presentarse()

#ADICIONAL
herencia=issubclass(Artista,Persona)
instancia1=isinstance(dire,EmpleadoArtista)
instancia2=isinstance(dire,Artista)
instancia3=isinstance(dire,Persona)
print(herencia)
print(instancia1)
print(instancia2)
print(instancia3)
