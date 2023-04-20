# 13/04/2023
"""Escribir un programa que pida al usuario una palabra
 y la muestre por pantalla 5 veces."""
"""palabra=str(input("Escribe una palabra y la mostraré 5 veces: "))
for i in range (5):
    print(palabra)"""

"""Escribir un programa que pregunte al usuario su edad 
y muestre por pantalla todos los años que ha cumplido 
(desde 1 hasta su edad)."""
"""edad=int(input("Cuál es tu edad? "))
contador=0

for i in range(edad):
    result=contador=1+contador
    print(result)"""

"""Escribir un programa que pida al usuario un número entero
positivo y muestre por pantalla todos los números impares
desde 1 hasta ese número separados por comas."""
"""n1= int(input("Dime un número: \n"))
if n1 >= 0:
    for i in range(1, n1, 2):
            # (de aqui, hasta aqui, con una suma de)
            print("Números impares: " + str(i))
else:
    print("Solo se aceptan números mayores a 0.")"""

"""Escribir un programa que almacene la cadena de caracteres
 contraseña en una variable, pregunte al usuario por la 
 contraseña hasta que introduzca la contraseña correcta."""

"""clave=str(input("Introduce una clave:\n"))
c = str(input("Clave guardada. Repítela:\n"))
if clave != c:
    acierto= False
    while acierto == False:
        c = str(input("Error. Repítela:\n"))
elif clave == c:
    acierto=True
    print("Clave correcta.")"""

"""Haz un menú donde selecciones tu color favorito
 entre rojo, verde y azul."""


color = str(input("selecciona tu color favorito entre rojo, verde y azul.\n"))

rojo = "rojo"
verde = "verde"
azul = "azul"

print(color)
match color:
    case str(rojo):
        print("Tu color favorito es el rojo.")
    case str(verde):
        print("Tu color favorito es el verde.")
    case str(azul):
        print("Tu color favorito es el azul.")
    case other:
        print("Así que es otro color... curioso.")
