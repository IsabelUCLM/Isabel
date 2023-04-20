# 18/04/2023
"""
a = 0
while a < 10:
    print(a)
    if a == 5:
        print("Saliendo del bucle antes de tiempo...")
        break
    a += 1

for a in range(1, 10):
    print(a)
    if a == 5:
        print("Saliendo del bucle antes de tiempo...")
        break

for a in range(1, 10):
    if a == 5 or a == 7:
        print("Se omitió este número...")
        continue
    if a == 9:
        print("Saliendo del bucle antes de tiempo...")
        break
    print(a)

for indice, elemento in enumerate(['rojo', 'azul', 'verde', 'amarillo'], 1):
    print(indice, '-', elemento)
    # ,1 hace que empiece desde el 1.
"""
def convierte():
    print()
    numero = input("Introduce un número:\n")
    sistema = input(
        "Introduce un sistema:\n1-Binario a decimal.\n2-Octal a decimal\n3-Hexadecimal a decimal.\n4-Base 32 a "
        "decimal.\n5-Salir.\n\n")

    if sistema == "1":
        sistema = 2
        final = int(numero, sistema)
        print("El número binario ", numero, " es el número ", final, " en decimales.")

    elif sistema == "2":
        sistema = 8
        final = int(numero, sistema)
        print("El número octal ", numero, " es el número ", final, " en decimales.")

    elif sistema == "3":
        sistema = 16
        final = int(numero, sistema)
        print("El número hexadecimal ", numero, " es el número ", final, " en decimales.")

    elif sistema == "4":
        sistema = 32
        final = int(numero, sistema)
        print("El número con base 32 ", numero, " es el número ", final, " en decimales.")

    elif sistema == "5":
        pass
    else:
        print("No has introducido una opción válida.")


def binario_decimal():
    numero = int(input("Introduce un número:\n"))
    convertido = bin(numero)[2:]
    print(convertido)


def octal_decimal():
    numero = int(input("Introduce un número:\n"))
    convertido = oct(numero)[2:]
    print(convertido)


def hexadecimal_decimal():
    numero = int(input("Introduce un número:\n"))
    convertido = hex(numero)[2:]
    print(convertido)


def menu():
    print("Elige una opción:\n",
          "1-Conversiones a decimal.\n",
          "2-Conversión de decimal a binario.\n",
          "3-Conversión de decimal a octal.\n",
          "4-Conversión de decimal a hexadecimal.\n",
          "5-Salir.\n")

    opcion = input("Escribe un número y pulsa enter: ")

    if opcion == "1":
        convierte()

    elif opcion == "2":
        binario_decimal()

    elif opcion == "3":
        octal_decimal()

    elif opcion == "4":
        hexadecimal_decimal()

    elif opcion == "5":
        pass

    else:
        print("No has introducido una opción válida.")


menu()
