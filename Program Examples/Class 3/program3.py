# ejecutar como:
# python program<n>.py
# n es el numero de programa
# Creación de un grafico de dispersion X,Y
#

# importamos librerias
import matplotlib.pyplot as plt

# creamos datos
datos = [0, 1, 2, 3, 4, 8, 5, 4, 2, 1, 0, 0, 5, 9, 10, 1, 3, 6, 8]

# graficamos histograma
plt.hist(datos, bins=4)
plt.show()