import random
from Dado import lanzar_dado as lz_dado

def lanzar_dado() -> int:
    """Simula el lanzamiento de un dado de 1 a 20"""
    return random.randint(1,20)

for _ in range(10):
    lz_dado()

