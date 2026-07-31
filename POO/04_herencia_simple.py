## HERENCIA SIMPLE ##

class Persona:
    def __init__(self, nombre,edad, nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")

class Empleado(Persona):#class Empleado hereda a class Persona
   # pass ( Solo la crea no activa nada)
      def __init__(self, nombre, edad, nacionalidad,trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo=trabajo
        self.salario=salario


#Creamos una instancia para el empleado le tenemos
#  q pasar las propiedades de Persona osea "HERENCIA"
dire=Empleado("Dire",18,"Peruano","Programador",1000)
print(dire.nacionalidad)
dire.hablar()

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,notas,universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas=notas
        self.universidad=universidad
        