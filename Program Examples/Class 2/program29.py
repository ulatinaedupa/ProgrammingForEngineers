# ejecutar como:
# python program29.py
#
# Ahora vamos a ver de manera rapida todo lo que hemos aprendido
# tenemos entonces letras asignadas a cada color de vehiculo
# y valores que corresponden a sus precios en miles
# carros_color = ['A', 'V', 'N', 'R', 'C' ... 'A']
# carros_precio = [20.2, 17.5, 15.75, ... 9.5]
# cada elemento de la lista corresponde a cada carro.
# A = Azul, V = Verde, N = Negro
# El precio 20.2 corresponde a 20200 USD
# Necesitamos hacer analitica basica para establecer el precio
# del mercado y ver si cambia por color y otras condiciones

# Importamos numpy como np
import numpy as np

# Creamos una lista 2D
carro_color  = ['A',   'V',  'N',  'C',  'B',  'P',  'A',  'N',  'B',  'N',  'A',  'V',  'N',  'A',  'B',  'N',   'P']
carro_precio = [10.2, 15.5, 14.2, 25.6, 40.2, 30.8, 12.5, 22.4, 25.2, 40.8, 50.2, 35.2, 38.7, 22.1, 40.2, 21.5, 16.75]


# convertimos las listas en arreglos numpy
carro_color_np, carro_precio_np = np.array(carro_color), np.array(carro_precio)


# observamos los carros que sean 'A' o amarillos
carro_color_A = carro_color_np == 'A'

# conseguimos los precios de estos carros
carro_precio_np[carro_color_A]

# imprimimos la media de estos carros
print(f'La media de estos carros anda alrededor de {round(np.mean(carro_precio),3)}')