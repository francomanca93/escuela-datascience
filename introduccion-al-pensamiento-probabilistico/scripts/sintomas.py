
def calcular_bayes(priori_H, prob_E_dado_H, prob_E):
    '''Teorema de Bayes.
    
    Variables de entrada:
    - priori_H = probabidad de la hipótesis
    - prob_E_dado_H = probabidad de la evidencia dada la hipótesis
    - prob_E = probabilidad de la evidencia

    return (priori_H * prob_E_dado_H) / prob_E
    '''
    return (priori_H * prob_E_dado_H) / prob_E

def prob_E(priori_H, prob_E_dado_H, prob_E_no_dado_H):
    '''Función que regresa la probabilidad de la evidencia.

    Variables de entrada:
    - priori_H = probabidad de la hipótesis
    - prob_E_dado_H = probabidad de la evidencia dada la hipótesis
    - prob_E_no_dado_H = probabilidad de la evidencia no dada la hipótesis

    return (priori_H * prob_E_dado_H) + (no_priori_H * prob_E_no_dado_H)
    '''
    no_priori_H = 1 - priori_H
    return (priori_H * prob_E_dado_H) + (no_priori_H * prob_E_no_dado_H)


if __name__ == '__main__':
    prob_cancer = 1 / 100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10 / 99999
    prob_no_cancer = 1 - prob_cancer

    prob_sintoma = prob_E(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma_dado_no_cancer)
    prob_cancer_dado_sintoma = calcular_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)

    print(prob_cancer_dado_sintoma)