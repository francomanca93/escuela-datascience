
<div align="center">
  <h1>Programación orientada a objetos y Algoritmos con Python</h1>
</div>

<div align="center"> 
  <img src="readme_img/poo-python.png" width="150">
</div>

### Objetivos
El contenido de este documento son apuntes del [Curso de POO y Algoritmos con Python](https://platzi.com/clases/poo-python/) y busca ser una guía a través de los conceptos de la programación orientada a objetos y algoritmos. El mismo está dictado por [David Aroesti](https://github.com/jdaroesti) del team [Platzi](https://platzi.com).

Objetivos del documento:
- Entender como funciona la Programación orientada a Objetos
- Entender cómo medir la eficiencia temporal y espacial de nuestro algoritmos.
- Entender cómo y por qué graficar.
- Aprender a resolver problemas de búsqueda, ordenación y optimización.

## Tabla de contenido 
- [Programación orientada a objetos](#Programación-orientada-a-objetos)
    - [Programación orientada a objetos en Python](#Programación-orientada-a-objetos-en-python)
    - [Tipos de datos abstractos](#Tipos-de-datos-abstractos)
    - [Decomposición](#Decomposición)
    - [Abstracción](#Abstracción)
- [Complejidad algorítmica](#Complejidad-algorítmica)

- [Algoritmos de búsqueda y ordenación](#Algoritmos-de-búsqueda-y-ordenación)

- [Ambientes virtuales](#Ambientes-virtuales)

- [Graficar](#Graficar)

- [Algoritmos de optimización](#Algoritmos-de-optimización)



## Programación orientada a objetos

### Programación orientada a objetos en Python

Uno de los elementos más importantes de los lenguajes de programación es la utilización de clases para organizar programas en módulos y abstracciones de datos.

La clave para entender la programación orientada a objetos es pensar en objetos como agrupaciones de datos y los métodos que operan en dichos datos.

La programación orientada a objetos nos permite modelar cosas reales y concretas del mundo y sus relaciones con otros objetos.

Por ejemplo: 
- Representar a una persona con propiedades como nombre, edad, género, etc. y los comportamientos de dicha persona como caminar, cantar, comer, etc. 
- Representar unos audífonos con propiedades como su marca, tamaño, color, etc. y sus comportamientos como reproducir música, pausar y avanzar a la siguiente canción.

Cuando decimos "Los objetos son las principales cosas que un programa de Python manipula. Cada objeto tiene un tipo que define qué cosas puede realizar un programa con dicho objeto.", nos estamos refiriendo a las ideas principales de la programación orientada a objetos. Hemos utilizado los tipos lista y diccionario, entre muchos otros, así como los métodos asociados a dichos tipos.

Así como los creadores de un lenguaje de programación sólo pueden diseñar una fracción muy pequeña de todas las funciones útiles (como ```abs, float, type```, etc.), también pueden escribir una fracción muy pequeña de los tipos útiles (```int, str, dict, list```, etc.). Ya sabemos los mecanismos que nos permiten crear funciones, ahora veremos los mecanismos que nos permiten crear nuevos tipos (o clases).

#### Clases
Las clases nos permiten crear nuevos tipos que contiene información arbitraria sobre un objeto. En el caso del hotel, podríamos crear dos clases `Hotel()` y `Cuarto()` que nos permitiera dar seguimiento a las propiedades como número de cuartos, ocupación, aseo, tipo de habitación, etc.

Es importante resaltar que las clases sólo proveen estructura. Son un molde con el cual podemos construir objetos específicos. 

Para definir una clase, simplemente utilizamos el keyword class. Por ejemplo:

```py
class Hotel:
    pass
```

La clase señala las propiedades que los hoteles que modelemos tendrán, pero no es ningún hotel específico. Para eso necesitamos las instancias.

#### Instancias
Mientras que las clases proveen la estructura, las instancias son los objetos reales que creamos en nuestro programa: un hotel llamado PlatziHotel o Hilton.

Una vez que tenemos una clase llamada Hotel podemos generar una instancia
llamando al constructor de la clase.

```py
hotel = Hotel()
```

Los atributos de clase nos permiten:

- Representar datos.
- Procedimientos para interactuar con los mismos (métodos).
- Mecanismos para esconder la representación.

Para acceder a los atributos de estos objetos se hace a través de la notación de punto. Además puede tener atributos privados (Por convención comienzan con _ ).


#### Atributos de la instancia
Los atributos de la instancia describen lo que representa el objeto.

Todas las clases crean objetos y todos los objetos tienen atributos. Utilizamos el método especial `__init__` para definir el estado inicial de nuestra instancia.

Recibe como primer parámetro obligatorio `self` (que es simplemente una
referencia a la instancia).
```py
class Hotel:
    
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0


hotel = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)
print(hotel.lugares_de_estacionamiento) # 20
```
#### Método de la instancia

Los métodos de instancia nos indican qué podemos hacer con las instancias de dicha clase y normalmente operan en los mencionados atributos.
Los métodos son equivalentes a funciones dentro de la definición de la clase, pero todos reciben `self` como primer argumento.

```py
class Hotel:

    ...

    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupacion_total(self):
        return self.huespedes


hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
hotel.checkout(1)
hotel.ocupacion_total() # 2

```

Estructura de la definición de una clase

```py

# definición de clase

# Primero definimos el nombre de la clase y podemos determinar si hereda de otra clase.
class nombre_de_la_clase(super_clase):

    # El método init es un constructor, y siempre los métodos dentro
    # de los parámetros inician con el parámetro self
    def __init__(self, params):
        expresion

    # Las clases pueden tener comportamientos,
    # y estos los definimos con los métodos.
    def nombre_del_metodo(self, params):
        expresion

```

Ejemplo:

```py

# Definición
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'


# Uso
>>> david = Persona('David', 28)
>>> karl = Persona('Karl', 26)
>>> 
>>> david.saluda(karl)
>>> 'Hola Karl, me llamo David'

```

### Tipos de datos abstractos

En Python todo es un objeto y tiene un tipo, esto significa que todo lo que hacemos en nuestro programa tiene una representación en memoria, los datos y el comportamiento se puede encapsular en un objeto.

Los tipos nos permiten modelar y manipular el mundo a través de la programación.

Las formas de interactuar con un objeto son:
- Creación
- Manipulación
- Destrucción

Cuando trabajamos con programación orientada a objetos tenemos varias ventajas:

- **Decomposición**: podemos estructurarlos en objetos mas pequeños.
- **Abstracción**: no nos preocupamos el funcionamiento del proceso de su comportamiento.
- **Encapsulación**: podemos esconder ciertos datos que solo son relevantes internamente en el objeto.

[Primera practica de POO en Python](https://github.com/francomanca93/Escuela-DataScience/blob/master/poo-y-algoritmos/coordenada.py)

### Decomposición

La decomposición es partir un problema en problemas más pequeños. 

Las clases permiten crear mayores abstracciones en forma de componentes. 

Cada clase se encarga de una parte del problema y el programa se vuelve más fácil de mantener.

[Practica](https://github.com/francomanca93/Escuela-DataScience/blob/master/poo-y-algoritmos/decomposicion.py). Ejemplo simple en el cual se trata de modelar un automovil y decomponer en clases que representen a otros objetos, ejemplo, Motor.

### Abstracción

Se trata de enfocarnos en la información relevante. Se debe separar la información central de los detalles secundarios. Para realizar este procedimiento podemos utilizar variables y métodos (privados o públicos). [Más info en Wiki](https://es.wikipedia.org/wiki/Abstracci%C3%B3n_(inform%C3%A1tica))

[Practica](https://github.com/francomanca93/Escuela-DataScience/blob/master/poo-y-algoritmos/abstraccion.py). Ejemplo simple en el cual se trata de modelar una Lavadora y abstraerse del funcionamiento de la misma con métodos ocultos.

## Complejidad algorítmica

## Algoritmos de búsqueda y ordenación

## Ambientes virtuales

## Graficar

## Algoritmos de optimización
