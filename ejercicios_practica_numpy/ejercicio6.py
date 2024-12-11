'''Ejercicio 6: Matrices e Iris
Carga los datos del ejemplo de las flores con el siguiente código:'''

import numpy as np
from sklearn.datasets import load_iris
datos=load_iris().data
resultado=load_iris().target

#Crea un array llamado x con las 99 primeras filas , la 1º columna y la 3º columna 
# de la matriz datos
x=np.array(datos[0:98, [0,2]])
#Crea un array llamado y con las 99 primeras filas del vector resultado
y=x[0:98]