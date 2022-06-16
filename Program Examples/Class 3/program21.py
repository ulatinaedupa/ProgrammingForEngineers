# ejecutar como:
# python program<n>.py
# n es el numero de programa
# Uso de operadores
#

# comparacion de cadenas
print("ENA" < 'ena') 

# comparacion numerica y de cadena
try:
    print(3 < 'Chris')
except:
	print('TypeError: unorderable types: int() < str()')
	pass

# comparacion de numero y flotante
print(4 < 8.21)

# importamos librerias
import numpy as np

# cargamos valores
values = np.array([1.4, 0.6, -2.2, -0.1, 2.15, 0.88])

# imprimimos indices de valores
print(values > 1.1)

# booleanos
cierto, falso = True, False

# comparamos valores
and_tabla = [cierto and cierto, 
                   cierto and falso, 
                   falso and cierto, 
                   falso and falso]

print(and_tabla)

# realizamos comparasion de valores
x = 61
print(x > 5 and x < 80)

# comparamos valores
or_tabla = [cierto or cierto,
            cierto or falso, 
            falso  or cierto,
            falso  or falso]
print(or_tabla)

# realizamos comparaciond e valores
y = 4.028
print(y < 6 or y > 10)

# operacion de negacion
print(not cierto, not falso)