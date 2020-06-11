import time
# Importo el modulo sys y aumento el limite de recursión, ya que viene predefinido con 1000
import sys
sys.setrecursionlimit(1000000)  # 1 000 000


def factorial_iterativo(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    
    return respuesta

def factorial_recursivo(n):
    if n == 1:
        return 1
    
    return n * factorial_iterativo(n - 1)


if __name__ == '__main__':
    n = 10000000

    print('Complejidad temporal de un algoritmo ITERATIVO. Factorial')
    comienzo = time.time()
    factorial_iterativo(n)
    final = time.time()
    tiempo_iterativo = final - comienzo 
    print(tiempo_iterativo)

    print('--------------------')

    print('Complejidad temporal de un algoritmo RECURSIVO. Factorial')
    comienzo = time.time()
    factorial_recursivo(n)
    final = time.time()
    tiempo_recursivo = final - comienzo
    print(tiempo_recursivo)

    print('-------------------')
    diferencia = abs(tiempo_iterativo - tiempo_recursivo)
    print(f'La diferencia de tiempo entre un algoritmo y otro es {diferencia}')

