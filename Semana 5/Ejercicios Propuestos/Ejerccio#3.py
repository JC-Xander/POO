# Crea un programa en Python que lea un archivo de texto llamado libro.txt y busque l
# a frecuencia de una palabra específica ingresada por el usuario. El programa debe 
# imprimir cuántas veces aparece la palabra en el archivo.

buscar = input('Ingrese la palabra que desea buscar\n>> ').lower().strip()


with open('libro.txt') as file:
    cont = 0
    for line in file:
        palabras = line.lower().split()

        for palabra in palabras:
            if palabra.rstrip(',.;:') == buscar:
                cont += 1


print(buscar.capitalize(), cont)
