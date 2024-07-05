# Crear un programa que le pida al usuario una temperatura en grados celsius,
# la convierta en grados Fahrenheit en imprima por pantalla la temperatura convertida

gradosCelcius = int(input('Ingrese la temperatura en celcius: '))
gradosFahrenheit = gradosCelcius * (9/5) + 32
print(f'{gradosCelcius}°C = {gradosFahrenheit}°F')