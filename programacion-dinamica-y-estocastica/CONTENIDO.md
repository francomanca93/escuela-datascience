<div align="center">
  <h1>Programación Dinámica y Estocástica con Python</h1>
</div>

<div align="center"> 
  <img src="readme_img/programacion-dinamica-estocastica-python.png" width="">
</div>

# Introducción al documento

El contenido de este documento son apuntes del [Curso de Programación Dinámica y Estocástica con Python](https://platzi.com/clases/programacion-estocastica/) y busca ser una guía. El mismo está dictado por [David Aroesti](https://github.com/jdaroesti) del team [Platzi](https://platzi.com).


### Objetivos del documento
- Aprender cuándo utilizar Programación Dinámica y sus beneficios.
- Entender la diferencia entre programas deterministas y estocásticos.
- Aprender a utilizar Programación Estocástica.
- Aprender a crear simulaciones computacionales válidas.


# Tabla de contenido

- [Programación Dinámica](#Programación-Dinámica)
    - [Introducción a la Programación Dinámica](#Introducción-a-la-Programación-Dinámica)
    - [Optimización de Fibonacci](#Optimización-de-Fibonacci)
- [Caminos Aleatorios](#Caminos-Aleatorios)
    - [¿Qué son los caminos aleatorios?](#¿Qué-son-los-caminos-aleatorios?)
    - [Camino de Borrachos](#Camino-de-Borrachos)
- [Programas Estocásticos](#Programas-Estocásticos)
    - [Introducción a la Programación Estocástica](#Introducción-a-la-Programación-Estocástica)
    - [Cálculo de Probabilidades](#Cálculo-de-Probabilidades)
    - [Simulación de Probabilidades](#Simulación-de-Probabilidades)
    - [Inferencia Estadística](#Inferencia-Estadística)
    - [Media](#Media)
    - [Varianza y Desviación Estándar](#Varianza-y-Desviación-Estándar)
    - [Distribución Normal](#Distribución-Normal)
- [Simulaciones de Montecarlo](#Simulaciones-de-Montecarlo)
    - [¿Qué son las Simulaciones de Montecarlo?](#¿Qué-son-las-Simulaciones-de-Montecarlo?)
    - [Simulación de Barajas](#Simulación-de-Barajas)
    - [Cálculo de PI](#Cálculo-de-PI)
- [Muestreo e Intervalos de Confianza](#Muestreo-e-Intervalos-de-Confianza)
    - [Muestreo](#Muestreo)
    - [Teorema del Límite Central](#Teorema-del-Límite-Central)
- [Datos Experimentales](#Datos-Experimentales)
    - [¿Cómo trabajar con datos experimentales?](#¿Cómo-trabajar-con-datos-experimentales?)
    - [Regresión Lineal](#Regresión-Lineal)


## Programación Dinámica

### Introducción a la Programación Dinámica

<div align="center"> 
  <img src="readme_img/richard-bellman.jpg" width="">
</div>

[Richard Bellman](https://es.wikipedia.org/wiki/Richard_Bellman) fue quien puso el nombre de [Programación Dinámica](https://es.wikipedia.org/wiki/Programaci%C3%B3n_din%C3%A1mica) pero este  no tiene ninguna relación con lo que el nombre proyecta. El origen de este se dio para que los patrocinadores vieran esto como algo atractivo matemáticamente hablando. 

Ya sabiendo que Programación Dinámica no esta relacionado con su nombre, lo cierto es que si es una de las técnicas mas poderosas para poder optimizar cierto tipos de problemas.

Los problemas que puede optimizar son aquellos que tienen una subestructura óptima, esto significa que **una solución óptima global se puede encontrar al combinar soluciones óptimas de subproblemas locales**.

También nos podemos encontrar con los **problemas empalmados**, los cuales implican resolver el mismo problema en varias ocasiones para dar con una solución óptima.

Una técnica para obtener una alta velocidad en nuestro programa es la Memorización, el cual consiste en guardar cómputos previos y evitar realizarlos nuevamente. Normalmente se utiliza un diccionario, donde las consultas se pueden hacer en O(1), y para ello hacemos un cambio de tiempo por espacio.

### Optimización de Fibonacci

La serie de _Fibonacci_ se representa como `Fn = Fn-1 + Fn-2` y es muy simple implementarla de forma recursiva en código. Sin embargo es muy ineficiente hacerlo simplemente recursivo, ya que repetimos varias veces el mismo computo.

<div align="center"> 
  <img src="readme_img/FibbonacciRecurisive.png" width="">
  <p>Algoritmo de Fibonnaci</p>
</div>

Si te fijas en la imagen te darás cuenta de que repetimos varias veces el calculo para `f(4), f(3), f(2), f(1) y f(0)`, esto significa que nuestro algoritmo crece de forma **exponencial** `O(2^n)`.

Para optimizar nuestro algoritmo implementaremos en primer lugar la **función recursiva** para luego dar paso a la **memorización**.

Sabiendo que en [complejidad algoritmica](https://github.com/francomanca93/Escuela-DataScience/blob/master/poo-y-algoritmos/CONTENIDO.md#Complejidad-algor%C3%ADtmica) podemos analizar un algoritmo desde lo temporal y lo espacial, lo que se hace es **intercambiar espacio** (en memoria) **por tiempo.** Con esto las mejoras serán realmente sorprendentes.

En la siguiente [practica](https://github.com/francomanca93/Escuela-DataScience/blob/master/programacion-dinamica-y-estocastica/programacion_dinamica.py) podemos ver dos funciones aplicando recursividad. En una es unicamente recursividad, en la otra se aplica recursividad y memorización. Esto me permite calcular numeros más grandes de fibonacci de forma mas eficiente. 

## Caminos Aleatorios
###      ¿Qué son los caminos aleatorios?

Los [**caminos aleatorios**](https://es.wikipedia.org/wiki/Camino_aleatorio) son un tipo de simulación que elige aleatoriamente una decisión dentro de un conjunto de decisiones válidas. Se utiliza en muchos campos del conocimiento cuando los sistemas no son deterministas e incluyen elementos de aleatoriedad.

Ejemplo en diferentes ciencias donde se se observan los caminos aleatorios:

- En genética de poblaciones
  - El camino aleatorio describe las propiedades estadísticas de la [**deriva genética**](https://es.wikipedia.org/wiki/Deriva_gen%C3%A9tica).

- En física, 
  - Usamos modelos simplificados del [**movimiento browniano**](https://es.wikipedia.org/wiki/Movimiento_browniano) y difusión tales como el movimiento aleatorio de las moléculas en líquidos y gases. Véase, por ejemplo, la agregación limitada por difusión. 
  - Los caminos aleatorios y algunos de los caminos que interactúan consigo mismos juegan un papel en la [**teoría cuántica de campos**](https://es.wikipedia.org/wiki/Teor%C3%ADa_cu%C3%A1ntica_de_campos).

- En biología matemática, 
  - Los caminos aleatorios son utilizados para describir movimientos individuales de los animales y como esto contribuye a los [**movimientos colectivos**](https://es.wikipedia.org/wiki/Comportamiento_colectivo_de_los_animales) de estos, 
  - En ocasiones para desarrollar la [**dinámica de poblaciones**](https://es.wikipedia.org/wiki/Din%C3%A1mica_de_poblaciones).

- En matemáticas,
  - El camino aleatorio se utiliza para calcular las soluciones de la [**ecuación de Laplace**](https://es.wikipedia.org/wiki/Ecuaci%C3%B3n_de_Laplace). 
  - Para estimar la [**media armónica**](https://es.wikipedia.org/wiki/Media_arm%C3%B3nica).
  - Para varias construcciones en el análisis y la [**combinatoria**](https://es.wikipedia.org/wiki/Combinatoria).

- En informática, 
  - Los caminos aleatorios son utilizados para estimar el tamaño de la Web. En la World Wide Web conference-2006, Bar-Yossef et al. publicó sus descubrimientos y algoritmos para lo mismo.
  - En el procesamiento de imágenes, los caminos aleatorios son utilizados para determinar las etiquetas (es decir, “objeto” o “fondo”) para asociarlas con cada píxel. Este algoritmo se suele denominar como algoritmo de segmentación del camino aleatorio.

###      Camino de Borrachos

Este es un ejercicio donde empezando desde un punto 0 aleatoriamente podemos decidir que dirección tomar, dependiendo de las opciones establecidas.

Para realizar un ejemplo de aleatoriedad vamos a crear un programa que representara el problema del "Camino de Borrachos". Crearemos 3 clases: 

- [Borracho](https://github.com/francomanca93/Escuela-DataScience/blob/master/programacion-dinamica-y-estocastica/camino_de_borrachos/borracho.py): Representa al agente que camina.

- [Coordenada](https://github.com/francomanca93/Escuela-DataScience/blob/master/programacion-dinamica-y-estocastica/camino_de_borrachos/coordenada.py): Genera una abstracción de las coordenadas.

- [Campo](https://github.com/francomanca93/Escuela-DataScience/blob/master/programacion-dinamica-y-estocastica/camino_de_borrachos/campo.py): Representa el plano en el cual nos estamos moviendo.

Con esto luego vamos a graficar la distancia en la que termina nuestro agente a medida que definimos una mayor cantidad de pasos que puede dar en nuestra archivo principal [camino_aleatorio](https://github.com/francomanca93/Escuela-DataScience/blob/master/programacion-dinamica-y-estocastica/camino_de_borrachos/camino_aleatorio.py). 

Para realizar todo esto debemos crear un ambiente virtual para utlizar finalmente la libreria bokeh que nos permitira graficar:

```py
mkdir camino_de_borramos    # Creamos una carpeta para nuestro proyecto.
cd camino_de_borrachos      # Ingresamos a la carpeta.
python3 -m venv env         # Creamos nuestro ambiente virtual.
source env/bin/activate     # Activamos nuestro ambiente.
pip install bokeh           # Instalamos el paquete de bokeh para generar nuestra gráfica.

```

Dentro el pensamiento estocástico debemos realizar varias simulaciones, por ese motivo en el ejemplo anterior realizamos varios intentos. Lo importante de esta aleatoriedad es que podemos distribuirla a lo largo de varios intentos, con esto podemos obtener certeza de que el comportamiento de nuestro programa se comporte en que esperamos estadísticamente.

```
# Como salida tenemos:

BorrachoTradicional caminata aleatorio de 10 pasos
Media = 2.814
Maxima = 7.1
Minima = 0.0
BorrachoTradicional caminata aleatorio de 100 pasos
Media = 9.621
Maxima = 29.7
Minima = 0.0
BorrachoTradicional caminata aleatorio de 1000 pasos
Media = 30.506
Maxima = 63.7
Minima = 3.2
BorrachoTradicional caminata aleatorio de 10000 pasos
Media = 95.481
Maxima = 269.6
Minima = 18.6
```

Con la siguiente gráfica generada:

<div align="center"> 
  <img src="readme_img/bokeh_plot.png" width="">
  <p>Caminos aleatorios</p>
</div>

## Programas Estocásticos
###     Introducción a la Programación Estocástica

En un [programa determinístico](https://es.wikipedia.org/wiki/Algoritmo_determinista) si se conocen las entradas del algoritmo siempre producirá la misma salida, y la máquina interna pasará por la misma secuencia de estados. Este tipo de algoritmos ha sido el más estudiado durante la historia y por lo tanto resulta ser el tipo más familiar de los algoritmos, así como el más práctico ya que puede ejecutarse en las máquinas eficientemente. 

Los programas determinísticos son muy importantes, pero existen problemas que no pueden resolverse de esa manera.

La programación [estocástica](https://es.wikipedia.org/wiki/Proceso_estoc%C3%A1stico) permite introducir aleatoriedad a nuestros programas para crear simulaciones que permiten resolver otro tipo de problemas. Los programas estocásticos se aprovechan de que las distribuciones probabilísticas de un problema se conocen o pueden ser estimadas.

###     Cálculo de Probabilidades
###     Simulación de Probabilidades
###     Inferencia Estadística
###     Media
###     Varianza y Desviación Estándar
###     Distribución Normal

## Simulaciones de Montecarlo
###     ¿Qué son las Simulaciones de Montecarlo?
###     Simulación de Barajas
###     Cálculo de PI

## Muestreo e Intervalos de Confianza
###     Muestreo
###     Teorema del Límite Central

## Datos Experimentales
###     ¿Cómo trabajar con datos experimentales?
###     Regresión Lineal