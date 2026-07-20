### SETS {} ###

# Un sets no es una estructura ordenada
# Un sets no admite repetidos

my_set=set() #Creacion de un set
my_other_set={}
print(type(my_set)) 
print(type(my_other_set)) #Es un diccionario

my_other_set={"Dire", "Espinal", 18} #Implemtacion de datos
print(type(my_other_set)) #Es un sets


print(len(my_other_set)) #Mide la cantidad de elemento en el Sets

my_other_set.add("XD") # Anade un elemento en sets
print(my_other_set) 
#Te añade pero esta todo desordenado los elementos a diferencia de una list

print("GG" in my_other_set) #¿Existe "GG" en el sets?
print("Dire" in my_other_set) #¿Existe "Dire" en el sets?

my_other_set.remove(18) #Borra un elemento en especifico
print(my_other_set)


my_other_set.clear()
print(my_other_set)
print(len(my_other_set)) ##Borro todos los elementos pero el sets esta activo

del my_other_set 
# print(my_other_set) NameError: name 'my_other_set' is not defined



my_new_set={"Hola", "Mundo", "XD"}
my_new_set2={"Hola", "Mundo", "Random"}
my_new_set3={"C++", "C#", "Python, JAVA"}
#my_list=list(my_new_set)
#print(my_list)
#print(my_list[0])
#Esto es ta mal usado ya que es arriesgado al haber mucho desorden en dicho conjunto

my_new_other_set1=my_new_set.union(my_new_set2) #NO REPITE PALABRAS
print(my_new_other_set1)


my_new_other_set2=my_new_set.union(my_new_set2).union(my_new_set3)
print(my_new_other_set2)

print(my_new_set2.difference(my_new_set))
print(my_new_set3.difference(my_new_set))
print(my_new_other_set2.difference(my_new_set))
print(my_new_other_set2.difference(my_new_other_set1).difference(my_new_set3))


"""
___CONSEJOS___

Si nos da igual el ORDEN y NO quiero REPETIDOS -> SETS

Si tenemos compartamiento de lista donde podamos añadir elementos y el id -> LIST

Si quieremos una lista inmutable -> TUPLA

"""