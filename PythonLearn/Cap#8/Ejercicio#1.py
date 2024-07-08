# Escribe una función llamada recortar que toma una lista y la modifica, removiendo el primer y último elemento, y regresa None. 
# Después escribe una función llamada medio que toma una lista y regresa una nueva lista que contiene todo excepto 
# el primero y último elementos.

def recortar(lista:list):
    del lista[0]
    del lista[-1]


def medio(lista:list):
    return lista[1:len(lista) - 1]

lista = [1, 2, 3, 4, 5]
recortar(lista)
print(lista)


lista = [1, 2, 3, 4, 5]
new_list = medio(lista)

print('Lista original:', lista)
print('Lista nueva:', new_list)

lista = [1, 2, 3, 5, 4]
new_lista = sorted(lista)

print(lista)
print(new_lista)