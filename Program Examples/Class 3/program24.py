# ejecutar como:
# python program<n>.py
# n es el numero de programa
# Uso de operadores
#

# probamos a ver si es impar
a = 1
if a % 2 == 1:
	print('step 1, a es impar')

# probamos a ver si es par
a = 8
if a % 2 == 0:
	print('step 2, a es par')

# probamos ambas con if else
a = 4
if a % 2 == 1:
	print('step 3, a es impar')
else:
	print('step 4, a es par')

# probamos mas con if elif else
b = 7
if b % 4 == 0:
    print('divisible por 4')
elif b % 3 == 0:
	print('divisible por 3')
else:
	print('no es divisible ni por 2 ni por 3')