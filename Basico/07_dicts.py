### Diccionarios ###

my_dict=dict()
my_other_dict={}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict={"Nombre":"Dire", "Apellido": "Espinal", "Edad":18, 1:"C++"}

my_dict={
    "Nombre":"Dire",
    "Apellido": "Espinal",
    "Edad":18,
    "Lenguaje": {"C++", "JAVA", "Python"},
    1:"Verde"
}
print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) #4 elements
print(len(my_dict)) #5 elements

#Formas de acceder a un elemento
print(my_dict["Nombre"])
my_dict["Nombre"]="Daniel" #Puedes actualizarlo
print(my_dict["Nombre"])

print(my_dict["Apellido"])
print(my_dict["Edad"])
print(my_dict["Lenguaje"])
print(my_dict[1])

#Operadores
print("\nOPERADORES " )

print("Dire" in my_dict) #F porque estamos buscando "CLAVES"
print("Nombre" in my_dict) # "Nombre" es la clave para acceder a "Dire"

print(my_dict.items()) #Returna los conjuntos y subconjuntos
print(my_dict.keys()) #Returna las lista
print(my_dict.values()) #Returna los valores

my_new_dict=my_other_dict.fromkeys(("Nombre",1)) #Crea un diccionario sin valores
print(my_new_dict)

my_new_dict=my_other_dict.fromkeys(("Nombre",1, "Piso"))
print(my_new_dict)

my_new_dict=dict.fromkeys(("Nombre",1,"Piso"))
print(my_new_dict)

my_list=["Nombre",1,"Piso"]
my_new_dict=dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict=dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict=dict.fromkeys(my_dict,["XD"])
print((my_new_dict))


print("\n Diferentes tipos")
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))