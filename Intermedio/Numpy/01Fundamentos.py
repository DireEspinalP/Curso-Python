import numpy as np

arr1=np.array([1,2,3,4,5,6,7])
arr2=np.array([[1,2,3], [4,5,6]])

# Acceso a los elementos de un arreglo
print(f"El primer elemento de arr1 es: {arr1[0]}")
print(f"El primer elemento de arr2 es: {arr2[0,2]}")
print(arr1[1]+arr2[1,1]) 
#Ten en cuenta que los indices son i-1 para la matriz
arr4 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr4[1, -1])

# Acceso a rangos de elementos
print(arr1[2:4])
print(arr2[0:2, 1:3])
print(arr1[:2])
print(arr2[2:])
print(arr1[::2])
print(arr1[1:5:2])
print(arr2[::2, ::2])

arr4=np.array([[1,2,3], [4,5,6], [7,8,9]])
print(f"El where de arr4 es: {np.where(arr4>5)}") # Indices de los elementos mayores a 5
print(f"El copy de arr4 es: {arr4.copy()}") # Copia del arreglo