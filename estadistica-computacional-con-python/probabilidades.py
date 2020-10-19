import random

def tirar_dado(numero_de_tiros):
    """Función que simular hacer tirado un dado.
    
    Parametros
        - secuencia_de_tiro: es una lista que guarda una secuencia de tiros. Es devuelta
    Buble: Se repite tantas veces como numero de tiros quiera realizar. El tiro lo guardo en la lista
    """
    secuencia_de_tiro = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiro.append(tiro)    

    return secuencia_de_tiro

def main(numero_de_tiros, numero_de_intentos):
    """Método que simula todo el contexto para jugar con dados

    Parametros:
        - tiros: Es una lista que almacena listas de secuencia_de_tiro.
        - probabilidad_tiros_con_1: Cual es la probabilidad de que salga un 1 en los intentos que yo haga.
    
    Bucle 1: Cuanto correrá la simulación. 
        - Para cada intento en un numero de intentos.
        - Tiros los dados. Guardo los valores de cada tiro en secuencia de cuantos tiros se hizo.
        - Las cantidad de secuencias de tiros se guardan en en una lista.

    Bucle 2: Cuantos tiros con 1 hay?. Analizo caso particular de la simulación del bucle 1. 
        - Para cada tiro en tiros = Voy tomando cada lista de la lista mayor y lo analizo.
        - Si el 1 se encuentra en la lista tiro.
        - Agregamos un valor a la cantidad de tiros con 1 que hubieron en la secuencia.
    
    """
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiro = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiro)
        # print(f'Tiros: {tiros}, Secuencia de tiro: {secuencia_de_tiro}')

    tiros_con_1 = 0
    for tiro in tiros:
        if 1 in tiro:
            tiros_con_1 += 1
            # print(f'Tiro: {tiro}, TIROS:{tiros}, Tiros con 1: {tiros_con_1}')
    
    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    print(f'Propiedad de obtener un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}')


if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantos tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulación: '))

    main(numero_de_tiros, numero_de_intentos)