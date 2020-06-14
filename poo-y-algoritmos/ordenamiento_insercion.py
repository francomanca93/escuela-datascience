# Algoritmo de ordenamiento por insercion

import random

def ordenamiento_insercion(lista):
    
    for i in range(len(lista)):
        # print(lista[i])
        for j in range(i, 0, -1):
            # print(lista[j - 1], lista[j])
            if lista[j - 1] > lista[j]:
                aux = lista[j]
                lista[j] = lista[j - 1]
                lista[j - 1] = aux
        # print(lista)
    
    return lista


def ordenamiento_insercion_PLATZI(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista

if __name__ == '__main__':
    # tamano_de_lista = int(input('De que tamaño sera la lista? '))
    print("Version mia")
    # lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    lista = [6, 5, 3, 1, 8, 7, 2, 4]
    print(lista)
    
    lista_ordenada = ordenamiento_insercion(lista)

    print(lista_ordenada)

    print("------------------------------")

    print("Version Platzi")

    print(lista)
    
    lista_ordenada = ordenamiento_insercion_PLATZI(lista)

    print(lista_ordenada)
