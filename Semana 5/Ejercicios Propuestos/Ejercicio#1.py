"""
Escribe un programa en Python que lea un archivo de texto llamado texto.txt y cuente
la frecuencia de cada palabra en el archivo. El resultado debe ser almacenado en un
diccionario donde las claves sean las palabras y los valores sean el número de veces
que cada palabra aparece. Ignora las diferencias entre mayúsculas y minúsculas
(por ejemplo, "Hola" y "hola" deben contarse como la misma palabra).
Al finalizar, imprime el diccionario. Omita los símbolos de puntuación.
"""

frecuencia_dic = {}

with open('texto.txt') as file:
    for palabra in file.read().split():
        palabra = palabra.capitalize()
        try:
            frecuencia_dic[palabra] += 1
        except:
            frecuencia_dic[palabra] = 1

for key, value in frecuencia_dic.items():
    print(key, '->', value)



# ===== Prueba =====
# frecuencia_dic['K'] += 1
# try:
#     frecuencia_dic['H'] += 1
# except KeyError:
#     frecuencia_dic['H'] = 1

# frecuencia_dic['H'] += 1

# print(frecuencia_dic)
