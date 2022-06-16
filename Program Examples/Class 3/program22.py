# ejecutar como:
# python program<n>.py
# n es el numero de programa
# Uso de operadores
#

#importamos librerias
import numpy as np

# cargamos valores
values = np.array([1.4, 0.6, -2.2, -0.1, 2.15, 0.88])
values = values ** 3 # elevamos al cubo 

print(values > 0.5)

print(values < 0.5)


print(values > -0.1 and values < 1)