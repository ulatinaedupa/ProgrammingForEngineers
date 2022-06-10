# ejecutar como:
# python program28.py
#
# tambien podemos realizar analiss exploratorio
# podemos encontrar el error en las medidas
# utilizando nuestra data de muestra

# Importamos numpy como np
import numpy as np

# Creamos una lista 2D
estatura_pesos = [[170, 182, 190, 178, 182, 156, 175, 210],
                  [180, 200, 158, 220, 176, 178, 185, 310]]


# convertimos esta lista en arreglo de numpy
estatura_pesos_np = np.array(estatura_pesos)


# Imprimimos la medianas de los pesos
med_pesos = np.median(estatura_pesos_np[:, 1])
print("Mediana: " + str(med_pesos))

# Imprimimos la desviacion estandard de las estaturas.
stddev_estatura = np.std(estatura_pesos_np[:,0])
print("Desviacion estandard: " + str(stddev_estatura))

# Imprimimos la correlacion de la primera y segunda columnas
corr_est_peso = np.corrcoef(estatura_pesos_np[:, 0], estatura_pesos_np[:, 1])
print("Correlacion: " + str(corr_est_peso))