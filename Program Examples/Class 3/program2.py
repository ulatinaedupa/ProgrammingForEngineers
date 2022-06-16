# ejecutar como:
# python program<n>.py
# n es el numero de programa
# Creación de un grafico de dispersion X,Y
#

# importamos librerias
import matplotlib.pyplot as plt

# creamos un conjunto de datos
# NOTA:  para graficar deben coincidir en cantidad de datos
year = [1990, 1991, 1992, 1993]
height = [1.70, 1.72, 1.76, 1.77]

# creamos el grafico
plt.scatter(year, height)

# mostramos el grafico
plt.show()