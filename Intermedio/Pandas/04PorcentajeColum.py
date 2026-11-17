import pandas as pd

titanic=pd.read_csv("Intermedio/Pandas/csv/titanic.csv")
print(f"TITANIC DATASET\n{titanic.head()}")
sobrevivieron=titanic["Survived"]
tasa=sobrevivieron.mean()
print(f"\nTasa de sobrevivencia: {round(tasa*100,2)}%")