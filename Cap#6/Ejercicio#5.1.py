"""
    Toma la siguinete código en python que almacena una cadena:

    str = 'X-DSPAM-Confidence:0.8475'

    Utiliza find y una parte de la cadena para extraer la porción de la cadena después del carácter dos puntos y después utiliza
    la función float para convertir la cadena extraída en un número de punto flotante.
""" 

str = 'X-DSPAM-Confidence:0.8475'

position = str.find(':')

flotante = float(str[(position + 1):])

print("Flotante: ",flotante)