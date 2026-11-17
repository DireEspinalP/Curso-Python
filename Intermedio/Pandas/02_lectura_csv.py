import pandas as pd

titanic = pd.read_csv("Intermedio/Pandas/csv/titanic.csv")
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


print(f"\nTITANIC DATASET\n{titanic.head()}")
sobrevivieron=titanic["Survived"]
tasa=sobrevivieron.mean()
print(f"\nTasa de sobrevivencia: {round(tasa*100,2)}%")



print(f"\n{titanic.head(3)}")

titanic = pd.read_csv("Intermedio/Pandas/csv/titanic.csv", sep=";") #modifica el separador de columnas, por defecto es ","

print(f"\n{titanic.head(2)}")

titanic = pd.read_csv("Intermedio/Pandas/csv/titanic.csv", usecols=[0, 1, 2]) # selecciona solo las columnas 0, 1 y 2

print(f"\n{titanic.head(2)}")

nulos=["NA", "NaN", "n/a", "null", "NULL", ""] #valores que se consideraran nulos
titanic = pd.read_csv("Intermedio/Pandas/csv/titanic.csv", na_values=nulos) #modifica los valores que se consideraran nulos
print(f"\n{titanic.head(2)}")
print(f"\n{titanic.isnull().sum()}") #imprime la cantidad de valores nulos por columna