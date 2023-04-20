# 13/04/2023
def saludo():
    print("Hola")

saludo()


"""Escribir una función que reciba una muestra de números
 en una lista y devuelva su media."""

def media(n):
    return sum(n)/len(n)

print(media([1, 2, 3, 4, 5]))
print(media([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

# Calcula los cuadrados de una lista.
def cuadrado(b):
    lista = []
    for i in b:
        lista.append(i**2)
    return lista

print(cuadrado([1, 2, 3, 4, 5]))
print(cuadrado([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

 #Función que calcula el area de un círculo.
def cirarea(r):
    pi = 3.1415
    return pi*r**2

#Función que calcula el volumen de un cilindro a partir del área del círculo.
def volumen(r, h):
    return cirarea(r)*h
print(volumen(3,5))

