def f(x):

    # Primera operación
    respuesta = 0

    # Segunda operacion. Sin importar de x este loop correrá 1000 veces.
    for i in range(1000):
        respuesta += 1

    # Tercera operación. Este loop correrá el valor de x
    for i in range(x):
        respuesta += x

    # Cuarta operación. Esta parte esta corriendo 2 loop. Esto será 2x² 
    for i in range(x):  
        for j in range(x):
            respuesta += 1
            respuesta += 1

    # Quinta operación.
    return respuesta

if __name__ == '__main__':
    print(f(2))