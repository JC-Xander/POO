diccionario = {'ERROR':0, 'WARNING':0}
with open('server.log') as file:
    for line in file:
        separar = line.split(':')
        
        if len(separar) > 0:
            key = separar[0].upper()
            if key in diccionario:
                diccionario[key] += 1
                
with open('reporte_errores.txt', mode='w') as file:
    for a, n in diccionario.items():
        file.write(f"{a} : {n}\n")
