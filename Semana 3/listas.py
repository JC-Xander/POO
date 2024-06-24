# Inicializar listas
# Crea una lista vacia
Lista = []
lista = list()
Lista = [1,2,3,4,5,'hola',True, [1,2,3]] # Permite añadir cualquier tipo de dato a una lista y esta es flexible su tamaño puede aumentar y disminuir

# Mostrar un dato de la lista
print(Lista[0]) # -> 1
print(Lista[7]) # -> [1, 2, 3]
print(Lista[6]) # -> True

#imprimiendo toda la lista
for elemento in lista:
    print(elemento)
    
# Tamaño de la lista
print('Cuanto eslementos hay en la lista ',len(lista))

#buscando un elemento en la lista
lista2 = ['hola', 'adios', 'objetos', 'programacion']
entrada = input('Buscar el elemento: ')
if entrada in lista2:
    print(f'Palabra encontrada {entrada}')
else:
    print(f'No se encontro la palabra {entrada}')
    
# recorre la lista de atras hacia adelante

lista3 = [10, 20, 30, 40]

print(lista3[-1]) # -> 40 
print(lista3[-2]) # -> 30
print(lista3[-3]) # -> 20

#insertar al final de la lista
lista3.append(50)

#Inserta en x posicion
# Primer parametro es la posicion u el segundo es el elemento a añadir
lista3.insert(1, 15) # -> [10, 15, 20, 30, 40]

#Eliminar
lista3.pop() #Elimina el ultimo elemento
lista3.pop(0) #Elimina el elemento en la posicion enviada
del lista3[1] #Elimina el elemento en la posicion 1
lista3.remove(0) # remueve el valor en la posicion enviada

ListaSTR = list('Hola') # Divide la cadena en sus caracteres y los retorna por lista.
t = 'Hola Mundo'
print(t.split(' ')) # Divide la cadena en donde se encuentre el caracter enviado y retorna la sub cadenas creadas como una lista

print(" ".join(lista2)) # Crea una cadena que contendra todos los elemento de la lista separados por el elemento que este entre' ', Solo funciona con cadenas

print(lista3)

# Si modifico una lista cambiaran todas las variables que apunten a ella
# Funciones
# copy() Crea una copia profunda de la lista
# sort() ordena los elemento pero solo si todos son del mismo tipo sino retorna un error
# ls.reverse() invierte los elemento de la cadena
