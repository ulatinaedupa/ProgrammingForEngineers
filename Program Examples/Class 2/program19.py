# ejecutar como:
# python program19.py
#
# Primeros pasos con numpy
# ahora que sabemos las dimensiones en pesos 
# que estan en libras nos interes saber cuanto 
# es en kilogramos

# Creamos una lista de datos
pesos = [180, 200, 158, 220, 176, 178, 185, 310]

# Importamos numpy como np
import numpy as np

# creamos un arreglo de numpy basado en la lista
pesos_np = np.array(pesos)

# calculamos en kg
pesos_np_kg = pesos_np*(1/2.204)

# imprimimos el peso en kg
print(pesos_np_kg)