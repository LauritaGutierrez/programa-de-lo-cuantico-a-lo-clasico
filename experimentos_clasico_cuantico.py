##Laura Gutierrez

##Importo estas librerias ya que me ayudan a realizar algunas de las operaciones y funciones necesarias
## importo algunas operaciones de una libreria que hice anteriormente de operaciones de complejos

from calculator_complex_numbers import *
import matplotlib.pyplot as plot
##Esta libreria es para poder graficar
import numpy as np
import math



## 1. El experimento de las canicas con coeficientes booleanos
## En este punto hago uso de dos funciones

def canicas_coeficientes(matr1, vec1):
    suma_v = 0
    matr = [0 for i in range(len(matr1))]
    for i in range(len(matr1)):
        for j in range(len(matr1)):
            for k in range(len(matr1[0])):
                suma_v = suma_v + matr1[i][k] * vec1[k]
            if suma_v == 0:
                matr[i] = False ##evalua si esto es falso o no, para poder retornar la matriz
            else:
                matr[i] = True
    return matr


def canicas_boo(matr1, vec1, c):
    if len(matr1) == 0 or len(vec1) == 0:
        print("Error, no se puede")
    elif len(matr1[0]) != len(vec1):
        print("Error, no se puede")
    else:
        cont = 1
        while cont <= c:
            vec = canicas_coeficientes(matr1, vec1)
            cont += 1
        return vec


## 2. Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.

def propabilistico(m, e, r):
    re = [0 for i in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            re[i] = re[i] + (m[i][j] * e[j])
    return propabilistico(m, re, r - 1) if r > 0 else re

## 3. Experimento de las múltiples rendijas cuántico.
##recibe la matriz, el vector

def sistCuantico(matr1, vec1, n):
    if len(matr1[0]) == len(vec1) and len(matr1[0]) == len(matr1):
        while n > 0:
            vec1 = accion(matr1, vec1)
            n -= 1
        for i in range(len(vec1)):
            vec1[i][0] = round(modulo(vec1[i][0]) ** 2, 2)
        return vec1


## 4.función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados
## Recibe el vector de estados para poder graficar sus probabilidades, hago uso de la libreria Mathplot

def diagrama_grafica(vector):
    datos = len(vector)
    x = np.array([x for x in range(datos)])
    y = np.array([round(vector[x][0] * 100, 2) for x in range(datos)])
    plot.bar(x, y, color='m', align='center')
    plot.title('probabilidades de un vector de estados')
    plot.show()

