frase = 'Hola como estas hoy'

diccionario = {}
for letra in frase.replace(' ', ''):
    if diccionario.get(letra) == None:
        diccionario[letra] = 1
    else:
        diccionario[letra] += 1

print(diccionario)

cont = None
key = None
for a, b in diccionario.items():
    if cont == None or cont < b:
        cont = b
        key = a

print(f"{key} : {cont}")
