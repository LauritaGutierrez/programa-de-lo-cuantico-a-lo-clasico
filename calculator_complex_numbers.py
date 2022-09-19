# Hago uso de funciones para solucionar las operaciones solicitadas con numeros complejos
import cmath
# son las sig. operaciones:
#1.Suma
#2.Producto
#3.Resta
#4.División
#5.Módulo
#6.Conjugado
#7.Conversión entre representaciones polar y cartesiano
#8.Retornar la fase de un número complejo.

import math

# son 4 variables a,b,c,d en la función de complejos.

def sum_complejos(a,b,c,d):
    num_real = a+c
    num_imaginario = b+d
    return (num_real, num_imaginario)


def rest_complejos (a,b,c,d):
    num_real = a - c
    num_imaginario = b - d
    return (num_real, num_imaginario)


def division_complejos(a1, a2):
    return(a1/a2)


def product_complejos (a,b,c,d):
    return ((a * c)-(b * d)+(b * c)+(a * d))


def modulos_complejos (a,b):
    return (math.sqrt(a ** 2 + b ** 2))


def conjugado_complejos (a,b):
    return a - b

def polares_cartesianos_complejos (a,b):
    angulo_theta = math.radians(a)
    x = a * math.cos (angulo_theta)
    y = a * math.sin (angulo_theta)
    return (x,y)

def fase_complejo (a1):
    theta= (a1[1]/a1[0])
    return ((math.degrees(math.atan(theta))))

def modulo(a):
    res = math.sqrt((a[0]**2) + (a[1]**2))
    return res


def multiMat(a, b):
    rowsA, columnsA = len(a), len(a[0])
    rowsB, columnsB = len(b), len(b[0])
    res = [[(0, 0) for j in range(columnsA)] for i in range(rowsA)]
    if columnsA == rowsB:
        for i in range(rowsA):
            for j in range(columnsB):
                for k in range(rowsB):
                    m = product_complejos(a[i][k], b[k][j])
                    n = res[i][j]
                    res[i][j] = sum_complejos(m, n)
    return res
def accion(a, b):
    res = multiMat(a, b)
    for i in range(len(res)):
        res[i] = res[i][:1]
    return res

