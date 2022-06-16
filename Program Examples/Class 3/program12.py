# ejecutar como:
# python program<n>.py
# n es el numero de programa
# Uso de pandas
#

# importamos librerias
import pandas as pd

# leemos el csv y asignamos la columna 0 como indice
df = pd.read_csv('pokemon.csv')
print(df.head())

# imprimimos los nombres de las columnas
print(df.columns)
print()

# accedemos a la columna 'against_fire'
print(df['against_fire'])
print(type(df['against_ground']))