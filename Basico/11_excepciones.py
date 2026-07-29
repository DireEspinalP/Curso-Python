### Exception Handling ###

""""
if numberOne>3:
    print(numberOne + numerTwo)
else: 
    print("No se cumple")
error de entenderlo de esta manera

if type(numberOne)==int:
    print(numberOne + numerTwo)
else: 
    print("No se cumple")    

"""
numberOne=5
numerTwo=1
numberTwo="1"


print("\nTRY-EXCEPT")
print("Iteracion 1)")
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

#CASO SI numberTwo=1
numberTwo=1
print("\nIteracion 2)")
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except:
    #Se ejecuta cuando se produce una excepcion
    print("Se ha producido un error")



#Considera a numberTwo=1
print("\nTRY-EXCEPT-ELSE")
print("Iteracion 3)")
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: 
    #Se ejecuta cuando NO se produce una excepcion
    print("La ejecucion continua correctamente")



#Considera a numberTwo=1
print("\nTRY-EXCEPT-ELSE-FINALLY")
print("Iteracion 4)")
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: 
    #Se ejecuta cuando NO se produce una excepcion
    print("La ejecucion continua correctamente")
finally:
    #Se ejecuta siempre
    print("La ejecucion continua")


#Excepcion de tipo
numberTwo="1"
print("\nEXCEPCIONES DE TIPOS")
print("Iteracion 5)")
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except ValueError:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un ValueError")
except TypeError:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un TypeError")

#Captura de la informacion de la excepcion
print("\nIteracion 6)")
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as name: # "name" es el nombre de la variable que contiene la informacion del error
    print(name)
except :
    print()