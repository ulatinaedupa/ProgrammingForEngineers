# ejecutar en ventana de anaconda command prompt como:
# python program5.py

# declaramos variables
entero = 3
flotante = 4.1
cadena = 'stringify'

# probamos diferentes formas de impresion

print('{}, {}'.format(entero, flotante))
print('%2i, %2.8f' % (entero, flotante))
print(f'%i %s' % (flotante, cadena))
print('\t tab y salto de linea \n' + '\r retorno\rde carro ' + str(44))