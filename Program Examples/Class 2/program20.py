# ejecutar como:
# python program20.py
#
# Primeros pasos con numpy
# Seguido podriamos calcular el indice de masa corporal
# para esto necesitamos la estatura y los pesos

# Importamos numpy como np
import numpy as np

# Creamos una lista de datos
estatura = [170, 182, 190, 178, 182, 156, 175, 210]
pesos = [180, 200, 158, 220, 176, 178, 185, 310]


# creamos un arreglo de numpy basado en la lista
pesos_np = np.array(pesos)
estatura_np_m = np.array(estatura)/100

# calculamos en kg
pesos_np_kg = pesos_np*(1/2.204)

# calculamis el IMC
IMC = pesos_np_kg / estatura_np_m ** 2

# imprimimos
print(IMC) 