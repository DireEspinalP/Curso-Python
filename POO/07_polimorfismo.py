## Polimorfismo 

class Animal():
    def sonido(self):
        pass
    """
---------------  SOBRECARGA DE METODOS --------------- 
        def sonido(self):
            pass
        def sonido(self, tipo):
            pass
        def sonido(self, tipo, cantidad):
            pass
            
la COHERCION AUTOMATICA es un tipo de polimorfismo,
ya que el metodo sonido() puede ser llamado con
diferentes tipos de argumentos y se comporta 
de manera diferente dependiendo del tipo de 
argumento que se le pase.

POR EJEMPLO: 
En pyhton esta el operador "+" que puede ser usado para 
sumar numeros, concatenar strings, unir listas, etc.

--------------- DUCK TYPING --------------- 
El duck typing es un tipo de polimorfismo que se basa en el
principio de que si algo se comporta como un pato, nada como un pato y grazna como un pato,
entonces es un pato. En otras palabras, si un objeto tiene los
mismos métodos y atributos que otro objeto, entonces se puede usar en su lugar. 
Esto permite que los objetos sean intercambiables y facilita la reutilización del código.

    1) Enlaces dinamicos: En Python, los métodos y atributos de un objeto se resuelven en tiempo de ejecución,
         lo que permite que los objetos sean intercambiables.
    2) Enlaces  estáticos: En lenguajes de programación estáticos, los métodos y atributos de un objeto 
         se resuelven en tiempo de compilación, lo que significa que los objetos no son intercambiables.
    3) Tipo real: En Python, el tipo de un objeto se determina en tiempo de ejecución, 
        lo que permite que los objetos sean intercambiables.
    4) Tipo declarado: En lenguajes de programación estáticos, el tipo de un objeto se determina en tiempo de compilación,
        lo que significa que los objetos no son intercambiables.
    """
    
class Gato(Animal):
    def sonido(self):
        return "Miau"
class Perro(Animal):
    def sonido(self):
        return "Guau"

def hacer_sonido(animal): 
    print(animal.sonido())

gato=Gato()
perro=Perro()
#  Aca tengo el poliformismo, ya que el metodo sonido()
#  es el mismo para ambas clases, pero cada clase
#  tiene su propia implementacion del metodo.

print(gato.sonido()) # Aca cambia el objeto para la funcion
print(perro.sonido())

hacer_sonido(gato) # Aca cambia el argumento para la funcion
hacer_sonido(perro)
#hacer_sonido(vaca) ERROR (vaca no tiene el metodo sonido() )
