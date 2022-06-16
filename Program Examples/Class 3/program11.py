# ejecutar como:
# python program<n>.py
# n es el numero de programa
# Uso de pandas
#

# importamos librerias
import pandas as pd

# leemos el csv y asignamos la columna 0 como indice
df = pd.read_csv('pokemon.csv', index_col=0)

# imprimimos el dataframe
print(df)