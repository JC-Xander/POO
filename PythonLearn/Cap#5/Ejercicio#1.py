# Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. 
# Una vez se haya introducido “fin”, muestra por pantalla el total, la cantidad de números 
# y la media de esos números. Si el usuario introduce cualquier otra cosa que no sea un número, 
# detecta su fallo usando try y except, muestra un mensaje de error y pasa al número siguiente.

contTotal = 0;
contNum = 0;

while True:
    dataInput = input('Introduzca un número: ')
    if (dataInput.lower()) == 'fin':
        break   
    else:
        try:
            castingInt = int(dataInput)
            contTotal += castingInt
            contNum += 1
        except ValueError:
            print('Entrada inválida')

if(contNum == 0):
    print('No se ingresaron numeros')
else:
    print(f'{contTotal} | {contNum} | {contTotal/contNum}')

