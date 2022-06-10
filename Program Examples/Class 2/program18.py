# ejecutar como:
# python program18.py
#
# Primeros pasos con numpy
# Ahora veremos los primeros pasos en el mundo de datos
# utilzaremos numpy como una herramoient poderosa de analisis
# 
# Estableceremos una lista que representaremos de datos
# para difrentes estaturas y las trataremos con numpy

# Creamos una lista de datos
pesos = [180, 200, 158, 220, 176, 178, 185, 310]

# Importamos numpy como np
import numpy as np

# creamos un arreglo de numpy basado en la lista
pesos_np = np.array(pesos)

# imprimimos el tipo de arreglo
print(type(pesos_np))