# 13/04/2023
"""# ----------- LISTAS -----------
fruta = ['manzana', 'manzana', 'platano', 'pera']
print(fruta)
fruta.append('fresa') # Solo añade un argumento.
print(fruta)
fruta.pop(0) # Solo acepta integers. Elimina posición 0.
print(fruta)
fruta.sort() # Ordena por letras.
print(fruta)
print(fruta.count('fresa'))
print(fruta.index('platano')) # Indica la posición.
fruta.clear() # Elimina todo el contenido de la lista.
print(fruta)
# ----------- TUPLAS -----------
tupla = 123, 'hola', 15.3
otra_tupla = () # Tupla vacía.
print(tupla[1]) # Muestra
# tupla.append('prueba') NO PUEDES AÑADIR.
print(len(tupla))
print(len(otra_tupla))
# ----------- CONJUNTOS (set) -----------
fruta2 = {'manzana','manzana', 'fresa', 'platano'}
# Los conjuntos eliminan datos repetidos.
print(fruta2)
print('fresa' in fruta2) # Devuelve true si se encuentra
# ----------- DICCIONARIOS -----------
numeros = {'bprimeros':123, 'asegundos':456}
print(numeros)
print(numeros['bprimeros'])
print(list(numeros))
print(sorted(numeros)) # Ordena
print('asegundos' in numeros) # True si lo encuentra
"""
"""Escribir un programa que almacene las asignaturas de un
curso (por ejemplo Matemáticas, Física, Química, Historia
y Lengua) en una lista y la muestre por pantalla."""
"""asignaturas = ['Física','Literatura', 'Historia']
notas = []
print(asignaturas)
print("Primero estudiaré " + asignaturas[0] + ", luego, " + asignaturas[1] +".")
for i in range(3):
    nota=int(input('¿Qué nota has sacado en ' + asignaturas[i] + "? "))
    notas.append(nota)
    print("He sacado un " + str(notas[i]) + " en " + str(asignaturas[i]) + ".")"""

"""Escribir un programa que almacene en una lista
los números del 1 al 10 y los muestre por pantalla
en orden inverso separados por comas."""

"""numeros=[1, 2, 3, 4, 5]
for i in range(1, 6):
    print(numeros[-i], end=",")"""

"""
Escribir un programa que guarde en un diccionario
los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos 
y muestre por pantalla el precio de ese número de kilos 
de fruta. Si la fruta no está en el diccionario debe 
mostrar un mensaje informando de ello.
"""
frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('¿Fruta deseada? ')
kg = float(input('¿Kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'cuestan', frutas[fruta]*kg, '€')
else: 
    print("La fruta", fruta, "no está.")


