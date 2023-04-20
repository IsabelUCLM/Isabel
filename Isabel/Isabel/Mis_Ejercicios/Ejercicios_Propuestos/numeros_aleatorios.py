import random, time

# Lista ordenada de menor a mayor.
for i in range(20):
    random.seed(5)
    lista = print(random.randint(0,100), end=", ") 


"""# Lista ordenada de mayor a menor sin repetir.
aleatorios = random.sample(range(0,100),20)
print(sorted(aleatorios, reverse=True)) """

# Lista de floats truncados con random y separados por coma.
inicio = time.time()
for i in range(20):
    random.seed(5)
    r = print(round(random.random()*100, 2), end=", ")
final = time.time()
print("\nEl primer for tarda: ", final-inicio)

# Lista ordenada de menor a mayor con paso de 5.
inicio = time.time()
paso = [random.randrange(0,100,5) for i in range(20)]
print(sorted(paso)) 
final = time.time()
print("\nEl segundo for tarda: ", final-inicio)

