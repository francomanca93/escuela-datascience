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