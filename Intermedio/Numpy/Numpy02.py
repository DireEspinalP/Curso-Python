import numpy as np
arr1=np.array([[4,9,16],[25,36,49]])
# Operadores
print(arr1)

print(np.zeros(2)) # Crea arr cero
print(f"\nCopia de arr1 en zeros \n{np.zeros_like(arr1)}  y con shape {np.zeros(arr1.shape)}")

print(np.ones(2)) # Crea arr 1
print(f"\nCopia de arr1 en ones\n {np.ones_like(arr1)}  y con shape {np.ones(arr1.shape)}  \n")

print(f" \n{np.identity(2)}") # Convertir matrix I

print(f" \n{np.sqrt(arr1)}") # Raiz cuadrada

print(f"\n {np.abs(arr1)}")

arr2=np.array([[0.1, 0.3 ,0.6]])
print(f"\n Array de probabilidaes {arr2}")
print(f"\n La suma de las prob. del arr es {np.sum(arr2)}") #Suma de elementos

# Crearemos el operador HADAMAR
arr3=np.array([[1,1],[1,-1]])
H=arr3/np.sqrt(2)
print(f" \n La suma de los elementos del Hadamar  \n {H} es {np.sum(H)}")