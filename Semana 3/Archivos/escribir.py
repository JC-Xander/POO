file_write = open('prueba1', mode='w') #Abre o crea un archivo
# Elimina todo lo que contiene y escribe 
# a Se hubica al final y añade lo nuevo.
file_write.write('Programción Orientada a Objetos\n') # Escribe en el archivo
file_write.write('22/06/2024') # Escribe en el archivo
file_write.writelines(
    [
        'Primera Linea\n',
        'Segunda Linea\n',
        'Tercera Linea\n'
    ]
)
