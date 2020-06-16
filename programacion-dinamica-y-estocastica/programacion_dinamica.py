import sys 

# Algoritmo de fibonacci aplicando unicamente recursión
def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Algoritmo de fibonacci aplicando recursión y memorización
def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    
    # Aplico memorización
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado
    
    return resultado


if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un numero: '))
    resultado = fibonacci_dinamico(n)

    print(resultado)