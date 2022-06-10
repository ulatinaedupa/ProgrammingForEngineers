# ejecutar como:
# python program26.py
#
# Aritmetica 2D
# Recordando como realizamos las covnersiones anteriormente
# para arreglos 1D, no es tan diferente para arreglos 2D
# Podemos combinar matrices, numeros, cadenas, vectores, etc
#
#import numpy as np
#np_mat = np.array([[1, 2],
#                   [3, 4],
#                   [5, 6]])
#np_mat * 2
#np_mat + np.array([10, 10])
#np_mat + np_mat
#
# [[ 2  4]
#  [ 6  8]
#  [10 12]]
#

# Importamos numpy como np
import numpy as np

# Creamos una lista 2D
estatura_pesos = [[170, 182, 190, 178, 182, 156, 175, 210],
                  [180, 200, 158, 220, 176, 178, 185, 310]]


# convertimos esta lista en arreglo de numpy
estatura_pesos_np = np.array(estatura_pesos)

# vamos ahora a añadirles unos 10 cm y 20 lb a cada persona
offset = np.array([[10],[20]])
print(100*'=')
print(estatura_pesos_np + offset)

# realizamos conversiones de las estaturas de cm->m, cm->in, cm->ft
convertir = np.array([[0.01], [0.393701], [0.0328084]])
calcular_estaturas = estatura_pesos_np[0, :]*convertir
print(100*'=')
print(calcular_estaturas)
print(100*'=')

# en metros
print(calcular_estaturas[0, :])
print(100*'=')

# en inches
print(calcular_estaturas[1, :])
print(100*'=')

# en ft
print(calcular_estaturas[2, :])