#Creando el manejador de ficheros
file = open('mbox.txt')
file2 = file

# Hace la lectura por linea
"""
for letra in file:
    print(letra, end='')
"""
#La lectura va consumiento el contenido

# print(file.read(6))
    

print(file.readline())
print(file2.readline())

file.close()