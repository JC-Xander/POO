# Función para simular un lanzamiento de dado
import random

def lanzar_dado() -> int:
    """Simula el lanzamiento de un dado 1 a 6"""
    return random.randint(1,6)

for _ in range(10):
    print(lanzar_dado())


