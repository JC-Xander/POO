"""
Descargar una copia de un archivo www.py4e.com/code3/romeo.txt. Escribir un programa para abrir el archivo romeo.txt y leerlo línea por línea. Para cada línea, dividir la línea en una lista de palabras utilizando la función `split`. Para cada palabra, revisar si la palabra ya se encuentra previamente en la lista. Si la palabra no está en la lista, agregarla a la lista. Cuando el programa termine, ordenar e imprimir las palabras resultantes en orden alfabético.
"""


lista = ['Holaa', 'Hola', 'Holaaaa']


print(lista)

name_file = 'romeo.txt'

with open(name_file) as file:
    contenido = file.read()
    
lista_palabras = contenido.split()       
        
cont = len(lista_palabras) - 1
while cont > 0:
    if lista_palabras.count(lista_palabras[cont]) > 1:
        del lista_palabras[cont]
    
    cont -= 1

lista_palabras.sort()
print('=' * 15)

print(lista_palabras)

print('=' * 15)

lista2 = contenido.split()

for palabra in lista2[:]:
    cont = lista2.count(palabra)
    if cont > 1:
        lista2.remove(palabra)

lista2.sort()
print(lista2)

