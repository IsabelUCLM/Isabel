# 17/04/2023
a = [[10, 100, 1000], ["texto1", "texto2"], [True]]

print(a[0])
print(a[0][0]) # Llamo a las posiciones internas

b = ["texto 3", 1400, True,
      [10, "texto1", 1000], [60, "texto2"], [True]]

print(b[4][0])
print(a[0][-3])
print(b[3][1][2]) # x de texto1

a[0].append("Soy yo")
print(a) # Se añade dentro de las listas anidadas, al final

# Invertir orden de listas con reverse()
b.reverse()
print(b)
a[0].reverse()
print(a)
