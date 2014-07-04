'''
Created on Jul 2, 2014

@author: viejoemer

HowTo delete a key and keeping the value at the same time in python?

¿Cómo eliminar una clave y mantener el valor, al mismo tiempo en python?

'''

#Creating a dict with data
d = {
     "red":100,
     "yellow":200,
     "blue" : 300
     }
print(d)

#Using pop to delete a key and keeping the value
value = d.pop("red")
print(d)
print(value)
