# ejecutar como:
# python program16.py
#
# utilizaremos un paquete para
# importar librerias matematicas y
# realizar calculos de perimetro y area

# definicion del radio
r = 0.22

# importamos el paquete de matematicas
import math

# calculamos el perimetro de una esfera
P = 2*math.pi*r

# calculamos el area de esa seccion
A  = math.pi*r**2

# calculamos el volumen
V = math.pi*r**3

# imprimimos valores
print(f'Perimetro: {P}')
print(f'Area: {A}')
print(f'Volumen {V}')