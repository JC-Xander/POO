# retornar -> return
# imprimir -> print
def subrayar(s: str):
    """Subrayar un texto"""
    print(s)
    print("-" * len(s))
    
subrayar('Hola Mundo')

texto = "MAMÁ"

print('Minuscula: ', texto.lower())
print('Apariciones', texto.count('h'))
print('Capitalizable: ', texto.capitalize())
print('Reemplazar', texto.replace('hola','adios'))

print(texto.startswith('m'))

print(texto.index('z'))
