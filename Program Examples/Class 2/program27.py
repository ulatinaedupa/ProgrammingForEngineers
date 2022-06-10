# ejecutar como:
# python program27.py
#
# Estadisticas basica con numpy
# Para realizar estadistica basica simplemente
# conviene importar la libreria y aplicar las funciones
# import numpy as np
# samples = [0.2, 0.4, 0.6, 0.8, 1.0]
# np.mean(samples) # samples.mean()
# np.median(samples) # samples.median()

# Importamos numpy como np
import numpy as np

# Creamos una lista 2D
estatura_pesos = [[170, 182, 190, 178, 182, 156, 175, 210],
                  [180, 200, 158, 220, 176, 178, 185, 310]]


# convertimos esta lista en arreglo de numpy
estatura_pesos_np = np.array(estatura_pesos)

# tomamos solo las estaturas
estatura_np = estatura_pesos_np[0,:]

# aplicamos la mediana
print(np.median(estatura_np))

# aplicamos la media
print(np.mean(estatura_np))