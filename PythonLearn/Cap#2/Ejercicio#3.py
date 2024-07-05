# Escribe un program para pedirle al usuario el numero de horas
# Y la tarifa por hora para calcular el salario bruto.

try:
    horas = float(input('Ingrese el numero de horas trabajadas\n>>'))
    tarifa = float(input('Ingrese la tarifa por hota\n>>'))
except ValueError:
    print('Dato enviado no valido')
else:
    print(f'Salario: {horas*tarifa}')