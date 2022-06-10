# ejecutar como:
# python program12.py
#
# Multiples argumentos
# Ahora utilizaremos la funcion sorted()
# Observe los argumentos que acepta
# iterable, key y reverse
# key=None, simboliza que no especifica un argumento key, será None.
# reverse=False, quiere decir que no especifica en forma inversa

# creamos dos listas de variables
x1 = [10, 20, 30, 40]
x2 = [1.2, 2.3, 3.4, 4.5]

# unificamos ambas listas
x12 = x1 + x2

# ordenamos las listas en orden mayor a menor
x12_ordenada = sorted(x12, reverse=True)

# imprimimos la lista ordenada
print(x12_ordenada)