#  Escribe un programa que solicite un nombre de archivo y después lea ese archivo buscando las líneas que tengan la siguiente forma:

# X-DSPAM-Confidence: 0.8475
# **Cuando encuentres una línea que comience con “X-DSPAM-Confidence:” ponla aparte para extraer el número decimal de la línea. Cuenta esas líneas y después calcula el total acumulado de los valores de “spam-confidence”. Cuando llegues al final del archivo, imprime el valor medio de “spam confidence”.

# Ingresa un nombre de archivo: mbox.txt
# Promedio spam confidence: 0.894128046745

# Ingresa un nombre de archivo: mbox-short.txt
# Promedio spam confidence: 0.750718518519
# Prueba tu programa con los archivos mbox.txt y mbox-short.txt.

def promedio_X_DSPAM_Confidence(archive:str) -> float:
    with open(archive) as file:
        acumulador = 0
        repeticiones = 0
        for line in file:
            if line.startswith('X-DSPAM-Confidence:'):
                str_decimal = line.strip().split(' ')[-1]
                if str_decimal.isdecimal:
                    acumulador += float(str_decimal)
                    repeticiones += 1
                else:
                    print('Error al obtener el numero', repr(str_decimal))
                    exit()

    return acumulador/repeticiones

print('Archivo - mbox.txt')
print(f'Promedio spam confidence: {promedio_X_DSPAM_Confidence("mbox.txt")}')
print()
print('Archivo - mbox-short.txt')
print(f'Promedio spam confidence: {promedio_X_DSPAM_Confidence("mbox-short.txt")}')
