# Algunas veces cuando los programadores se aburren o quieren divertirse un poco, agregan un inofensivo Huevo de Pascua a su programa. Modifica el programa que pregunta al usuario por el nombre de archivo para que imprima un mensaje divertido cuando el usuario escriba “na na boo boo” como nombre de archivo. El programa debería funcionar normalmente para cualquier archivo que exista o no exista. Aquí está un ejemplo de la ejecución del programa:

# python huevo.py
# Ingresa un nombre de archivo: mbox.txt
# Hay 1797 líneas subject en mbox.txt

# python huevo.py
# Ingresa un nombre de archivo: inexistente.tyxt
# El archivo no puede ser abierto: inexistente.tyxt

# python huevo.py
# Ingresa un nombre de archivo: na na boo boo
# NA NA BOO BOO PARA TI - Te he atrapado!

def mensaje():
    print('=' * 50)
    print('NA NA BOO BOO PARA TI - Te he atrapado!'.center(50))
    print('=' * 50)

name_file = input('Ingrese el nombre del archivo: ')
try:
    with open(name_file) as file:
        print(f'El archivo fue abierto: {name_file}')

except FileNotFoundError:
    if name_file.upper() == 'NA NA BOO BOO':
        mensaje()
    else:
        print(f'El archivo no puede ser abierto: {name_file}')
