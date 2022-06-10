# ejecutar como:
# python program3.py
#
# Lista de listas
# Tenemos la necesidad de procesar muchos datoas.
# En vez de crear una lista de cadenas y flotantes podemos 
# crear lista.
# Note la diferencia entre variables y cadenas


x1 = 11.2
x2 = 480
x3 = 128
x4 = 22.2

# etiquetamos cada parte de la figura en la lista de listas
x_coord = [["borde",  x1], 
           ["fin"  ,  x2], 
           ["centro", x3], 
           ["foco", x4]]

# imprimimos las coordenadas
print(x_coord)

#imprimimos el tipo
print(type(x_coord))