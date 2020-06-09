def busca_pais_en_diccionario(paises, pais):
    """
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.
    """
    
    try:
        return paises[pais]
    except KeyError:
        return None

def imprime_datos(pais, cantidad):
    if cantidad:
        print(f'La cantidad de infectados es {cantidad}')
    else:
        print(f'No se tiene información para {pais}')


# Las cantidades son ejemplos unicamente.
paises_infectados_covid19 = {
    'Argentina': 15654,
    'Brazil': 67895,
    'Mexico': 113654
}

pais = 'Argentina'
cantidad = busca_pais_en_diccionario(paises_infectados_covid19, pais)
imprime_datos(pais, cantidad)

pais2 = 'Chile'
cantidad2 = busca_pais_en_diccionario(paises_infectados_covid19, pais2)
imprime_datos(pais2, cantidad2)
