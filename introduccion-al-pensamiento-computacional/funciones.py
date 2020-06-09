# Pequeño y rapido programa uniendo todos los algoritmos basicos con bugs
def enumeracion(objetivo):
    """
    ¿Que hace?
    ¿Que significan los parámetros?
    ¿Que devuelve?
    """
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        return respuesta

def aproximacion(objetivo, epsilon=0.01):
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        pass
    else:
        return respuesta

def busquedaBinaria(objetivo, epsilon = 0.01):
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    return respuesta
def menu():
    print('Calculo de raiz cuadrada')
    objetivo = int(input('Escoge un entero: '))
    print('¿Con que tipo de algoritmo quieren calcular la raiz cuadrada?')
    print('1. Enumeracion exhaustiva')
    print('2. Aproximacion de solución')
    print('3. Busqueda binaria')
    metodo = int(input('Escoge un numero: '))

    if metodo == 1:
        respuesta = enumeracion(objetivo)
    elif metodo == 2:
        respuesta = aproximacion(objetivo)
    elif metodo == 3:
        respuesta = busquedaBinaria(objetivo)
    else:
        print('No has seleccionado una opcion correcta')
    
    print(f'La respuesta para el tipo de algoritmo que elegiste es {respuesta}')

menu()