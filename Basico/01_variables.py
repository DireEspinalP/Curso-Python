"""
Este archivo es para ver
diferentes tipos de variables y declaraciones
de variables en python

Convenciones:
1) Las variables en python no tienen un tipo de dato definido, 
es decir, no es necesario declarar el tipo de dato de la variable, python lo hace automáticamente.
2) Las variables en python no pueden empezar con un número, ni contener espacios, ni caracteres
    especiales, ni palabras reservadas de python.
3) Las variables en python pueden contener letras, números y guiones bajos (_).
4) Las variables en python son case sensitive, es decir, diferencia entre mayúsculas y
"""
#Errores comunes
"""""
first-name="juan"
first@name="juan"
first$name="juan"
num-1="diez"
1num="diez"
"""
#Ejemplo 1) Declaración de variables
mi_variable="Hola mundo" #tipo str
print (mi_variable)

#Ejemplo 2)
my_int=10
print(my_int) #tipo int

my_float=3.14
print(my_float) #tipo float

#Puedes hacer combinaciones de tipos

print(my_int+my_float) #tipo float en general sumando dos tipos y el resultado es float
print(my_int, my_float) #tipo int y float por separado
print(my_int, my_float, mi_variable) #tipo int, float y str por separado

my_int_str=str(my_int) #casteo de int a str
print(my_int_str) #tipo str OJO NO ES EL MISMO TIPO DE DATO (int)

#Concatenacion de variables en un print
print(type(print(my_int, my_float, mi_variable))) #tipo NoneType, el print no retorna nada, solo imprime en pantalla)