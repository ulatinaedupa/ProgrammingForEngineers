# ejecutar como:
# python program<n>.py
# n es el numero de programa
# Uso de operadores
#

# importamos librerias
import numpy as np
values = np.array([1.4, 0.6, -2.2, -0.1, 2.15, 0.88])

#imprimimos el tipo
print(type(values))

# filtramos por aquellos que son mayores a 1.1
values_filtered = values > 1.1
print(type(values_filtered), values_filtered)

# tomamos los datos de esos indices que son mayores a 1.1
values_subset = values[values_filtered]
print(type(values_subset), values_subset)
