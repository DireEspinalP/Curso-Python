### Listas [] ###

my_list=list()
my_other_list=[]

print(len(my_list))
print(len(my_other_list))

"""
() -> Crea una lista vacía 
[] -> Crea una lista vacía 

El () y [] se utilizan para crear listas vacías,
 pero [] es la forma más común y recomendada.
"""

my_list=[1, 7, 3, 8, -70]
print(my_list) #Imprime toda la informacion incluido []
print(len(my_list)) #cantidad de datos

my_other_list=[35, 24, 62, 52, 12, 24,"Dire", "Dire", "Dire", "Daniel" , "Daniel", 25, True, False]
print(my_other_list) 
print(len(my_other_list))

print(my_list+my_other_list)
print(my_other_list+my_other_list)

print(type(my_list))
print(type(my_other_list)) 

print(my_other_list[4])
print(my_other_list[-7])
# No puedes hacer print(my_other_list[10]) y print(my_other_list[-11])
# porque no existen esos indices, te dara un error de indice fuera de rango

print(my_other_list.count("Dire"))
print(my_other_list.count(24))

#Count: repeticiones de elementos
#Len: cantidad de elementos

private_list=[18,1.75,"Dire", "Espinal"]
age,height,name,lastname=private_list
print(name,lastname)
print(age,height)

print(list([1,2,3,4])) #Constructor de listas
print([1,2,3,4])


## Funciones con listas ##
"""
append() -> Agrega un elemento al final de la lista
copy() -> Devuelve una copia superficial de la lista
count() -> Devuelve el número de veces que un elemento aparece en la lista
extend() -> Agrega los elementos de un iterable al final de la lista
index() -> Devuelve el índice del primer elemento que coincide con el valor dado
insert() -> Inserta un elemento en una posición específica de la lista
pop() -> Elimina y devuelve el último elemento de la lista
remove() -> Elimina la primera aparición de un elemento en la lista
reverse() -> Invierte el orden de los elementos en la lista
sort() -> Ordena los elementos de la lista en orden ascendente

clear() -> Elimina todos los elementos de la lista
"""

print("____Operadores con listas_____-")

my_new_lista=[1,2,3,4,5, "Dire", "Dire"]
my_new_lista.append("Daniel")
print(my_new_lista)

my_new_lista_copy=my_new_lista.copy()
print(my_new_lista_copy+[("COPIA")])

print(my_new_lista.count("Dire"))

my_new_lista.extend(["ESPINAL"])
print(my_new_lista)

print(my_new_lista.index("Daniel"))

my_new_lista.insert(2,"azul")
print(my_new_lista)


my_pop_element=my_new_lista.pop(2)
print(my_pop_element)

my_new_lista.remove(1)
my_new_lista.remove(2)
my_new_lista.remove(3)
print(my_new_lista)

my_new_lista.reverse()
print(my_new_lista)

#Solo trabaja con la misma variables
my_list.sort()
print(my_list)

my_clear_lista=my_new_lista.clear()
print(my_clear_lista)