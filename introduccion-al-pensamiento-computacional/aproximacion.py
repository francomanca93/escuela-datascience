objetivo = int(input('Escoge un numero: '))
epsilon = 0.01  # Que tan preciso queremos ser
paso = epsilon**2
respuesta = 0.0
iteraciones = 0

while abs(respuesta**2 - objetivo) >= epsilon: # and respuesta <= objetivo:
    #print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso
    iteraciones +=1

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada del {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es la {respuesta}')

print(f'El numero de iteraciones fue {iteraciones}')