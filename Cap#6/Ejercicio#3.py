palabra = 'banana'

def contador(palabra:str, caracter:str): 
    contador = 0
    for letra in palabra:
        if letra == caracter:
            contador += 1
    
    print(contador)


contador(palabra, 'a')