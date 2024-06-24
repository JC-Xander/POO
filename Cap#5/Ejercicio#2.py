# Escribe otro programa que pida una lista de números como la anterior y al final 
# muestre por pantalla el máximo y mínimo de los números, en vez de la media

contTotal = 0
contMax = None
contMin = None

while True:
    dataInput = input('Introduzca un número: ')
    if (dataInput.lower()) == 'fin':
        break   
    else:
        try:
            castingInt = int(dataInput)
            contTotal += castingInt
            if contMin == None or castingInt < contMin:
                contMin = castingInt
            
            if contMax == None or castingInt > contMax:
                contMax = castingInt

        except ValueError:
            print('Entrada inválida')


print(f'Conteo Total: {contTotal}')
print(f'Maximo: {contMax}')
print(f'Minimo: {contMin}')