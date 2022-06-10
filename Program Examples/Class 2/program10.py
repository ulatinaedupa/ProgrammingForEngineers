# ejecutar como:
# python program10.py
#
# Trabajando listas (asignando)
# Veamos como de la_lista realizamos una copia
# de la lista.
# Si copiamo a otra variable la_lista, al modificar
# podemos modificar la lista original, para que no
# ocurra esto debemos realizar una copia de la lista


# creamos una lista
la_lista = ["nuevo", 1, "bueno", 3, "sueno", 4, "veneno", 6, "ibuprofeno", 8]
# imprimimos lista en cada momento
print(la_lista)

# de copia_lista
copia_lista = list(la_lista) 
# imprimimos lista en cada momento
print(copia_lista)


# cambiando un valor en la lista
copia_lista[3] = 33
print(la_lista)
print(copia_lista)