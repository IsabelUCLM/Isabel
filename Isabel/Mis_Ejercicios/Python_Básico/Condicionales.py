# 12/04/2023 --------------------------------------
"""Escribir un programa que pregunte al usuario su edad y
 muestre por pantalla si es mayor de edad o no."""

"""edad = int(input("Dime tu edad "))
if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")"""

"""Escribir un programa que almacene la cadena de caracteres
contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla
si la contraseña introducida por el usuario coincide 
con la guardada en la variable sin tener en cuenta mayúsculas 
y minúsculas."""

"""clave = input("Dime una clave ")
nuevaclave = input("Repítela a ver si coincide ")
if clave.lower() != nuevaclave.lower():
    print("Es diferente")
else:
    print("Es igual.")"""

# 13/04/2023 --------------------------------------
"""Escribir un programa que pida al usuario dos números
y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error."""
"""n1 = int(input("Dime un número dividendo "))
n2 = int(input("Dime un número divisor "))

if n2 == 0:
    print("Error. El divisor no puede ser 0.")
else:
    print("El resultado es ", int(n1/n2))"""

"""Para tributar un determinado impuesto se debe ser mayor 
de 16 años y tener unos ingresos iguales o superiores a
1000 € mensuales. Escribir un programa que pregunte al
usuario su edad y sus ingresos mensuales y muestre por
pantalla si el usuario tiene que tributar o no."""
#edad=int(input("Edad? "))
#ingresos=(int(input("Ingresos? ")))

#if edad > 16 and ingresos >= 1000:
#    print("Puedes tributar.")
#else:
 #   print("No puedes tributar.")

"""La pizzería Bella Napoli ofrece pizzas vegetarianas y 
no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen 
a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere
una pizza vegetariana o no, y en función de su respuesta le
muestre un menú con los ingredientes disponibles 
para que elija. Solo se puede eligir un ingrediente además de
la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es
vegetariana o no y todos los ingredientes que lleva.""" 

print("== BELLA NAPOLI ==")
tipo=int(input("A continuación se te ofrece: \n 1. Pizza vegetariana \n 2. Pizza no vegetariana \n Escribe 1 o 2. \n"))
if tipo == 1:
    ingrediente=str(input("Los ingredientes son: \n * Pimiento \n * Tofu \n"))
    if ingrediente == "Pimiento":
        print("Has elegido la pizza tipo %s con %s. Además contiene mozzarella y tomate. "%(tipo,ingrediente))
    elif ingrediente == "Tofu":
        print("Has elegido la pizza tipo %s con %s. Además contiene mozzarella y tomate. "%(tipo,ingrediente))
    else:
        print("Escribe Pimiento o Tofu.")
elif tipo == 2:
    ingrediente=str(input("Los ingredientes son: \n * Salmón \n * Jamón \n Escribe Salmón o Jamón. \n"))
    if ingrediente == "Salmón" or ingrediente == "Salmon":
        print("Has elegido la pizza tipo %s con %s. Además contiene mozzarella y tomate. "%(tipo,ingrediente))
    elif ingrediente == "Jamón" or ingrediente == "Jamon":
        print("Has elegido la pizza tipo %s con %s. Además contiene mozzarella y tomate. "%(tipo,ingrediente))
    else:
        print("Escribe Salmón o Jamón.")