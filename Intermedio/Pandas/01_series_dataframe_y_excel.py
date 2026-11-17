import pandas as pd 

edades=pd.Series([25,30,22,35], ["Ana", "Luis", "Carlos", "Sofia"])
print(f"\n{edades}")
#Imprime la Serie([datos, indice]) con ordenamiento posicional
edades=pd.Series(index=["Ana", "Luis", "Carlos", "Sofia"], data=[25,30,22,25]) #otra forma 
print(f"\n{edades}")

numeracion=pd.Series([12,3,4,51,5])
print(f"\n{numeracion}")


"""
 En si es una sola columna con todo sus datos etiquetado por indices. (al principio no lo hagas caso)
Si quieres usar varias columnas usa un DataFrame

"""


data={
    "Nombre":["Ana","Luis", "Carlos", "Lucia"],
    "Nota": [20,14,2,10],
    "Ciudad":["Lima", "Bogota", "Madrid", "Quito"]
}

print(type(data))
print(pd.DataFrame(data))
print(type(pd.DataFrame(data)))