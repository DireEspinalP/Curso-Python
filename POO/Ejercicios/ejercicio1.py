"""
Crear una clase con el nombre de "Estudiante" 
que tenga los atributos "Nombre", "Edad", "Grado"
ademas encargar un metodo que se llame "estudiar" que imprima
"El estudiante {nombre} esta estudiando

Para trabajar con instancia
Crear un objeto Estudiante
y usar un metodo estudiar()

incluso debe interactuar con el usuario para brindar los atributos
si despues de registrar los atributos coloca "estudiar" 
usar el metodo estudiar()

"""
#Solucion

# MI FORMA
class Estudiante():

    def estudiar(self):
        self.nombre = input("\nNombre: ")
        self.edad = int(input("Edad: "))
        self.grado = str(input("Grado: "))
        estudia = str(input("Quieres estudiar?\n"))
        
        if (estudia.lower() == "si"):
            print(f"El estudiante {self.nombre} esta estudiando")
        else:
            print(f"El estudiante {self.nombre} NO esta estudiando")


student1 = Estudiante()   
student1.estudiar()

# SOLUCIONARIO
class Estudiante():
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad =edad
        self.grado =grado
    def estudiar(self):
        print("Estudiando...")
nombre=input("\n\nDigame su nombre: ")
edad=input("Ahora su edad: ")
grado=input("Por ultimo, su grado: ")

estudiante=Estudiante(nombre,edad,grado)
print(f"""
    DATOS DEL ESTUDIANTE: \n\n
    Nombre: {estudiante.nombre}\n
    Edad:: {estudiante.edad}\n
    Grado:: {estudiante.grado}\n
    """)

while True:
    estudiar=input()
    if (estudiar.lower()=="estudiar"):
             estudiante.estudiar()
    break