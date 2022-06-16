# ejecutar como:
# python program<n>.py
# n es el numero de programa
# Uso de pandas
#

# importamos librerias
import pandas as pd

# cargamos el dataframe
df = pd.read_csv('pokemon.csv')
print(df.head())