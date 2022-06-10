# ejecutar como:
# python program17.py
#
# tambien podemos realizar selectivamente las
# importaciones, por ejemplo podemos importar
# la funcion de conversion de radianes

# definicion del radio
r = 122

# importamos radianes
from math import radians

# calculamos el arco
phi = 45
arc = r*radians(phi)

# imprimimos la longitud del arco
print(arc)