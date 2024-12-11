import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import random
from time import perf_counter
from keras.models import Sequential
from keras.layers import Dense

#Calculo del modelo
def compile_fit(capas,x,y,epochs,activacion,activacion_salida):

    if x.ndim==1:
        x_dim=1
    else:
        x_dim=np.shape(x)[1]

    np.random.seed(5)
    tf.random.set_seed(5)
    random.seed(5)
     
    model=Sequential()
    for index,neuronas_capa in enumerate(capas):
        if (index==0):
            model.add(Dense(neuronas_capa, activation='relu',input_dim=x_dim))
        elif (index==len(capas)-1):
            model.add(Dense(y.shape[1], activation=activacion_salida))
            '''activacion salida-sigmoid-salida de 0-1
                       linear-valor
                       softmax-varias neuronas de salida
                       '''
        else:
            model.add(Dense(neuronas_capa, activation=activacion))
    model.compile(loss='mean_squared_error')
    
    tiempo_entrenamiento= perf_counter()

    history=model.fit(x,y,epochs=epochs,verbose=False)

    #Tiempo de entrenamiento
    tiempo_entrenamiento=perf_counter()-tiempo_entrenamiento    
 
    return model,history, tiempo_entrenamiento


#Calculo del Mean Squared Error
#Mejor con numeros bajos
def get_mse(y_true,y_pred):
    y_error=(y_true-y_pred)**2
    mse=np.sum(y_error)/np.size(y_true)
    return mse

#Calculo del coeficiente de determinacion
#rango[-inf,1], siendo 1 sin error y 0 malo
def get_coef_determinacion(y_true,y_pred):
    media_valores_verdaderos=np.sum(y_true)/np.size(y_true)
    suma_errores=np.sum((y_true-y_pred)**2)
    suma_valores_media=np.sum((y_true-media_valores_verdaderos)**2)
    coef_determinacion=1-(suma_errores/suma_valores_media)
    return coef_determinacion
    

def get_metricas_modelo(model,x,y_true):
    y_pred=model.predict(x,verbose=False)
    mse=get_mse(y_true,y_pred)
    coeficiente_determinacion=get_coef_determinacion(y_true,y_pred)
    return mse,coeficiente_determinacion