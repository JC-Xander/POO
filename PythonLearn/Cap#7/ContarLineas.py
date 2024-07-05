# Cuenta las lineas totales de un archivo de texto

file = open('mbox-short.txt')

cont = 0
for linea in file:
    cont += 1

print('Lineas Totales: ', cont)
