
def morral(tamaño_morral, pesos, valores, n):
    if n == 0 or tamaño_morral == 0:
        return 0
    if pesos[n - 1] > tamaño_morral:
        return morral(tamaño_morral, pesos, valores, n - 1)

    return max(valores[n - 1] + morral(tamaño_morral - pesos[n - 1], pesos, valores, n - 1), 
                morral(tamaño_morral, pesos, valores, n - 1))
    
    
if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamaño_morral = 50
    n = len(valores)

    resultado = morral(tamaño_morral, pesos, valores, n)
    print(resultado)