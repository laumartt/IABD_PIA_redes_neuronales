from tabulate import tabulate
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import load_iris
from matplotlib.colors import LightSource
import random

iris=load_iris()

sepal_length=iris.data[0:99,0]
petal_length=iris.data[0:99,2]
flower_type=iris.target[0:99]

x=np.column_stack((sepal_length,petal_length))
y=flower_type


np.random.seed(5)
tf.random.set_seed(5)
random.seed(5)

def fit_compile(capas, x, y, epocas=40):

    model=Sequential()
    model.add(Dense(capas[0], activation='relu',input_dim=2))
    for i in range(1,len(capas)-2):
      model.add(Dense(capas[i], activation='relu'))

    model.add(Dense(capas[-1], activation='sigmoid'))
    model.compile(loss='mean_squared_error')

    model.fit(x, y,epochs=epocas)

    return model

redes=[[2,  4 , 1], [4,  8, 8, 2, 1], [8, 12, 24, 12, 1], [8, 16, 8, 1], [16, 32, 1]]

resultados=[]

for i in range(0,len(redes)-1):
  model=fit_compile(redes[i], x, y)
  resultados1=model.predict(np.array([[4.9,1.4]]))
  resultados2=model.predict(np.array([[6.3,4.9]]))
  index=i+1
  resultados.append([index, resultados1,resultados2])
  print(resultados)

print(resultados)

#model=fit_compile([2,  4 , 1], x, y)

print('\n-----------------------------\n')

print(tabulate(resultados, headers=('indice', 'resultados1', 'resultados2')))