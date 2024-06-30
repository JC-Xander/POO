Alumno = []

with open('Notas.csv') as document:


    document.readline() # Leyendo la linea para no procesarla
    cuentaAnterior = None
    subCadena = []
    for linea in document:
        linea = linea.strip()
        ArrayLinea = linea.split(',')
        if cuentaAnterior == ArrayLinea[0]:
            subCadena.append([ArrayLinea[2], ArrayLinea[3]])
        else:
            if cuentaAnterior != None:
                Alumno.append(subCadena)
            subCadena = []
            cuentaAnterior = ArrayLinea[0]
            subCadena.append(ArrayLinea[0])
            subCadena.append([ArrayLinea[2], ArrayLinea[3]])
            
    if subCadena:
        Alumno.append(subCadena)
            
# Sumatoria del uv * nota
NotasFinales = []
for linea in Alumno:
    suma_uv_x_nota = sum([(int(columna[0]) * int(columna[1])) for columna in linea[1:]])
    sumaUV = 0
    for columna in linea[1:]:
        sumaUV += int(columna[0]) 
    subCadena = []
    subCadena.append(linea[0])
    subCadena.append(suma_uv_x_nota//sumaUV)
    NotasFinales.append(subCadena)
    
print(NotasFinales)

