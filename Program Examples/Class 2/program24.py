# ejecutar como:
# python program24.py
#
# Arreglos 2D
# Vimos tambien que es una forma mas comprimida realizar 
# este tipo de arreglos 2D, ahora mismo los datos son manejable
# pero cuando la cantidad de datos crezca es mejor tenerlos 
# apilados y adquiridos en una sola variable

# Importamos numpy como np
import numpy as np

# Creamos una lista 2D
estatura_pesos = [[170, 182, 190, 178, 182, 156, 175, 210],
                  [180, 200, 158, 220, 176, 178, 185, 310]]


# convertimos esta lista en arreglo de numpy
estatura_pesos_np = np.array(estatura_pesos)

# imprimimos forma y tamaño
print(estatura_pesos_np.shape, estatura_pesos_np.size)