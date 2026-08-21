#---------Principio_de_Responsabilidad_Unica-------------
class Auto():
    def __init__(self, tanque):
        self.posicion=0
        self.tanque=tanque
       # self.combustible=100L
    def mover(self, distancia):
         if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            return f"Moviste el auto, nueva posición: {self.posicion}"
         else:
            return "No se mueve el auto"
    def obtener_posicion(self):
        return self.posicion
"""
Si dentro de la clase uso estas funciones 
    def agregar_combustible(self,cantidad):
        self.combustible+=cantidad
    def obtener_combustible(self):
        return self.combustible
      
----->NO SERIA OBTIMO
"""

class TanqueDeCombustible:
    def __init__(self):
        self.combustible=100
    def agregar_combustible(self, cantidad):
        self.combustible+=cantidad
    def obtener_combustible(self):
        return self.combustible 
    def usar_combustible(self,cantidad):
        self.combustible-=cantidad   

tanque1=TanqueDeCombustible()
auto2=Auto(tanque1)
auto1=Auto(tanque1)
print(auto1)
print(auto2.obtener_posicion())
print(auto2.mover(50))
print(auto2.obtener_posicion())
print(auto2.mover(80))
print(auto2.obtener_posicion())
print(auto2.mover(100))
print(auto2.obtener_posicion())

"""
Este código sigue el Principio de Responsabilidad Única, que dice que 
cada clase debe encargarse de una sola cosa. Por eso separamos el código 
en dos clases: Auto y TanqueDeCombustible. El Auto solo se encarga de 
moverse y saber en qué posición está. El TanqueDeCombustible solo se 
encarga de guardar, agregar y gastar combustible. El Auto no sabe cómo 
funciona el tanque por dentro, solo le pregunta "¿cuánto combustible 
tienes?" o le dice "usa esta cantidad", y el tanque responde. Gracias a 
esto, si un día queremos cambiar cómo funciona el combustible (por 
ejemplo, ponerle un límite o cambiar las unidades), solo tocamos la clase 
del tanque y no tenemos que tocar la clase del auto. Esto hace que el 
código sea más fácil de entender, de arreglar y de mejorar sin romper 
otras partes.
"""


  