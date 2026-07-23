### Condicionales ###

"""
sitaxis breve 

variable=....

if "mi_condicion":
    operacion si es V
else:
    operacion si es F

"""
## if and else ##
my_variable=18
my_other_variable=5*2

print(f"Primera variable {my_variable}")
print(f"Segunda variable {my_other_variable}")

print("\n Condicion 1)")
if my_variable==my_other_variable:
    print(" Son numeros iguales")
else: 
    print("Son numeros diferentes")

print("\n Condicion 2)")
if my_variable>10:
    print ("la variable 1 es mayor que 10")
else:
    print ("la variable 1 es menor o igual que 10")


## elif
my_numer=3
print("\n Condicion 3)")
print(f"Mi numero es {my_numer}")
print("¿Mi numero esta en entre [1:5]?")
if my_numer<0:
    print("Error es menor que cero (NEGATIVO)")
elif my_numer>0 and my_numer<5:
    print("SI esta entre [1:5] XD")
else:
    print("El numero es mayor que 5")


## OR ##
print("\n Condicion 4)")
if my_other_variable>15 or my_other_variable<9:
    print(" La variable 2 es esta en el rango de [9:15]")
else: 
    print("La variable 2 NO esta en el rango de [9:15]")

## AND ##
mensaje1="hola"
mensaje2="mundo"
print("\n Condicion 5)")
print(f"Palabra HOLA tiene {len("hola")} letras ")
print(f"Palabra MUNDO tiene {len("mundo")} letras ")
if len(mensaje1)<len(mensaje2) and len(mensaje1)>len(mensaje2):
    print("Las dos palabras SI tienen la misma cantidad de letras")
else:
 print("Las dos palabras NO tienen la misma cantidad de letras")

## NOT ##
my_text=""
print("\n Condicion 6)")
print(f"Mi texto es ...{my_text}...")
if not my_text:
    print("mi texto esta vacio")
if my_text=="my_text":
    print("estos textos coindiden")