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

# accedemos a las filas 1:5 excluyendo 5
print(df[1:5])

# acceso a filas basado en loc
row = df.loc[220] # pero si el índice fuese un string iria el string aqui
print(row) # serie

# acceso a filas basado en loc (dataframe)
row = df.loc[[220]]
print(row)

# acceso a mas filas
rows = df.loc[[220, 1, 100]]
print(rows)

# acceso a ambas
rc = df.loc[[220, 1, 100], ['against_bug', 'against_fire']]
print(rc)

# acceso a todas las filas y columnas especificas
rc = df.loc[:, ['against_bug', 'against_fire']]
print(rc)