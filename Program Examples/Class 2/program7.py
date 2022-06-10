# ejecutar como:
# python program7.py
#
# Extrayendo segmentos de lista de listas
# Es posible tambien extraer información no 
# especificando los indices.  Si hace esto
# ira desde el punto hasta el final especificado


# creamos una lista
la_lista = ["nuevo", 1, "bueno", 3, "sueno", 4, "veneno", 6, "ibuprofeno", 8]

# de nuevo a veneno
nuevo_a_veneno = la_lista[:7]


# todos despues de sueno
todos_despues_de_sueno = la_lista[5:]

# imprimimos extractos de listas
print(la_lista)
print(nuevo_a_veneno)
print(todos_despues_de_sueno)