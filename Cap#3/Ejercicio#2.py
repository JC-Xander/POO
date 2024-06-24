# Reescribe el programa de salario usando ´try´ y ´except´, de modo que el programa sea capaz
# de gestionar entradas no numéricas con elegancia, mostrando un mensaje y saliendo del programa.

try:
    horas = float(input('Ingrese el numero de horas trabajadas\n>>'))
    tarifa = float(input('Ingrese la tarifa por hota\n>>'))
    total = 0
    if horas > 40:
        total = 40 * tarifa;
        horas -= 40
        total += horas * (tarifa * 1.5)
    else:
        total = horas * tarifa
except ValueError:
    print('Dato enviado no valido')
else:
    print(f'Salario: {total}')