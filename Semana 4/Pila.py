# Convertir una lista en una pila

def push(p:list, elemento:object) -> bool:
    p.append(elemento)
    return True

def pop(p:list) -> object:
    return p.pop()

def size(p:list) -> int:
    return len(p)

def top(p:list) -> object:
    return p[-1]

p = []

push(p, 10)
push(p, 'Hola Mundo')
push(p, 100)
print('Tamaño: ', size(p))
assert top(p) == 100 
print(p)


