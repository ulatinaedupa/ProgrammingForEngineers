# ejecutar como:
# python program<n>.py
# n es el numero de programa
# Uso de pandas
#

# importamos librerias
import pandas as pd
import numpy as np

# creamos un diccionario
d = {'hora':[1, 2, 4, 6, 10], 
     'lugar':['sala', 'cocina', 'comedor', 'baño', 'cuarto'],
     'cantidad':[2.2, 4.85, 5.22, 4.2, 6.56]}

# creamos el dataframe
df = pd.DataFrame(d)

# cambiamos el valor de los indices
df.index = ['A0', 'B0', 'C0', 'D0', 'E0']

# imprimimos indices
print(df)

# 1 - seleccionamos las columnas
print()
col_cant = df.iloc[:, 2] # lo mismo a col_cant = df.loc[:, "cantidad"]
print(col_cant)

# 2 - comparamos con las cantidades que nos da mas de 5.5
print()
idx = col_cant > 5.5
print(idx)

# 3 - Filtramos y presentamos
cant_55 = df[idx]
print(cant_55)

# realizamos un filtro logico
filtro = np.logical_and(df['cantidad'] > 4, df['cantidad'] < 6)
print(filtro)

# imprimimos el resultado
print(df[filtro])