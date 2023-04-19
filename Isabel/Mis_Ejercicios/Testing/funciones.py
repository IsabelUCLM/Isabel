def calcula_media(*args):
    return(sum(*args)/len(*args))

print(calcula_media([3, 7, 5]))
# Debe dar 5

print(calcula_media([30, 0]))
# Debe dar 15

assert(calcula_media([3, 7, 5]) == 5.0)
assert(calcula_media([30, 0]) == 15.0)
# Si en assert cambiamos los números 5 y 15, dará AssertionError 
