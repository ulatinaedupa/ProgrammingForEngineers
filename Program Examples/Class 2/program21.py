# ejecutar como:
# python program21.py
#
# Subset de datos
# los subset de datos se consiguen de diferentes maneras
#
# x = [1, 2, 3 , 5]
# x[2]
# import numpy as np
# y = np.array(x)
# y[1]
# para numpy especificamente podemos conseguir un subset mas filtrado
# mayores_que_2 = y > 2
# y[mayores_que_2]
# el codigo inferor podemos filtrar por personajes que tengan un IMC bajo

# Importamos numpy como np
import numpy as np

# Creamos una lista de datos
estatura = [170, 182, 190, 178, 182, 156, 175, 210]
pesos = [180, 200, 158, 220, 176, 178, 185, 310]


# creamos un arreglo de numpy basado en la lista
pesos_np = np.array(pesos)
estatura_np_m = np.array(estatura)/100

# calculamos en kg
pesos_np_kg = pesos_np*(1/2.204)

# calculamis el IMC
IMC = pesos_np_kg / estatura_np_m ** 2

# filtrapos por aquellos que tengan un IMC < 30
IMC_menor_30 = IMC < 30

# imprimimos el resultado del filtro
print(IMC_menor_30)

# imprimimos los IMC
print(IMC[IMC_menor_30]) 