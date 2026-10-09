import numpy as np
from numpy import random

# Random
x= random.randint(100)
y=random.rand()
print(f"El num random de x={x}  y={y}\n")

arr1=np.random.randint(100, size=(1,3))
arr2=np.random.randint(100, size=(2,2))
print(f"Random de 1x3: {arr1}")
print(f"Random de 2x2:\n {arr2}")

# Si tengo un arr y quiero elementos cualquiera de ese arr (choise)

arr3=np.array([1,10,40,50,100])
print(f"Numero random del arr3: {np.random.choice(arr3)}") 
print(f"Genera un 2x2 de los elementos de arr3 \n{np.random.choice(arr3, size=(2,2))}\n")
print(f"Random seed: {np.random.seed(42)}") # Semilla para generar numeros random reproducibles
print(f"Permuta de arr3: {np.random.permutation(arr3)}") # Permuta los elementos del arr3
print(f"Randn: {np.random.randn(2,2)}") # Genera un arreglo de 2x2 con numeros random de una distribucion normal estandar