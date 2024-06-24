# Reescribe el programa del cálculo del salario para darle al empleado 1.5 veces
# la tarifa horaria para todas las horas trabajadas que excedan de 40.

import math

horas = float(input('Ingrese el numero de horas trabajadas\n>>'))
tarifa = float(input('Ingrese la tarifa por hota\n>>'))
total = 0
if horas > 40:
    total = 40 * tarifa;
    horas -= 40
    total += horas * (tarifa * 1.5)
else:
    total = horas * tarifa

print(f'Salario: {total}')