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
    - [Ejercicio de Bayes en código](#Ejercicio-de-Bayes-en-código)
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

### Ejercicio de Bayes en código
### Aplicaciones del Teorema de Bayes

## Mentiras estadísticas
### Garbage in, garbage out
### Imágenes engañosas
### Cum Hoc Ergo Propter Hoc
### Prejuicio en el muestreo
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