try:
    numIngresado = input('Ingrese un numero positivo\n>>')
    
    cont = 0
    for values in numIngresado:
        cont += int(values)
        
    print(f'La suma de los digitos es: {cont}')   
except:
    print('No se ingreso un numero')
    
    