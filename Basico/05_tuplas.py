### TUPLAS () ###

"""
Lista
my_list=list()
my_other_list=[]

Tupla
my_tuple=tuple()
my_other_tuple=()

es un conjunto de valores

"""
my_tuple=tuple()
my_other_tuple=()

my_tuple=(18,1.72, "Dire" ,"Espinal", "Dire")
my_other_tuple=(1,4,5,"Hola","Mundo")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[-5]) Error fuera de rango
#print(my_tuple[4])  Error fuera de rango

print(my_tuple.count("Dire"))
print(my_tuple.index("Espinal"))
print(my_tuple.index("Dire"))

# my_tuple[1]=1.80 Error, porque no podemos signar como tal
print(my_tuple+my_other_tuple)

my_sum_tuples=my_tuple+my_other_tuple
print(my_sum_tuples)

print(my_sum_tuples[3:6])

my_tuple=list(my_tuple)
print(type(my_tuple))

my_tuple.insert(1, "PERU")
print(type(tuple(my_tuple)))
print(my_tuple)
