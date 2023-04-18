# 18/04/2023
import re
""" LECTURA DE ARCHIVOS
try:

    with open('C:/Users/usuario/Desktop/Tutorial Python/Practicando_Ficheros/fichero_1.txt', 'r', encoding="utf-8") as texto:
        # encoding es para que no de errores en acentos, por ejemplo
        lectura = texto.readlines()

    print(lectura)


except FileNotFoundError:
    print("No se encontró el archivo.")

try:
    contador = 0
    palabra = input("Ingresa palabra a buscar:\n")
    with open("C:/Users/usuario/Desktop/Tutorial Python/Practicando_Ficheros/fichero_1.txt", encoding='utf-8') as data:
        lineas = data.readlines()
        for linea in lineas:
            if linea.find(palabra) == -1:
                pass
            else:
                contador += 1
        if contador >= 1:
            print(f"La palabra {palabra} ha sido encontrada")
        else:
            print(f"La palabra {palabra} NO ha sido encontrada")
            
except FileNotFoundError:               
    print("Archivo no Existe")
    """
""" ESCRITURA DE ARCHIVOS 
with open("C:/Users/usuario/Desktop/Tutorial Python/Practicando_Ficheros/fichero_2.txt", "w", encoding="utf-8") as texto:
    texto.write("Esta es mi primera línea\n")
    texto.write("Esta es la segunda línea\n")
    texto.write("Esta es la tercera línea\n")
# Para que no se borre lo anterior, en vez de W, utilizar A.
with open("C:/Users/usuario/Desktop/Tutorial Python/Practicando_Ficheros/fichero_2.txt", "a", encoding="utf-8") as texto:
    texto.write("\n")
    texto.write("Esta es la cuarta línea\n")
    texto.write("Esta es la quinta línea\n")"""

# r+ -> Permite escribir y leer al mismo tiempo. Da error si no existe.
with open("C:/Users/usuario/Desktop/Tutorial Python/Practicando_Ficheros/fichero_2.txt", "r+", encoding="utf-8") as texto:
    for linea in texto:
        print(linea)
        texto.write("\n Otra línea")
        print("Añadido.")

# w+ -> Este además hace lo anterior y crea el archivo si no existe.
with open("C:/Users/usuario/Desktop/Tutorial Python/Practicando_Ficheros/fichero_2.txt", "r+", encoding="utf-8") as texto:
    for linea in texto:
        print(linea)
        texto.write("\n Otra línea")
        print("Añadido.")





