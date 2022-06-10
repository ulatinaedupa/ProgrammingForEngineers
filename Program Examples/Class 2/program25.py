# ejecutar como:
# python program25.py
#
# Subset de Arreglos 2D
# Cada fila y columna tiene un numero fijo de valores
# existen varias maneras sencillas y complicadas de 
# acceder un arreglo
#
# lista de listas
# hola = [["h", "o"], ["l", "a"]]
# [hola[0][0], hola[1][0]]
#
# numpy
# import numpy as np
# hola_np = np.array(hola)
# hola_np[:, 0]
#
# para python regular, acceder a listas es un poco engorroso
# sin embargo para numpy es bastante intuitivo
# el caracter : es el divisor y nos facilita la particion de un arreglo
# observe el codigo inferior para ver como se hace le slicing

# Importamos numpy como np
import numpy as np

# Creamos una lista 2D
estatura_pesos = [[170, 182, 190, 178, 182, 156, 175, 210],
                  [180, 200, 158, 220, 176, 178, 185, 310]]


# convertimos esta lista en arreglo de numpy
estatura_pesos_np = np.array(estatura_pesos)

# imprimimos la fila 1, todos los elementos
print(estatura_pesos_np[1, :])

# imprimimos todas las filas, solo los elementos de la columna 3
print(estatura_pesos_np[:, 3])

# imprimimos el caracter de la fila 1 columna 4
print(estatura_pesos_np[1, 4])