'''Ejercicio 11: Funciones a arrays
Crea una función llamada f que acepte como parámetro el número y que retorne el valor multiplicado por 2 y 
además que se le sume 1.'''

def funcion(param):
  return param*2+1

funcion(8)

#Crea ahora el vector de numpy [1,5,4,7,3,9,8,6] y aplícale la función f

a=np.array([1,5,4,7,3,9,8,6])

b=np.array([funcion(i) for i in a])
print(b)

b=funcion(a)
print(b)