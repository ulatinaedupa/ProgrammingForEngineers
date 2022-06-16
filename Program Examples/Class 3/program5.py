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
plt.plot(year, height)
#plt.scatter(year, height)

# agregamos leyenda a ejes
plt.xlabel('años')
plt.ylabel('alturas')
plt.title('Mi altura a traves de los años')
plt.yticks([1.705, 1.71, 1.715, 1.72, 1.725, 1.73, 1.735,
            1.74, 1.745, 1.75, 1.755, 1.76, 1.765, 1.77])

# mostramos el grafico
plt.show()