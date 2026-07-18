### Strings ###

my_string="Mi string" #Doble comilla
my_other_string='Mi otro string' #Comilla simple

print(len(my_string)) # 9
print(len(my_other_string)) #14

print(my_string + " " + my_other_string) #UNIR STR


#Saltos de Linea
my_new_line="Este es un string\ncon salto de linea" #\n salto de linea
print(my_new_line)

#Tabulacion
my_tab="Este es un string\tcon tabulacion" #\t tabulacion
print(my_tab)

#Salto y Tabulacion
my_tab_and_new_line="\tEste es un string con tabulacion y \nsalto de linea"
print(my_tab_and_new_line)

#Formateo 
"""
%s -> String
%d -> Entero
%f -> Float
%c -> Caracter

"""
name, surname, age= "Dire", " Daniel", 25
print("Mi nombre es Dire Daniel y tengo 25 años") #Solo texto
print("Mi nombre es {}{} y tengo {} años".format(name, surname, age)) #Primer formateo "antiguo"
print("Mi nombre es %s %s y tengo %d años" %(name, surname, age)) #Segundo formateo "antiguo"

#Inferencia de datos
print(f"Mi nombre es {name} {surname} y tengo {age} años") #Tercer formateo "nuevo" y mas moderno


#Error basico sin formateo
print("Mi nombre es " + name + surname + " y tengo " + str(age) + " años") 

#USA FORMATEO PARA STRINGS en VEZ DE CONCATENAR


# Desempaquetado de caracteres

variable="Python"
a,b,c,d,e,f=variable
print (a) #p
print (b) #y
print (c) #t
print (d) #h
print (e) #o
print (f) #n

#Division de strings

variable_dividido=variable[1:3]
print(variable_dividido) #yt

variable_dividido=variable[1:6]
print(variable_dividido) #ython

variable_dividido=variable[0:6:3]
print(variable_dividido) #Ph

variable_dividido=variable[1:]
print(variable_dividido) #ython

variable_dividido=variable[:3]
print(variable_dividido) #Pyt


dividir_lenguaje=variable[-2]
print(dividir_lenguaje) #o

reversa=variable[::-1]
print(reversa) #nohtyP

### FUNCIONES CON STRINGS ##
"""
.upper() -> Convierte a mayúsculas
.lower() -> Convierte a minúsculas
.capitalize() -> Convierte la primera letra a mayúscula
.title() -> Convierte la primera letra de cada palabra a mayúscula
.strip() -> Elimina espacios en blanco al inicio y al final
.replace("old", "new") -> Reemplaza una cadena por otra
.split("delimiter") -> Divide la cadena por un delimitador
.join(["list", "of", "strings"]) -> Une una lista de cadenas con un delimitador
.count("substring") -> Cuenta cuantas veces aparece una subcadena
.find("substring") -> Devuelve el índice de la primera aparición de una subcadena

.startswith("substring") -> Devuelve True si la cadena empieza con la subcadena, False en caso contrario
.endswith("substring") -> Devuelve True si la cadena termina con la subcadena, False en
".is(operador"s) -> Devuelve True si la cadena cumple con la condición, False en caso contrario
"""
my_string="Dire Daniel"
print(my_string.upper()) #DIRE DANIEL
print(my_string.lower()) #dire daniel
print(my_string.capitalize()) #Dire daniel
print(my_string.title()) #Dire Daniel
print(my_string.strip()) #Dire Daniel
print(my_string.replace("Dire", "Adiós")) #Adiós Daniel
print(my_string.split(" ")) #['Dire', 'Daniel']
print(" ".join(["Dire", "Daniel"])) #Dire Daniel
print(my_string.count("d")) #1
print(my_string.find("d")) #4

print(my_string.startswith("Dire")) #True
print(my_string.endswith("Daniel")) #True
