# PROGRAMA SIMULACIÓN DE LO CLÁSICO A LO CUÁNTICO

Este programa se trata de una simulacion cuantica, haciendo uso de librerias y a su vez mostrar casos de prueba, Se va a basar en el libro guía de la clase, "Quantum Computing for Computer Scientists", capítulo 3 ya que presenta los temas, conceptos e ideas representadas para comprender la mecánica cuantica.  

## Lo que contiene

Este programa de simulación tendrá cuatro experimentos, los cuales estarán hechos en tipo libreria, con ejemplo de ejecución, comentarios respectivos, estos experimentos son:

```
1. Los experimento de la canicas con coeficiente booleanos
2. Experimento de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
3. Experimento de las múltiples rendijas cuántico.
4. Función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados.
```

### Algunos requisitos y cosas necesarias

Las cosas necesita a la hora de tener el programa son:

-Esta libreria, PROGRAMA SIMULACIÓN DE LO CLÁSICO A LO CUÁNTICO, se puede ejecutar en visual code de Python, en IDLE y en PyCharm.

-Se requieren conocimientos sobre grafos y matrices, sus ecuaciones cuanticas.

- ordenador adecuado para lograr ejecutar un lenguaje de programacion.

### Pruebas

Las pruebas para cada programa
se debe importar la libreria de experimentos_clasico_cuantico, ya que se hace uso de esta.

```
1.
con false and true para evaluar el valor.
matriz = np.array(([[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 1],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [1, 0, 0, 0, 1, 0]])
El estado = [6, 2, 1, 5, 3, 10]
luego de 1 click: [0, 0, 12, 5, 1, 9]

2.
matr1 = [[0, 1/6, 5/6], [1/3, 1/2, 1/6], [2/3, 1/3, 0]]
vec1 = [[1/6], [1/6], [2/3]]
c = 3
self.assertEqual(sistClasico(m1, v1, n), [[0.451], [0.313], [0.237]])



4.
Los valores del vector para poder graficar con matplotlib se debe instalar este programa.
```

## Construido con

* Lenguaje Python
* Hecho en entorno de Pycharm

## Autor

* **Laura Gutiérrez** - *Ingenieria de sistemas* - CNYT


