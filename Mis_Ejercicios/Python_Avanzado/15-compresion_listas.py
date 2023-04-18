#18/04/2023
potencias = [x*x for x in (1,2,5,10,50)]
print(potencias)
# Hará 1 x 1 , 2 x 2, 5 x 5... 

potencias2=[]
for x in (1,2,5,10,50):
    x = x * x
    potencias2.append(x)
print(potencias2)
# Em ambos casos es lo mismo pero el primero es más
# eficiente.
rosa = ["fucsia", "salmón", 'chicle', 'coral', 'pastel']
coloresM = [x.upper() for x in rosa]
print(coloresM)

adiosLetras=[x.strip("otra") for x in ["una,", "coma,", "y,", "otra,", "y,", "otra,"]]
print(adiosLetras)

car = [x if x in 'pny' else 'Caracter no encontrado' for x in 'python']
print(car)
# Si existe pny aparece, si no, va al else.


