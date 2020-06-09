# assert <expresion booleana>, <mensaje de error>

def primera_letra(lista_de_palabras):
    primeras_letras = []

    try:
        for palabra in lista_de_palabras:
            print(palabra)
            assert type(palabra) == str, f'{palabra} no es str'
            assert len(palabra) > 0, 'No se permiten str vacios'
            primeras_letras.append(palabra[0])

        return primeras_letras
    except AssertionError:
        return None

paises = ['Colombia', '', 'Chile', 4]
print(primera_letra(paises))
