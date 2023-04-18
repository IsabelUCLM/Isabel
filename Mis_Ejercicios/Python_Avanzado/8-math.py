# 17/04/2023
def operaciones1():
    a, b, c, d, e, f, g = 5, 10, 15, 20, 25, 30, 35
    a = a + 10
    b = b - 10
    c = c * 10
    d = d / 10
    e = e // 10
    f = f % 10
    g = g ** 10
    print(a,b,c,d,e,f,g)

operaciones1()

def operaciones2():
    a, b, c, d, e, f, g = 5, 10, 15, 20, 25, 30, 35
    a += 10
    b -= 10
    c *= 10
    d /= 10
    e //= 10
    f %= 10
    g **= 10
    print(a,b,c,d,e,f,g)

operaciones2()

import operator

a, b = 10, 15

a = operator.iadd(a,b) # suma

print(a)

a, b = 10, 15

print(operator.sub(a, b)) # resta

a, b = 10, 15

print(operator.mul(a, b)) # multiplicación

a, b = 10, 15

print(operator.truediv(a, b)) # división

a, b = 100, 30

c = a/b

print(type(c),c)

c= a//b # forzamos que se quede como int aunque divida y de
# decimal
print(type(c),c)

a, b = 2, 10

print(a ** b) # exponentes

print(operator.mod(10, 3)) # resto de una división

a = cociente, resto = divmod(10, 3)
print(a) # saca tanto el cociente como el resto

a, b = 2, 10
c = pow(a, b)

print(c) # exponentes también

import math

a = 1
b = math.exp(a)
print(b)

a = 5
b = math.exp(a)
print(b) # cálculo de potencias

a = math.sqrt(10)

print(type(a)) # raíz cuadrada

import cmath

a = cmath.sqrt(10)

print(type(a)) # raíz cuadrada truncando decimales
