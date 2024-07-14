diccionario = {}
with open('ventas.csv') as file:
    for line in file:
        separar = line.split(',')
        try:
            key = separar[0][0:7]
            costo = int(separar[-1])
            if len(key) > 0:
                try:
                    diccionario[key] += costo
                except KeyError:
                    diccionario[key] = costo
        except ValueError or IndexError:
            print('Se encontro una linea mal formateada')
        
        
with open('ventas_totales.txt', mode='w') as file:
    for mes, total in diccionario.items():
        file.write(f"Total del mes {mes} : {total}\n")
    