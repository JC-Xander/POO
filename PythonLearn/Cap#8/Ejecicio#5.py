name_file = 'mbox-short.txt'

print('[... Lineas de Salidas removidas ...]')

line_From = []
with open(name_file) as file:
    for line in file:
        secciones = line.split()
        if secciones and secciones[0] == 'From':
            line_From.append(secciones[1])

print('\n'.join(line_From))
print('Lineas totales:', len(line_From))