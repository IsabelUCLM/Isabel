# 18/04/2023
# BINARIO A DECIMAL
print(int('10100111', 2))
# 2 porque es para binario
"""
def convierte():
    numero = input('Introduce un número:\n')
    sistema = int(input('Introduce un sistema de conversión:\n'))
    print(int(numero, sistema))
# CALCULADORA CONVERSORA

convierte()
"""

# DECIMAL A BINARIO
def binario_decimal():
	numero = int(input('Introduce un número:\n'))
	convertido = bin(numero)[2:] # oct() para octal, hex()
	# ...para hexadecimal
	print(convertido)


binario_decimal()