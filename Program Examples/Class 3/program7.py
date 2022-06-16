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

# añadiendo mas datos
more_years = [1994, 1995, 1996, 1997]
more_heights = [1.77, 1.77, 1.78, 1.78]
year = year + more_years
height = height + more_heights

# creamos el grafico
plt.plot(year, height)
#plt.scatter(year, height)

# agregamos leyenda a ejes
plt.xlabel('años')
plt.ylabel('alturas')
plt.title('Mi altura a traves de los años')
plt.yticks([1.71, 1.72, 1.73, 1.74, 1.75, 1.76, 1.77, 1.78],
	       ['1B', '1B', '2B', '3B', '4B', '5B', 'UNI', 'UNI_END'])

# mostramos el grafico
plt.show()