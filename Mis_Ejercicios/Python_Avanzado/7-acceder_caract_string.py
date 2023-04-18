# 17/04/2023
texto = "facilito"
print(texto[0])
print(texto[0:3])

colores = {'rojo', 'azul', 'rojo', 'verde', 'amarillo', 'azul'}
print(colores)

colores.add("Naranja")

print(colores)

# frozenset hará que no podamos añadir más campos
colores = frozenset({'rojo', 'azul', 'rojo', 'verde', 'amarillo', 'azul'})
print(colores)

colores = ['rojo', 'azul', 'verde', 'amarillo']
print(colores * 2) # Multiplico X2 los datos

# También se puede hacer llamado a elementos de la lista
print(colores[2] * 5, " que te quiero ", colores[2] * 5)



