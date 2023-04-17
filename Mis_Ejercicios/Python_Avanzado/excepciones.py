# 17/04/2023
from collections import defaultdict

def valor_defecto():
    return "Ese elemento no existe en el diccionario."

usuario = defaultdict(valor_defecto)

usuario["ID"] = 1
usuario["Nombre"] = "Enrique"
usuario["Apellidos"] = "Barros Fernández"
usuario["Edad"] = 28

print(usuario["ID"])
print(usuario["Nombre"])
print(usuario["Apellidos"])
print(usuario["Edad"])

# Si llamamos a un elemento que no existe, saltará
# un error... Por eso importamos defaultdict y añadimos
# la función.
print(usuario["Dirección"])
print(type(usuario))
