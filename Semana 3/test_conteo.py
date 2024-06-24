def conter_letras(cadena:str):
    cadena = cadena.lower()
    vocales = 0
    consonantes = 0
    for letra in cadena:
        if letra != ' ':
            if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
                vocales += 1
            elif letra == 'á' or letra == 'é' or letra == 'í' or letra == 'ó' or letra == 'ú':
                vocales += 1
            else:
                consonantes += 1
                
                
    print(f'Vocales: {vocales}')
    print(f'Consonantes: {consonantes}')

print(ord('a'))
print(ord('e'))
print(ord('i'))
print(ord('o'))
print(ord('u'))
print(ord('á'))
print(ord('é'))
print(ord('í'))
print(ord('ó'))
print(ord('ú'))


conter_letras('holá')

conter_letras('Esta es una frase mas larga')