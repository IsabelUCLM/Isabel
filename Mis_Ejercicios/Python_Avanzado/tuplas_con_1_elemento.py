# 17/04/2023
a = (10, 100, 1000)
a = (10)
print(type(a))
# Si le añades una "," se convierte otra vez en tupla
a = (10,)
print(type(a))
# Sin paréntesis también es una tupla (xD)
a = 10,
print(type(a))
# Aunque los corchetes indiquen una lista, si por fuera
# pones paréntesis, se trata de una tupla.
# (una lista dentro de una tupla)
a = ([10]),
print(type(a))