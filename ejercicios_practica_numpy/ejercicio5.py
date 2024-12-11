'''
Ejercicio 5: Matrices e Iris
Carga los datos del ejemplo de las flores con el siguiente código:'''
import numpy as np
from sklearn.datasets import load_iris
datos=load_iris().data
resultado=load_iris().target

#Crea un array llamado sepal_length con las 99 primeras filas y la 1º columna de la matriz datos
sepal_length=np.array(datos[0:98, 0])
print('---------------------')
#Crea un array llamado petal_length con las 99 primeras filas y la 3º columna de la matriz datos
petal_lenght=np.array(datos[0:98, 2])
print('---------------------')
#Crea un array llamado x juntando las 2 columnas sepal_length y petal_length
x=np.column_stack((sepal_length, petal_lenght))
print('---------------------')
#Crea un array llamado y con las 99 primeras filas del vector resultado
y=x[0:98, :]
print('---------------------')