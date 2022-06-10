# ejecutar como:
# python program6.py
#
# Extrayendo segmentos
# Extraer valores solo es una seccion de las acciones
# que quisieramos hacer, a veces queremos extraer mas 
# valores que simplemente uno solo, en listas esto es
# la_lista[valor_inicial:valor_final]
# note que el valor_final es no inclusivo y no tiene
# relacion a la cantidad de datos a extraer


# creamos una lista
la_lista = ["nuevo", 1, "bueno", 3, "sueno", 4, "veneno", 6, "ibuprofeno", 8]

# de nuevo a veneno
nuevo_a_veneno = la_lista[0:7]

# de 3 a 6
de_3a6 = la_lista[3:8] 

# todos despues de sueno
todos_despues_de_sueno = la_lista[5:9]

# imprimimos extractos de listas
print(la_lista)
print(nuevo_a_veneno)
print(de_3a6)
print(todos_despues_de_sueno)