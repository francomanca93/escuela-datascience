<div align="center">
  <h1>Introducción al Pensamiento Probabilístico
</h1>
</div>

<div align="center"> 
  <img src="readme_img/introduccion-pensamiento-probabilistico.png" width="">
</div>

# Introducción al documento

El contenido de este documento son apuntes del [Curso de Introducción al Pensamiento Probabilístico](https://platzi.com/clases/probabilistica/) y busca ser una guía. El mismo está dictado por [David Aroesti](https://github.com/jdaroesti) del team [Platzi](https://platzi.com).

### Objetivos del documento
- Desarrollar el pensamiento probabilistico. Este nos permitirá entender:
    - Como calcular las probabilidades de lo que sucede a nuestro alrededor.
    - Como actualizar estas probabilidades conforme se va teniendo expereciencia y evidencia del mundo.
- Una introducción al Machine Learning y a los algoritmos de clasificación.

# Tabla de contenido
- [Programación probabilística](#Programación-probabilística)
    - [Introducción a la programación probabilística](#Introducción-a-la-programación-probabilística)
    - [Probabilidad condicional](#Probabilidad-condicional)
    - [Teorema de Bayes](#Teorema-de-Bayes)
    - [Aplicando Teorema de Bayes](#Aplicando-Teorema-de-Bayes)
    - [Aplicaciones del Teorema de Bayes](#Aplicaciones-del-Teorema-de-Bayes)
- [Mentiras estadísticas](#Mentiras-estadísticas)
    - [Garbage in, garbage out](#Garbage-in,-garbage-out)
    - [Imágenes engañosas](#Imágenes-engañosas)
    - [Cum Hoc Ergo Propter Hoc](#Cum-Hoc-Ergo-Propter-Hoc)
    - [Prejuicio en el muestreo](#Prejuicio-en-el-muestreo)
    - [Falacia del francotirador de Texas](#Falacia-del-francotirador-de-Texas)
    - [Porcentajes confusos](#Porcentajes-confusos)
    - [Falacia de regresión](#Falacia-de-regresión)
- [Introducción a Machine Learning](#Introducción-a-Machine-Learning)
    - [Feature vectors](#Feature-vectors)
    - [Métricas de distancia](#Métricas-de-distancia)
- [Agrupamiento](#Agrupamiento)
    - [Introducción al agrupamiento](#Introducción-al-agrupamiento)
    - [Agrupamiento jerárquico](#Agrupamiento-jerárquico)
    - [Agrupamiento K-means](#Agrupamiento-K-means)
    - [Otras técnicas de agrupamiento](#Otras-técnicas-de-agrupamiento)
- [Clasificación](#Clasificación)
    - [Introducción a la clasificación](#Introducción-a-la-clasificación)
    - [Clasificación K-nearest neighbors](#Clasificación-K-nearest-neighbors)
    - [Otras tecnicas de clasificación](#Otras-tecnicas-de-clasificación)


## Programación probabilística
### Introducción a la programación probabilística

La **programación probabilística** utiliza [_probabilidades_](https://es.wikipedia.org/wiki/Teor%C3%ADa_de_la_probabilidad) y [_modelos probabilísticos_](https://es.wikipedia.org/wiki/Modelo_probabil%C3%ADstico) para ejecutar cómputos. Se utiliza en una gran cantidad campos: investigación científica, inteligencia artificial, medicina, etc.

Existen lenguajes y librerías especializadas para ejecutar este tipo de cómputo, como [_Pyro_](https://pyro.ai/) de [Uber](https://www.uber.com/ar/en/).

### Probabilidad condicional

La [**probabilidad condicional**](https://es.wikipedia.org/wiki/Probabilidad_condicionada) es la probabilidad de que ocurra un evento _A_, sabiendo que también sucede otro evento _B_. La probabilidad condicional se escribe **_P(A|B)_**, y se lee **_«la probabilidad de A dado B»_**.

No tiene por qué haber una relación causal o temporal entre _A_ y _B_. _A_ puede preceder en el tiempo a _B_, sucederlo o pueden ocurrir simultáneamente. _A_ puede causar _B_, viceversa o pueden no tener relación causal. Las relaciones causales o temporales son nociones que no pertenecen al ámbito de la probabilidad. Pueden desempeñar un papel o no, dependiendo de la interpretación que se le dé a los eventos.

La notación para escribir,

_«la probabilidad de A y B suceden»_: `P(A and B) = P(A) * P(B_` 

_«la probabilidad de B»_: `P(B) = P(A) * P(B|A) + P(Ac) * P(B|Ac)`

Un ejemplo de esto puede ser la probabilidad que una persona **tenga cáncer**, luego de realizar pruebas.

`P(cancer) = P(positivo) * P(cancer|positivo) + P(negativo) * P(cancer|negativo)`

Otro ejemplo es cual es la probabilidad de que una persona **use drogas**, pero como dato adicional esta persona es músico.

`P(drogas) = P(musico) * P(drogas|musico) + P(no sea musico) * P(drogas|no sea musico)`

### Teorema de Bayes

El [**teorema de Bayes**](https://es.wikipedia.org/wiki/Teorema_de_Bayes), en la teoría de la probabilidad, es una proposición planteada por el matemático inglés [Thomas Bayes](https://es.wikipedia.org/wiki/Thomas_Bayes) (1702-1761)​ y publicado en 1763, tras su muerte.
<br>
<div align="center">
    <img src="readme_img/Thomas_Bayes.gif" height="60%">
</div>
<br>

Este expresa que la probabilidad condicional de un evento aleatorio _A_ dado _B_ en términos de la distribución de probabilidad condicional del evento _B_ dado _A_ y la distribución de probabilidad marginal de solo _A_.

En términos más generales y menos matemáticos, el teorema de Bayes es de enorme relevancia puesto que vincula la probabilidad de _A_ dado _B_ con la probabilidad de _B_ dado _A_. 

Por ejemplo, sabiendo la probabilidad de tener un dolor de cabeza dado que se tiene gripe, se podría saber (si se tiene algún dato más), la probabilidad de tener gripe si se tiene un dolor de cabeza. Muestra este sencillo ejemplo la alta relevancia del teorema en cuestión para la ciencia en todas sus ramas, puesto que tiene vinculación íntima con la comprensión de la probabilidad de aspectos causales dados los efectos observados.

> Sea <img src="readme_img/conjunto-a1-an.svg" height="15"> un conjunto de sucesos mutuamente excluyentes y exhaustivos, y tales que la probabilidad de cada uno de ellos es distinta de cero (0). Sea B un suceso cualquiera del que se conocen las probabilidades condicionales <img src="readme_img/pba.svg" height="15">. Entonces, la probabilidad <img src="readme_img/pab.svg" height="15"> viene dada por la expresión:
> <br>
> <div align="center">
>     <img src="readme_img/bayes.svg" height="60">
> </div>
> <br>
> 
> donde:
> - <img src="readme_img/pai.svg" height="15"> son las probabilidades a priori,
> - <img src="readme_img/pba.svg" height="15"> es la probabilidad de <img src="readme_img/B.svg" height="12"> en la hipótesis <img src="readme_img/Ai.svg" height="15">,
> - <img src="readme_img/pab.svg" height="15"> son las probabilidades a posteriori.


> Como sabemos que <img src="readme_img/pb.svg" height="15"> podemos reemplazarlo en la ecuación y nos quedaría:
> <br>
> <div align="center">
>     <img src="readme_img/bayes-expandido.svg" height="60">
> </div>
> <br>

#### Entendiendo teorema de bayes

En el siguiente enlace hay una excelente explicación animada del [Teorema de Bayes en 3Blue1Brown](https://www.youtube.com/watch?v=HZGCoVF3YvM&t).

En las sigueints imagenes se puede ver el Teorema de Bayes y una representación visual del mismo. 

<br>
<div align="center">
    <img src="readme_img/bayes-3b1b.png" height="">
</div>
<div align="center">
    <img src="readme_img/geometria-bayes.png" height="">
</div>
<br>

Analicemos la gráfica 
- _P(H) = 13%_. **Probabilidad a priori** (Hipotesis)
- _P(E|H) = 35%_ (El 35% de P(H)). Probabilidad del Evento **E** dada la probabilidad de la Hipotesis **H**.
- _P(¬H) = 100% - 13%_. Probabilidad de que no ocurra la Hipotesis. 
- P(E|¬H) = 13% (El 13% de P(¬H)). Probabilidad del Evento **E** dada la probabilidad de la Hipotesis no ocurra **¬H**.
- _P(H|E) = 28%_. **Probabilidad a posteriori**. Probabilidad de la Hipotesis **H** dada la probabilidad de que ocurra el Evento **E**  .

_P(H|E) = P(H) * P(E|H) / (P(H) * P(E|H) + P(¬H) * P(E|¬H))_ = (0,13×0,35)÷(0,13×0,35 + (1−0,13)×0,13)

En el siguiente enlace se puede aplicar lo anterior descripto y jugar con diferentes probabilidades del [Teorema de Bayes de forma gráfica](https://www.skobelevs.ie/BayesTheorem/).

### Aplicando Teorema de Bayes

En el siguiente ejercicio se analizará los síntomas que alguien tiene antes de presentarse al médico y poder determinar cual es la probabilidad de que tenga cierta enfermedad. En este caso, la enfermedad será cancer. 

<br>
<div align="center">
    <img src="readme_img/datos-sintomas-cancer.png" height="">
</div>
<br>

Analizando variables:
- **H**ipótesis = Tener cancer. 
    - _P(H) = 1 / 100 000 = 0,00001 = 0,001%_
- **E**videncia = Presentar síntomas.
- ¬**H**ipótesis = No tener cancer. 
    - _P(¬H) = 1 - P(H)= 0,99999 = 99,999%_
- P(E|H) = Probabilidades de presentar síntomas dado que tenga cancer.
    - _P(E|H) = 1 = 100%_
- P(E|¬H) = Probabilidades presentar síntomas dado que no tenga cancer.
    - _P(E|¬H) = 10 / 99999 = 0,000100001 = 0,0100001%_

[Script](https://github.com/francomanca93/Escuela-DataScience/blob/master/introduccion-al-pensamiento-probabilistico/scripts/sintomas.py) que cálcula el teorema de bayes.

```py
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
```

Salida:
```
0.09090909090909091
```

### Aplicaciones del Teorema de Bayes

El Teorema de Bayes es uno de los mecanismos matemáticos más importantes en la actualidad. A grandes rasgos, nos permite medir nuestra certidumbre con respecto a un suceso tomando en cuenta nuestro conocimiento previo y la evidencia que tenemos a nuestra disposición. El Teorema de Bayes permea en tu vida diaria, desde descubrimientos científicos hasta coches autónomos, el Teorema de Bayes es el motor conceptual que alimenta mucho de nuestro mundo moderno.
​

En esta lectura me gustaría darte ejemplos de cómo se utiliza en la vida moderna para que puedas comenzar a implementarlo en tus proyectos, análisis y hasta en
tu vida personal.

#### Turing y el código enigma de los Nazis

​
Casi todos sabemos que [Alan Turing](https://es.wikipedia.org/wiki/Alan_Turing) es uno de los padres del cómputo moderno; pocos saben que fue gracias a él que los aliados pudieron tener una ventaja decisiva cuando Turing logró descifrar el código enigma que encriptaba todas las comunicaciones nazis; pero aún menos saben que para romper este código utilizó el Teorema de Bayes.

<br>
<div align="center">
    <img src="readme_img/alan-turing.jpg" height="300">
    <p><b>Alan Turing</b></p>
</div>
<br>

Lo que hizo Turing fue aplicar el Teorema para descifrar un segmento de un mensaje, calcular las probabilidades iniciales y actualizar las probabilidades
de que el mensaje era correcto cuando nueva evidencia (pistas) era presentada.

#### Finanzas

Una de las decisiones más difíciles cuando estás manejando un portafolio de inversión es determinar si un instrumento financiero (acciones, valores, bonos, etc.) se va a apreciar en el futuro y por cuánto, o si, por el contrario se debe vender el instrumento. Los portafolios managers más exitosos utilizan el Teorema de Bayes para analizar sus portafolios.
​

En pocas palabras, puedes determinar las probabilidades iniciales basándote en el rendimiento previo de tu portafolio o en el rendimiento de toda la bolsa y
luego añadir evidencia (estados financieros, proyecciones del mercado, etc.) para tener una mayor confianza en las decisiones de venta o compra.

#### Derecho

El Derecho es uno de los campos más fértiles para aplicar pensamiento bayesiano. Cuando un abogado quiere defender a su cliente, puede comenzar a evaluar una probabilidad de ganar (basada en su experiencia previa, o en estadísticas sobre el número de juicios y condenados con respecto del tema legal que competa) y actualiza su probabilidad conforme vayan sucediendo los eventos del proceso jurisdiccional.
​

Cada nueva notificación, cada prueba y evidencia que encuentre, etc. sirve para actualizar la confianza del abogado.

#### Inteligencia artificial

El Teorema de Bayes es central en el desarrollo de sistemas modernos de inteligencia artificial. Cuando un coche autónomo se encuentra navegando en las calles, tiene que identificar todos los objetos que se encuentran en su “campo de visión” y determinar cuál es la probabilidad de tener una colisión. Esta probabilidad se actualiza con cada movimiento de cada objeto y con el propio movimiento del vehículo autónomo. Esta constante actualización de probabilidades es lo que permite que los vehículos autónomos tomen decisiones
acertadas que eviten accidentes.
​

En esta rama existen muchos ejemplos como para cubrirlos todos, pero quiero por lo menos mencionar algunos casos de uso: 
- filtros de spam.
- reconocimiento de voz.
- motores de búsqueda.
- análisis de riesgo crediticio
- ofertas automáticas, 
- y un largo etcétera.
​

## Mentiras estadísticas

Aunque nuestro software este bien estructurado, hay veces que el mismo puede arrojarnos errores, estos errores son como un tercer nivel de bugs, donde podemos identicar a 3:
1. **Error de Sintaxis**. Error tradicional.
2. **Error de Lógica**. Bugs mas complejos.
3. **Error en el diseño del software**. Esto se debe por la forma en la que pensamos y llegamos a conclusiones. Bugs que no están en el programa en sí. Son los más difíciles de encontrar.  

En esta sección veremos diferentes errores de pensamientos que nos podemos encontrar y que debemos aprender a detectar cuando estemos frente a uno. 

### Garbage in, garbage out
La calidad de nuestros datos es igual de fundamental que la precisión de nuestros cómputos. Cuando los datos son errados, aunque tengamos un cómputo excelente nuestro resultado serán erróneos.

En pocas palabras: con datos errados las conclusiones serán erradas.

### Imágenes engañosas

Las visualizaciones son muy importantes para entender un conjunto de datos. Errores que pueden confundir o manipular y llegar a conclusiones erroneas cuando analizamos gráficas pueden ser: 
- **Variación de escalas.** Cuando se juega con la escala se puede llegar a conclusiones incorrectas.
- **Sin Etiquetas.** Si no hay etiquetas, no se puede llegar a una conclusión. 
- **Sin escalas.** Si no hay escalas, no podemos comparar. 

**Nunca se debe confiar en una gráfica sin escalas o etiquetas.**

### Cum Hoc Ergo Propter Hoc

[Cum Hoc Ergo Propter Hoc](https://es.wikipedia.org/wiki/Cum_hoc_ergo_propter_hoc) significa _Después de esto, eso_; ó _entonces a consecuencia de esto, eso_. 

Esto es una falacia (es decir, un argumento que parece válido, pero que no lo es) que se comete al inferir que dos o más eventos están conectados causalmente porque se dan juntos.

La falacia consiste en inferir que existe una relación causal entre dos o más eventos por haberse observado una correlación estadística entre ellos. Esta falacia muchas veces se refuta mediante la frase **correlación no implica causalidad**. 

Dos variables están positivamente correlacionadas cuando se mueven en la misma dirección y negativamente correlacionadas cuando se mueven en direcciones opuestas. Esta correlación no implica causalidad.

Puede existir variables escondidas que generen la correlación.

Analizando la falacia: 
> En general, la falacia reside en que, dados dos eventos A y B, al descubrir una correlación estadística entre ambos, es un error inferir que A causa B sin antes considerar la validez de al menos una de las siguientes cuatro posibilidades:
> - Que B sea la causa de A.
> - Que haya un tercer factor desconocido que sea realmente la causa de la relación entre A y B.
> - Que la relación sea tan compleja y numerosa que los hechos sean simples coincidencias.
> - Que B sea la causa de A y al mismo tiempo A sea la de B, es decir, que estén de acuerdo, que sea una relación sinérgica o simbiótica donde la unión cataliza los efectos que se observan.

### Prejuicio en el muestreo

Para que un [muestra estadística](https://es.wikipedia.org/wiki/Muestra_estad%C3%ADstica) pueda servir como base para la inferencia estadística tiene que ser aleatorio y representativo.

Una muestra representativa es una pequeña cantidad ___algo___ que refleja, con la mayor precisión posible, a un grupo más grande. 

El prejuicio en el muestreo elimina la representatividad de las muestras.

A veces conseguir muestras es difícil, por lo que se utiliza a la población de más fácil acceso (ejemplo: en caso estudios universitarios), esto se debe evitar si queremos que nuestra sea representativa.

### Falacia del francotirador de Texas
### Porcentajes confusos
### Falacia de regresión

## Introducción a Machine Learning
### Feature vectors
### Métricas de distancia

## Agrupamiento
### Introducción al agrupamiento
### Agrupamiento jerárquico
### Agrupamiento K-means
### Otras técnicas de agrupamiento

## Clasificación
### Introducción a la clasificación
### Clasificación K-nearest neighbors
### Otras tecnicas de clasificación