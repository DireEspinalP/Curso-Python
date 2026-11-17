import pandas as pd

data={
    "Nombre":["Ana","Luis", "Carlos", "Lucia"],
    "Nota": [20,14,2,10],
    "Ciudad":["Lima", "Bogota", "Madrid", "Quito"]
}

print(type(data))
print(pd.DataFrame(data))
print(type(pd.DataFrame(data)))