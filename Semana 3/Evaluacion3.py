variable = input('Ingrese una cadena: ')

def conteo(cadena:str):
    if len(cadena) != 0:
        if len(cadena) == 1:
            return cadena
        else:
            contador = 1
            caracter = cadena[0]
            for current in cadena[1:]:
                if caracter == current:
                    contador += 1
                else:
                    break
            
            if contador > 1:
                return f'{contador}{conteo(cadena[contador:])}'
            else:
                return f'{caracter}{conteo(cadena[contador:])}'

NewCadena = conteo(variable)
print(NewCadena)

