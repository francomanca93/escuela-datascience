def fibonacci(n):
    """Calcula el numero de fibonacci de n, 
    donde n es la posicion del numero obtenido en la sucesion de fibonacci. 
    La sucesion empieza con 0.

    n int > 0
    return fibonacci(n - 1) + fibonacci(n - 2)
    """
    print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Escribe un entero: '))

print(fibonacci(n))