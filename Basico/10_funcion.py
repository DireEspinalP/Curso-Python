### Funciones ###
"""
Sintaxis:
    def name_funct(parametros):
        (operador de dicha funcion)

    name_funct() "llamada de la funcion"
"""


print("\nFuncion 1)" )
def my_function():
    print("Esto es una funcion")
my_function() 


print("\nFuncion 2) 'Sin parametros'"  )
def suma():
    num1=int(input("Primer num: "))
    num2=int(input("Segundo num: "))
    num3=num1+num2
    print(f"La suma de los dos numeros es {num3}")
suma()


print("\nFuncion 3) 'Con parametros'"  )
def sum(num1, num2): #Puedes especificar los tipos
#def sum(num1: int, num2: int)
    print(num1+num2)
sum(5,7)# Llamada de la funcion con parametros
sum(5470,804)
sum(0,-4)
sum("4","6")

print("\nFuncion 4) 'Con Return'"  )
def sum_return(num1, num2):
    return num1+num2
num3=sum_return(1,8)
print(num3)

print("\nFuncion 5) 'String'"  )
def print_name ():
    name=str(input("Nombre : "))
    lastname=str(input("Apellido: "))
    print(f"Eres {name} {lastname}, Bienvenido a Python ")
print_name()

print("\nFuncion 6) 'Texto largo'"  )
def print_texts(*texts):
     print(texts)
print_texts("ESTO", "ES", "LA", "UNI")

print("\nFuncion 7) 'Texto largo y FOR'"  )
def print_for_texts(*texts):
    for text in texts:
        print(text)
print_for_texts("ESTO", "ES", "LA", "UNI")

print("\nFuncion 8) 'Texto largo en LOWER'"  )
def print_lower_text(*texts):
      for text in texts:
        print(text.lower())
print_lower_text("esto", "Es", "lA", "UNI")
