valores = []
while True:
    value = input('Ingrese un numero: ')
    if value.lower() == 'hecho':
        break

    if value.isdecimal:
        valores.append(float(value))
    elif value.isalnum:
        valores.append(int(value))
    else:
        print('Para salir ingrese la palabra hecho')

print('Máximo:', max(valores))
print('Minino:', min(valores))