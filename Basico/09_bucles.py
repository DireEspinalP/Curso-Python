### BUCLES ###

##----WHILE----##
"""
while condicion:
    operador
"""
print("\n---------WHILE---------")
my_variable=1
print("\n Condicion 1)")
if my_variable<=10 and my_variable>0:
    while my_variable<=10:
        print(my_variable) 
        my_variable+=2
        #a partir de esto vale 9
else:
    print("Mi condicion es mayor que 10")
print(f"El nuevo cambio de mi variable es {my_variable}")


my_other_variable=1
print("\n Condicion 2)")
if my_variable<15 and my_other_variable>0:
    while my_other_variable<15:
        my_other_variable+=2
        print(my_other_variable) 
else:
    print("Mi condicion es mayor que 10")
print(f"El nuevo cambio de mi variable es {my_other_variable}")

#Esta segunda forma es la mejor usada para la logica ya que el valor final toma el max de la condicion

# BREAK
my_variable=10
print("\n---------BREAK---------")
print(" Condicion 3)")
while my_variable<18:
    my_variable+=1
    if my_variable==15:
        print(f"Se detuvo la ejecucion hasta el numero {my_variable}")
        break
    print(my_variable)



##----FOR----##
print("\n---------FOR---------")

print("\nCondicion 4) 'lista' ")
my_list={35,67,69,81,150}
for element in my_list:
    print(element)

print("\nCondicion 5) 'tupla' ")
my_set={"C++", "C#", "Python, JAVA"}
for element in my_set:
    print(element)


print("\nCondicion 6)  'dict' ")
my_dict={
    "Nombre":"Dire",
    "Apellido": "Espinal",
    "Edad":18,
    "Lenguaje": {"C++", "JAVA", "Python"},
    1:"Verde"
}
for element in list(my_dict.values()):
    print(element)

print("\nCondicion 7)")
for element in my_dict:
    print(element)
    if element=="HOLA": 
        print(f"Termino la ejecucion hasta el dict de '{element}' ")    
        break   
    elif element=="Lenguaje":
        print(f"Termino la ejecucion hasta el dict de '{element}' ")    
        break



##----CONTINUE----##
print("\n---------CONTINUE---------")

print("\nCondicion 8)")
for element in my_dict:
    print(element)
    if element=="Edad":    
        continue
    print("Se ejecuta")
   # print("Se ejecuta") CORTA SOLO A "Edad"


