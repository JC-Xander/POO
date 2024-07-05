# Reescribe el programa de calificaciones del capítulo anterior usando una funcion llamada
# calculadora_calificacion, que reciba una puntuación como parámetro y devuelva una
# calificación como cadena.

def calculadora_calificación(puntuacion:float) -> str:
    try:
        valor = float(puntuacion)
        if valor < 0 or valor > 1:
            return 'Puntuación incorrecta'
        elif valor >= 0.9:
            return 'Sobresaliente'
        elif valor >= 0.8:
            return 'Notable'
        elif valor >= 0.7:
            return 'Bien'
        elif valor >= 0.6:
            return 'Suficiente'
        else:
            return 'Insuficiente'
    except ValueError:
        return 'Puntuación Incorrecta'


puntuacion = input('Ingrese la puntuación\n>>')
print(calculadora_calificación(puntuacion))