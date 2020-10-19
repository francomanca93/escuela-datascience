import random
import collections


PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

def crear_baraja():
    '''Función que permite crear una baraja'''
    barajas = []
    for palos in PALOS:
        for valor in VALORES:
            barajas.append((palos, valor))
    
    return barajas

def obtener_mano(barajas, tamaño_mano):
    '''Función que permite obtener una mano cualquiera de la baraja.'''
    mano = random.sample(barajas, tamaño_mano)
    return mano

def obtener_valores(mano):
    '''Función que me permite recorrer las cartas de una mano.'''
    valores_mano = []

    for carta in mano:
        valores_mano.append(carta[1])

    return valores_mano

def ordenar_valores(valores_mano):
    '''Función que permite ordenar los valores que tengo en la mano. De menor a mayor
    '''
    mano_ordenada = []

    for VALOR in VALORES:
        for valor in valores_mano:
            if VALOR == valor:
                mano_ordenada.append(valor)
    return mano_ordenada

#### -- Funciones para escalera
def arreglos_escalera(mano_ordenada, tamaño_mano):
    '''Función de la cual obtengo un arreglo de arreglos de los tipos de escaleras que hay en un mazo.
    '''
    arreglos = []
    n_arreglos = len(VALORES) - len(mano_ordenada) + 1

    for i in range(0, n_arreglos):
        arreglos.append(VALORES[i: i + tamaño_mano])

    return arreglos

def es_escalera(arreglos, mano_ordenada):
    '''Función que me permite saber si tengo una escalera o no
    '''
    acum = 0

    for arreglo in arreglos:
        if mano_ordenada == arreglo:
            acum += 1
    
    if acum > 0:
        return True
    else:
        return False

def es_escalera_mismo_palo(arreglos, mano_ordenada, mano):
    '''Función que me permite saber si mi mano, es la cuela tenga escalera es de color o no.
    '''
    palos = []
    hay_color = False

    for carta in mano:
        palos.append(carta[0])
    counter_palos = dict(collections.Counter(palos))

    for palo in counter_palos.values():
        if palo == len(mano):
            hay_color = True

    if hay_color == True:
        acum = 0
        for arreglo in arreglos:
            if mano_ordenada == arreglo:
                acum += 1
        if acum > 0:
            return True
        else:
            return False

#### ---- Funciones para par

def hay_doble(mano):
    '''Función que me permite saber si hay doble o no en una mano'''
    par = 0
    es_doble = False
    
    valores = []
    for carta in mano:
        valores.append(carta[1])

    counter = dict(collections.Counter(valores))
    for val in counter.values():
        if val == 2:
            par += 1
    if par > 0:
        return True
    else:
        return False

#### Probabilidades

def probabilidad_par(tamano_mano, intentos):
    '''Función que me calcula la probabilidad de los pares que me puede tocar en una mano'''
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        mi_mano = hay_doble(mano)
        if mi_mano:
            pares += 1
        else:
            pass

    probabilidad = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad}')


def probabilidad_escalera(tamaño_mano, intentos):
    '''Función que me calcula la probabilidad de las escaleras de una mano. '''

    barajas = crear_baraja()
    cantidad_escaleras = 0
    cantidad_escaleras_mismo_palo = 0
    for _ in range(intentos):
    
        mano = obtener_mano(barajas, tamaño_mano)
        valores_mano = obtener_valores(mano)
        mano_ordenada = ordenar_valores(valores_mano)
        arreglos_posibles = arreglos_escalera(mano_ordenada, tamaño_mano)
        hay_escalera = es_escalera(arreglos_posibles, mano_ordenada)
        
        if hay_escalera == True:
            cantidad_escaleras += 1
        hay_escalera_mismo_palo = es_escalera_mismo_palo(arreglos_posibles, mano_ordenada, mano)

        if hay_escalera_mismo_palo == True:
            cantidad_escaleras_mismo_palo += 1

    
    probabilidad_escalera = cantidad_escaleras / intentos
    print(f'La probabilidad de encontrar una escalera en {intentos} intentos es {probabilidad_escalera}')
    probabilidad_escalera_mismo_palo = cantidad_escaleras_mismo_palo / intentos
    print(f'La probabilidad de encontrar una escalera del mismo palo en {intentos} intentos es {probabilidad_escalera_mismo_palo}')


if __name__ == '__main__':
    tamaño_mano = int(input('¿De cuantas cartas será la mano? (Poker = 5 cartas): '))
    intento = int(input('¿Cuantos intentos para calcular la probabilidad?: '))

    
    probabilidad_par(tamaño_mano, intento)
    probabilidad_escalera(tamaño_mano, intento)
