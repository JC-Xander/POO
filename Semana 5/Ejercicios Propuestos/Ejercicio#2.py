# Según una evaluación anterior de compresión de cadenas según el número de repeticiones de una letra de forma consecutiva. 
# Usar un archivo entrada.txt que contenga los datos originales y uno denominado compreso.txt donde ya exista la salida con compresión.


def frecuencia_palabras(name_file:str) -> dict:
    frecuencia_dic = {}

    with open(name_file) as file:
        for palabra in file.read().split():
            palabra = palabra.capitalize().rstrip('.,:')
            try:
                frecuencia_dic[palabra] += 1
            except:
                frecuencia_dic[palabra] = 1

    return frecuencia_dic


## init
diccionario = frecuencia_palabras('entrada.txt')

with open('compreso.txt', mode='w') as file:
    cadena = ''
    cont = 1
    for i in range (1, 4):
        if i % 3 == 0:
            file.write(f"{'Palabra'.center(17)}    N°\n")
        else:
            file.write(f"{'Palabra'.center(17)}    N°  |   ")

    for key, value in diccionario.items():
        if cont % 3 == 0:
            cadena += f'{"%2d" % cont}) { key.ljust(15) } -> {value}\n' 
        else:
            cadena += f'{"%2d" % cont}) { key.ljust(15) } -> {value}   |   '
        cont += 1

    file.write(cadena)
