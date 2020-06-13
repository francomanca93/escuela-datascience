# Algoritmo de busqueda binaria recursivo con contador

import random

def busqueda_binaria(lista, comienzo, final, objetivo, contador):

    contador += 1
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')

    if comienzo > final:
        return False, contador
    
    medio = (comienzo + final) // 2  # División de enteros

    if lista[medio] == objetivo:
        return True, contador
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, contador)
    else:  # lista[medio] > objetivo:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, contador)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que número quieres encontrar? '))

    # Ordenando la lista
    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    # Que esperaría nuestra lista
    contador = 0
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo, contador)

    print(lista)
    encontrado_bool = encontrado [0]
    print(f'El elemento {objetivo} {"esta" if encontrado_bool else "no esta"} en la lista')
    print(f'El algoritmo conto {encontrado[1]} veces')
