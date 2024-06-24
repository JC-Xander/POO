#indicar un tipo de variable no restingre a la función
def sumar(a: int, b: int = 0) -> int:
    """Puede sumar de 1 2 o hasta 3 numero"""
    print(a + b)
  
# Probando la función  
sumar(1)
sumar(1, 2)
