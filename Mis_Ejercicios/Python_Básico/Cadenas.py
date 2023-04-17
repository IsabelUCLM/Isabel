# 12/04/2023 --------------------------------------
"""Escribir un programa que pregunte el nombre del usuario
 en la consola y un número entero e imprima por pantalla 
 en líneas distintas el nombre del usuario tantas veces 
 como el número introducido."""

#usuario=input("Dime tu nombre de usuario")
#n=input("Dime un número entero")
#print((usuario + "\n") * int(n))

"""Escribir un programa que pregunte el nombre completo
del usuario en la consola y después muestre por pantalla
el nombre completo del usuario tres veces, 
una con todas las letras minúsculas, 
otra con todas las letras mayúsculas y otra
solo con la primera letra del nombre y de los apellidos
en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas
y minúsculas como quiera."""

#nombre = str(input("Dime tu nombre "))
#print(nombre.lower() + "\n" + nombre.upper() + "\n" + nombre.title())
# Capitalize solo convierte la 1 letra en mayusc de 1 palabra
# title convertira la 1 letra de todas las palabras

"""Escribir un programa que pregunte el nombre del usuario en la consola y 
después de que el usuario lo introduzca muestre por pantalla
 <NOMBRE> tiene <n> letras, 
 donde <NOMBRE> es el nombre de usuario en mayúsculas y
<n> es el número de letras que tienen el nombre."""

#nombre=input(str("Nombre de usuario?"))
#n = len(nombre)
#print("%s tiene %s letras"%(nombre,n))

"""Los teléfonos de una empresa tienen el siguiente formato
 prefijo-número-extension donde el prefijo es el código
 del país +34, y la extensión tiene dos dígitos
(por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número 
de teléfono con este formato y muestre por pantalla
el número de teléfono sin el prefijo y la extensión."""

#telefono = input("Indica número de teléfono ")
#print("El teléfono es ", telefono[4:-3])

"""Escribir un programa que pida al usuario que introduzca una frase en la consola
 y muestre por pantalla la frase invertida."""

#cadena = input(str("Nombre? "))
#print(cadena[::-1])


"""Escribir un programa que pregunte al usuario la fecha
de su nacimiento en formato dd/mm/aaaa y muestra por
pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione 
cuando el día o el mes se introduzcan con un solo
carácter."""

fecha = input(("Introduce fecha de nacimiento con / "))
print("Dia: " , fecha[:2] , "Mes: " , fecha[4:5] , "Año: ", fecha[6:10] )