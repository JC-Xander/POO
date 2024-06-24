s = 'Hola Mundo'

for letra in s:
    print(letra, end='-')
    
    
print()
print(s[0], type(s[0]))
print('Tamaño', len(s))

# s[0] = 'x' TypeError ya que el str es inmutable