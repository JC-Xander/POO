try:
    data = input('Ingrese un numero positivo\n>>')
    intData = int(data)
    
    bandera = True
    if intData > 0:
        for value in range(2,intData):
            if intData % 2 == 0:
                bandera = False
                break
            
        if bandera:
            print(f'el numero {intData} es primo')
        else:
            print(f'el numero {intData} no es primo')
    else:
        print('El numero ingresado no es mayor que 0')
                
                
except:
    print('No se ingreso un numero')
    
    