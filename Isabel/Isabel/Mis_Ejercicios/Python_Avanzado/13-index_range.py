# 18/04/2023
"""
a = []
a.extend(range(5000))
print(a)
# Hará un bucle hasta llegar a ese número.
"""


a = [1, 2, 3]
a.extend(range(4, 10))
print(a)

# Concatenar listas
a = [1, 2, 3]
b = [7, 8, 9]
c = a + [4, 5, 6] + b
print(c)


def convierte_binario_octal():
    numero = input("Introduce un número binario: ")
    convertido = int(numero, 2)
    print("El número decimal obtenido es:",convertido, "\nConvirtiendo a octal...")
    convertido2 = oct(convertido)[2:]
    print("El número binario " + numero + " en octal es el número: " + convertido2)

convierte_binario_octal()
