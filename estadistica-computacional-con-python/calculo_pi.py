import random
import math
from estadisticas import desviacion_estandar, media

def arrojar_agujas(numero_de_agujas):
    '''Función que sirve para arrojar agujas.

    - El bucle calcula cada distancia de las agujas que se arrojan representadas por puntos.
    - Si la distancia del centro es menor a 1, la aguja se encuentra dentro del circulo.
    - return int: 4 * (adentro_del_circulo / numero_de_agujas)
    '''

    adentro_del_circulo = 0
    
    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)

        if distancia_desde_el_centro <= 1:
            adentro_del_circulo += 1
    
    return 4 * (adentro_del_circulo / numero_de_agujas)

def estimacion(numero_de_agujas, numero_de_intentos):
    '''Función que sirve para estimar la media y la desviacion estandar de los numeros de intentos.

    - El bucle sirve para agregar cada estimación de pi.
    - return tupla: (media_estimados, sigma)
    '''
    estimados = []

    for _ in range(numero_de_intentos):
        estimacion_de_py = arrojar_agujas(numero_de_agujas)
        estimados.append(estimacion_de_py)
    
    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Media de estimados = {round(media_estimados, 5)}, Desviación estandar = {round(sigma, 5)}, Agujas = {numero_de_agujas}')

    return (media_estimados, sigma)

def estimar_pi(precision, numero_de_intentos):
    '''Función que me permite estimar el numero pi'''

    numero_de_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        media, sigma = estimacion(numero_de_agujas, numero_de_intentos)
        numero_de_agujas *= 2 
    
    return media

if __name__ == "__main__":
    estimar_pi(0.01, 1000)
