# Escribe un programa que solicite una puntuación entre 0.0 y 1.0.
# Si la puntuacion esta fuera del rango, muestra un mensaje de error
# Si la puntuacion esta en el rango muestra la calificación siguienta esta tabla:
# | Puntuación | Calificación 
# | >= 0.9     | Sobresaliente
# | >= 0.8     | Notable
# | >= 0.7     | Bien
# | >= 0.6     | Suficiente
# | < 0.6      | Insuficiente

valorIngresado = input('Ingrese la puntuación\n>>')
try:
    valor = float(valorIngresado)
    if valor < 0 or valor > 1:
        print('Puntuación incorrecta')
    elif valor >= 0.9:
        print('Sobresaliente')
    elif valor >= 0.8:
        print('Notable')
    elif valor >= 0.7:
        print('Bien')
    elif valor >= 0.6:
        print('Suficiente')
    else:
        print('Insuficiente')
except ValueError:
    print('Puntuación Incorrecta')