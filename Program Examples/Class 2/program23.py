# ejecutar como:
# python program23.py
#
# Arreglos 2D
# ahora estaremos utilizando valores para contener
# un arreglo 2D.
# Tendremos un conjunto de datos arbitrario y empezaremos 
# A observar tipos y su contenido

# Importamos numpy como np
import numpy as np

# Creamos una lista 2D
estatura_pesos = [[170, 182, 190, 178, 182, 156, 175, 210],
                  [180, 200, 158, 220, 176, 178, 185, 310]]


# convertimos esta lista en arreglo de numpy
estatura_pesos_np = np.array(estatura_pesos)

# imprimimos tipo
print(type(estatura_pesos_np))

# imprimimos la forma del arreglo
print(estatura_pesos_np.shape)