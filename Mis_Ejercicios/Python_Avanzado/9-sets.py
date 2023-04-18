# 18/04/2023
a = {'a', 'b'}

print('a' in a) # True

a = {1, 2}

print(3 not in a) # True

a = {1, 2}

a.remove(1)

print(a)

a = {1, 2}

a.discard(1)

print(a)
"""
Hay una diferencia  entre remove() y discard():
Si eliminamos un elemento del set con remove(), lo elimina, 
pero si intentamos eliminarlo de nuevo,
va a dar error porqué no encuentra el elemento.
En cambio, esto no ocurre con discard(),que ignora el error.
"""
a = {1, 2}

a.remove(1)
#a.remove(1) descomentar para que de error

print(a)

# discard
a = {1, 2}

a.discard(1)
a.discard(1)

print(a)

a = {1, 2}

a.add(3) # añado un solo elemento
print(a)
a.update({3, 4, 5, 6}) # añado varios elementos
print(a)

set1 = {1, 1, 2, 3, 4, 4}.union({1, 2, 3, 4, 5, 6, 6, 6})
# une elementos y borra los repetidos
print(set1)

set1 = {1, 1, 2, 3, 4, 4}.union({1, 2, 3, 4, 5, 6, 6, 6})
set2 = set1.union({7, 8, 9})

print("Set 1 union:", set1)
print("Set 2 union:", set2)

set1 = {1, 1, 2, 3, 4, 4}.union({1, 2, 3, 4, 5, 6, 6, 6})
set2 = set1|({7, 8, 9})
# la barra es lo mismo que poner .union

set1 = {1, 1, 2, 3, 4, 4}.intersection({1, 2, 3, 4, 5, 6, 6, 6})
set2 = set1.intersection({7, 8, 9})
# INTERSECTION solo saca los comunes a AMBOS
print("Set 1 intersection:", set1)
print("Set 2 intersection:", set2)

set1 = {1, 1, 2, 3, 4, 4}&({1, 2, 3, 4, 5, 6, 6, 6})
set2 = set1.intersection({7, 8, 9})
# Forma abreviada de INTERSECTION
print("Set 1 &:", set1)
print("Set 2 &:", set2)

a = {'a', 'b', 'c', 'd'}
b = {'d', 'e', 'f', 'g'}

print(a & b)

print(b.intersection(a))

a = {'a', 'b', 'c', 'd'}
b = {'d', 'e', 'f', 'g'}
# Obtenemos los valores diferentes
print(a.difference(b))

print(b.difference(a))

a = {'a', 'b', 'c', 'd'}
b = {'d', 'e', 'f', 'g'}
# igual que difference
print(a - b)
print(b - a)

a = {'a', 'b', 'c', 'd'}
b = {'d', 'e', 'f', 'g'}

print(a.symmetric_difference(b))
print(b - a)

a = {'a', 'b', 'c', 'd'}
b = {'d', 'e', 'f', 'g'}
# Si no están todos en b devuelve FALSE
print(a.issuperset(b))
print(b >= a)

x = {"manzana", "plátano", "fresa"}
y = {"iphone", "samsung", "xiaomi"}

z = x.difference(y)

print(z)
# {'samsung', 'manzana', 'plátano', 'fresa', 'iphone', 'xiaomi'}
# {'plátano', 'fresa', 'manzana'}
"""
Symmetric_difference:
Devuelve todos los valores no repetidos tanto del uno como
del otro.
difference: devuelve valores no repetidos de Y respecto
a X.
"""
a = {'a', 'b', 'c', 'd'}
b = {'d', 'e', 'f', 'g','a', 'b', 'c'}
print(a.issuperset(b))
print(b >= a)

a = {'a', 'b', 'c', 'd'}
b = {'d', 'e', 'f', 'g','a', 'b', 'c'}
# Si los valores de A están en B, es true
print(a.issubset(b))
print(b <= a)

a = {'a', 'b'}
b = {'d', 'e'}
# isdisjoint devuelve True, si los valores de un set no están
# en el otro, si uno solo de ellos está, devuelve False.
print(a.isdisjoint(b))
