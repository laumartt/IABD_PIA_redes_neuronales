



import numpy as np
x=np.linspace(-6,6,20)              #Crea 20 valores entre 6 y -6
y=np.linspace(-6,6,20)
x,y=np.meshgrid(x,y)                #Todas las combinaciones posibles 
z=np.sin(np.sqrt(x ** 2 + y ** 2))  #Cálculo de z
