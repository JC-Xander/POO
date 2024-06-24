def sumar(a,b) -> int:
    """suma dos numeros"""
    return a + b

def restar(a,b) -> int:
    """Resta 2 numeros"""
    return a - b

# Guardando la función en una variable.
f = sumar
print(f(1,2))

def duplicar(funcion, a , b) -> int:
    """Multiplica el resultado de la funcion enviada * 2"""
    return 2 * funcion(a, b)

# Provando las funciones.
print(duplicar(sumar, 2, 2))
print(duplicar(restar, 3, 5))
