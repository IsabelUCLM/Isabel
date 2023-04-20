# 13/04/2023

"""
Escribir una función que pida un número entero entre 1 y 10
 y guarde en un fichero con el nombre tabla-n.txt 
 la tabla de multiplicar de ese número, 
 done n es el número introducido.
"""
n = int(input('Introduce un número entero entre 1 y 10: '))
nombre = 'tabla-' + str(n) + '.txt'
f = open(nombre, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()
"""
Escribir una función que pida dos números n y m entre 1 y 10,
lea el fichero tabla-n.txt con la tabla de multiplicar
 de ese número, y muestre por pantalla la línea m del fichero
 Si el fichero no existe debe mostrar un mensaje por pantalla
informando de ello.
"""

num1 = int(input('Introduce un número entero entre 1 y 10: '))
num2 = int(input('Introduce otro número entero entre 1 y 10: '))
nombre = 'tabla-' + str(num1) + '.txt'
try: 
    with open(nombre, 'r') as f:
        lineas = f.readlines()
    print(lineas[num2 - 1])
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)