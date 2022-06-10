# ejecutar como:
# python program22.py
#
# Subset de datos
# hemos visto diferentes manera de interaccion de datos
# por medio de listas y numpy arrays
# tambien vimos que numpy y listas se comportan diferente
# en el momento de agregar datos, pero para hacer subsets
# se comportan bastante parecido
# los siguientes conjuntos de datos nos ayudaran a entender
# el subsetting

# Importamos numpy como np
import numpy as np

# Creamos una lista de datos
estatura = [170, 182, 190, 178, 182, 156, 175, 210]
pesos = [180, 200, 158, 220, 176, 178, 185, 310]


# creamos un arreglo de numpy basado en la lista
pesos_np = np.array(pesos)
estatura_np_m = np.array(estatura)/100

# imprimimos el peso al indice 6
print(pesos_np[6])

# imprimimos las estaturas del indice 1 al 5
print(estatura_np_m[1:6])