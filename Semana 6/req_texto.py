from urllib.request import urlopen

recurso = urlopen('http://data.pr4e.org/romeo.txt')
for linea in recurso:
    print(linea.decode().strip())

# Conseguir una imagen con urllib.request y el metodo urlopen
imag = urlopen('http://')
