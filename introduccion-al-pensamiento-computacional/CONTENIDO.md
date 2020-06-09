# Introducción al Pensamiento Computacional con Python

El contenido de este documento busca ser una guía a través de los conceptos del pensamiento computacional. El mismo está dictado por [David Aroesti](https://github.com/jdaroesti) del team Platzi.

## Tabla de contenidos
- [Algoritmos básicos](#Algoritmos-básicos)
    - [Enumeración exhaustiva](#Enumeración-exhaustiva)
    - [Aproximación de soluciones](#Aproximacion-de-soluciones)
    - [Busqueda binaria](#Busqueda-binaria)
- [Recursividad](#Recursividad)
- [Tipos estructurados, mutabilidad y funciones de alto nivel](#Tipos-estructurados-mutabilidad-y-funciones-de-alto-nivel)
    - [Funciones como objetos](#Funciones-como-objetos)
    - [Tuplas](#Tuplas)
    - [Rangos](#Rangos)
    - [Listas](#Listas)
    - [Diccionarios](#Diccionarios)
- [Pruebas y debugging](#Pruebas-y-debugging)
    - [Pruebas de caja negra](#Pruebas-de-caja-negra)
    - [Pruebas de caja cristal](#Pruebas-de-caja-cristal)
    - [Debugging](#Debugging)
- [Excepciones y afimaciones](#Excepciones-y-afimaciones)



## Algoritmos básicos

#### Enumeración exhaustiva. 
[Práctica](https://github.com/francomanca93/Escuela-DataScience/blob/master/introduccion-al-pensamiento-computacional/enumeracion.py)

Tambien llamado ["busqueda de fuerza bruta"](https://es.wikipedia.org/wiki/B%C3%BAsqueda_de_fuerza_bruta) o "adivida y verifica".

Consiste en enumerar sistemáticamente todos los posibles candidatos para la solución de un problema, con el fin de chequear si dicho candidato satisface la solución al mismo. 
  
Uno de los primero algoritmos en los que hay que pensar.

#### Aproximacion de soluciones. 
[Práctica](https://github.com/francomanca93/Escuela-DataScience/blob/master/introduccion-al-pensamiento-computacional/aproximacion.py)

Similar al algoritmo de Enumeración exhaustiva, pero no necesita una respuesta exacta.

Si nos queremos aproximar a una solucion tenemos que definir que tan cerca queremos estar de esta. A esto lo llamamos epsilon, diferencia entre la realidad y la aproximación. Es el error que estamos dispuesto a cometer. Ejemplo de errores que llamamos epsilon:
- 1% = 1/100 = 0.01 
- 5% = 5/100 = 0.05

Como siempre en programación debemos hacer un trade-off, no podemos ser precisos y rápidos a la ves, por lo tanto cuando nuestro epsilon es muy pequeño esto significa que debemos realizar mas iteraciones para llegar a la aproximación, lo cual significa sacrificar tiempo. Y por otro lado si queremos que nuestro tiempo de ejecución sea lo mas corto posible debemos sacrificar la precisión aumentando el valor de epsilon.

#### Busqueda binaria. 
[Práctica](https://github.com/francomanca93/Escuela-DataScience/blob/master/introduccion-al-pensamiento-computacional/busqueda_binaria.py)

[Busqueda binaria](https://es.wikipedia.org/wiki/B%C3%BAsqueda_binaria) es un algoritmo de búsqueda que encuentra la posición de un valor en un array ordenado.​ 

Compara el valor con el elemento en el medio del array, si no son iguales, la mitad en la cual el valor no puede estar es eliminada y la búsqueda continúa en la mitad restante hasta que el valor se encuentre.


[Programa uniedo todos los algoritmos básicos utilizando funciones.](https://github.com/francomanca93/Escuela-DataScience/blob/master/introduccion-al-pensamiento-computacional/funciones.py)

## Recursividad

[Recursividad](https://es.wikipedia.org/wiki/Recursi%C3%B3n_(ciencias_de_computaci%C3%B3n))

Deficion algoritmica: Forma de crear soluciones utilizando el concepto de "divide y venceras". Esto significa que un problema podemos resolverlo utilizando versiones mas pequeñas del mismo problema. Se trata de encontrar una solucion base facil de resolver y utilizarla para que iterativamente encontremos la solucion del problema.

Deficion programatica: Funcion que se llama a si misma.

Aplicando recusividad
- [Factorial]()
- [Fibonacci]()
