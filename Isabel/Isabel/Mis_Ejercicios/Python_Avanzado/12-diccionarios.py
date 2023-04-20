#  18/04/2023
a = {'Nombre': 'Javier'}
b = {**a}
# Copio un diccionario dentro de otro
print(b)

a = {'Nombre': 'Javier'}
b = {'Color': 'Rojo'}
c = {**a, **b}
# Fusiono diccionarios. Si se repite, se omite.
print(c)

a = dict(Nombre='Marga', Edad=11)
# También podemos utilizar dict() para decir que es
# un diccionario
print(type(a), a)

d={'Nombre': 'Enrique', 'Apellido': 'Barros'}
d['Edad'] = '28'
# Añadir elementos a un diccionario
print(d)

a = {'Nombre': 'Enrique', 'Apellido': 'Barros'}
# Recorriendo diccionarios
for x in a:
    print(x, 'recorriendo :', a[x])

a = {'Nombre': 'Enrique', 'Apellido': 'Barros'}
# Accediendo a valores del diccionario
print(a['Nombre'])