#Reescribe el programa Salario, con tarifa-y-media para las horas extras, y crea una función llamada 'calculo salario'
#que resiba dos paramentros(horas Y tarifa)
import math

def calculo_salario(horas:int, tarifa:float) -> float:
    total = 0
    if horas > 40:
        total = 40 * tarifa;
        horas -= 40
        total += horas * (tarifa * 1.5)
    else:
        total = horas * tarifa

    return total

horas = float(input('Ingrese el numero de horas trabajadas\n>>'))
tarifa = float(input('Ingrese la tarifa por hota\n>>'))

print(f'Salario: {calculo_salario(horas, tarifa)}')