import pandas as pd

titanic=pd.read_csv("Intermedio/Pandas/csv/titanic.csv")

print(f"\ntitanic.shape: {titanic.shape}")
print(f"\ntitanic.head():\n {titanic.head()}")
#Imprime las primeras 5 filas del dataset, si quieres imprimir más o menos filas usa el parametro n=numero de filas
"""
NaN no siempre son nulos, en el caso de este dataset sí, pero 
habra otros casos donde representen otras cosas como
indeterminaciones matemáticas , errores de cálculo o datos corruptos, etc.
"""
print(f"\ntitanic.info():\n {titanic.info()}")
#   imprime columnas, cantidad de datos no nulos, tipo de dato y memoria usada
#   dtypes: type(cantidad de datos no nulos)
#   memory usage: memoria usada por el dataset

print(f"\ntitanic.describe():\n {titanic.describe()}")
#   imprime estadisticas de las columnas numericas del dataset

"""
count: cantidad de datos no nulos
mean: promedio de los datos
std: desviación estandar de los datos
min: valor minimo de los datos
25%: percentil 25 de los datos
50%: percentil 50 de los datos
75%: percentil 75 de los datos
max: valor maximo de los datos
"""