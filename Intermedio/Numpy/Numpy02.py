import numpy as np
arr1=np.array([[4,9,16],[25,36,49]])
# Operadores
print(arr1)

print(np.zeros(2)) # Crea arr cero
print(f"\nCopia de arr1 en zeros \n{np.zeros_like(arr1)}  y con shape {np.zeros(arr1.shape)}")

print(np.ones(2)) # Crea arr 1
print(f"\nCopia de arr1 en ones\n {np.ones_like(arr1)}  y con shape {np.ones(arr1.shape)}  \n")

print(f"El eye(3,2) es: \n{np.eye(3,2)}") # No es lo mismo que identity, ya que identity es una matriz cuadrada y eye puede ser rectangular
print(f"El full(3,2) es: \n{np.full((3,2), 7)}") # Crea una matriz de 3 filas y 2 columnas con el valor 7
print(f"El arage(1,10,2) es: \n{np.arange(1,10,2)}") # Crea un arreglo de 1 a 10 con paso de 2
print(f"El linspace(1,10,5) es: \n{np.linspace(1,10,5)}") # Crea un arreglo de 1 a 10 con 5 elementos equidistantes

print(f" \n{np.identity(2)}") # Convertir matrix I

print(f" \n{np.sqrt(arr1)}") # Raiz cuadrada
print(f"\n {np.abs(arr1)}")
print(f"\n {np.exp(arr1)}") # Exponencial
print(f"\n {np.log(arr1)}") # Logaritmo natural
print(f"\n {np.power(arr1,2)}") # Potencia
print(f"\n {np.clip(arr1, 10, 30)}") # Limita los valores del arreglo entre 10 y 30
print(f"\n allclose(arr1>0) {np.allclose(arr1, arr1)}") # Compara si dos arreglos son iguales

# Allclose a diferencia de all, allclose permite comparar arreglos con TOLERANCIA, es decir,
# si los elementos son iguales dentro de un margen de error.




arr2=np.array([[0.1, 0.3 ,0.6]])
print(f"\n Array de probabilidaes {arr2}")
print(f"\n La suma de las prob. del arr es {np.sum(arr2)}") #Suma de elementos
# Crearemos el operador HADAMAR
arr3=np.array([[1,1],[1,-1]])
H=arr3/np.sqrt(2)
print(f" \n La suma de los elementos del Hadamar  \n {H} es {np.sum(H)}")