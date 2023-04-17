# 12/04/2023 --------------------------------------
# Doc: https://docs.python.org/es/3/tutorial/
# Ejs: https://aprendeconalf.es/docencia/python/ejercicios/cadenas/
"""Escribir un programa que muestre por 
pantalla la cadena ¡Hola Mundo!."""

print("Hola mundo")

"""Escribir un programa que almacene la cadena
¡Hola Mundo! en una variable y luego muestre 
por pantalla el contenido de la variable."""

mundo = "Hola mundo!!!"
print(mundo)

"""Escribir un programa que pregunte
el nombre del usuario en la consola y
después de que el usuario lo 
introduzca muestre por pantalla la cadena 
¡Hola <nombre>!, donde <nombre> 
es el nombre que el usuario haya introducido."""

#nombre= input("Dime tu nombre ")
#print("Así que tu nombre es %s" %(nombre))

"""Escribir un programa que muestre por pantallaqweruiop879+
 el resultado de la siguiente operación aritmética 
 """
resultado = ((3 + 2) / (2 - 5))**2
print(resultado)

"""Escribir un programa que pregunte al usuario por
 el número de horas trabajadas y el coste por hora. Después debe mostrar por
 pantalla la paga que le corresponde."""

#horas = input("Número de horas trabajadas: ")
#coste = input("Coste por hora: ")
#resultado = int(horas) * int(coste)
#print("El resultado de %s horas por un coste de %s es %s euros." %(horas, coste, resultado))

"""Escribir un programa que lea un entero positivo n, 
, introducido por el usuario y después
 muestre en pantalla la suma de todos los enteros
   desde 1 hasta  La suma de los n
 primeros enteros positivos puede ser calculada
   de la siguiente forma:"""

#n = int(input("Introduce un entero positivo: "))
#suma = n * (n+1) / 2
#print("La suma desde %s es %s"%(n,suma))

"""Escribir un programa que pida al usuario
 su peso (en kg) y estatura (en metros), 
 calcule el índice de masa corporal 
 y lo almacene en una variable, 
 y muestre por pantalla la frase 
 Tu índice de masa corporal es <imc> donde <imc> 
 es el índice de masa corporal calculado redondeado 
 con dos decimales."""

#peso = input("¿Cuál es tu peso en kg? ")
#estatura = input("¿Cuál es tu estatura en metros?")
#imc = round(float(peso)/(float(estatura)**2,2))
#print("Tu índice de masa corporal es " + str(imc))

"""Escribir un programa que pida al usuario dos números 
enteros y muestre por pant++alla la <n> entre <m> 
da un cociente <c> y un resto <r> donde <n> y <m> 
son los números introducidos por el usuario, y <c> y <r>
son el cociente y el resto de la división entera
 respectivamente."""

#8+n = int(input("Inserta un número "))
#m = int(input("Inserta otro número "))
#cociente
#c = n / m

#resto
#r = n % m

#print("La división entre %s y %s tiene de cociente %s y resto %s"%(n,m,c,r))

"""Una panadería vende barras de pan a 3.49€ cada una.
El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience
leyendo el número de barras vendidas que no son del día.
Después el programa debe mostrar el precio habitual 
de una barra de pan,
 el descuento que se le hace por no ser fresca 
 y el coste final total."""

n = int(input("Cuántas barras no son del día? "))
precio = 3.49 
descuento = 0.6
final = n * precio * (1 - descuento)
print("El coste de una barra fresca es " + str(precio) + "euros")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(final, 2)) + "euros")
