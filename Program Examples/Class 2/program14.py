# ejecutar como:
# python program14.py
#
# Métodos de listas
# las cadenas en python no son los unicos que tienen
# metodos, las listas, flotantes, enteros y boleanos
# tambien tienen metodos que podemos utilizar
#
# index(), para tomar el elemento que hace click en la entrada
# count(), para ver el numero de veces un elemento esta en la lista

# creamos una lista de experimentos
valores = [10.2, 29.0, 20.2, 29.0, 87.2]

# imprimimos el valor del indice 20.2
print(valores.index(87.2))

# imprimir cuantas veces aparece 29.0 en la lista
print(valores.count(29.0))