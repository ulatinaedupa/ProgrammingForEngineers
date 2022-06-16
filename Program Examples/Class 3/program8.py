# ejecutar como:
# python program<n>.py
# n es el numero de programa
# Creación de diccionarios en python
#

# diccionario vacio
d = dict() 
print(d, type(d))
d = {}
print(d, type(d))

# creacion de diccionario
d = dict(zip(['ana', 'beto', 'juan'], [1, 2, 4]))
print(d)

d = {'ana':2, 'beto':4, 'juan':8}
print(d)

# tomamos por llave
print(d['juan'])