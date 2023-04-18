# 18/04/2023
from operator import itemgetter

usuarios = [{'id': 1, 'Nombre': "Enrique", 'Edad': 28},
            {'id': 2, 'Nombre': "Juana", 'Edad': 30},
            {'id': 3, 'Nombre': "Pedro", 'Edad': 22},
            {'id': 4, 'Nombre': "María", 'Edad': 25}]
"""ordena_id=itemgetter('id')
ordena_nombre=itemgetter('Nombre')
ordena_edad=itemgetter('Edad')
usuarios.sort(key=ordena_edad)
usuarios.reverse()"""

usuarios=sorted(usuarios, key=lambda x: x['Edad'])
usuarios.reverse()
# Este bucle deja el print más bonito
for x in usuarios:
    print(x)
