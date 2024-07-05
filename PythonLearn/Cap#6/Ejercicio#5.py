# Prueba

dato = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

inicio = dato.find('@')
final = dato.find(' ', inicio)

print(dato[inicio + 1:final])


