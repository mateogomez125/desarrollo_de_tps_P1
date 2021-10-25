'''
Leer una matriz de tres filas por tres columnas y calcular la suma 
de cada una de sus filas y de sus columnas, colocando los resultados en dos vectores,
uno para la suma de las filas y otro para la suma de las columnas. 

'''
import numpy as np 
import random

matriz=np.array([[0]*3]*3)
def mostrar_matriz(matriz):
    datos=matriz.shape
    filas=datos[0]
    columnas=datos[1]
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f,c],end=' ')
        print()
def carga_de_matriz_random(matriz):
    datos=matriz.shape
    filas=datos[0]
    columnas=datos[1]
    for f in range(filas):
        for c in range(columnas):
            matriz[f,c]=random.randint(1,6)
    return matriz
def suma_de_filas(matriz):
    suma=0
    datos=matriz.shape
    filas=datos[0]
    columnas=datos[1]
    vectorf=[0]*filas
    for f in range(filas):
        for c in range(columnas):
            suma= suma + matriz[f,c]
            vectorf[f]=suma
        suma=0
    return vectorf
def suma_de_columnas(matriz):
    suma=0
    datos=matriz.shape
    filas=datos[0]
    columnas=datos[1]
    vectorf=[0]*columnas
    for c in range(columnas):
        for f in range(filas):
            suma= suma + matriz[f,c]
            vectorf[c]=suma
        suma=0
    return vectorf

carga_de_matriz_random(matriz)
mostrar_matriz(matriz)
print()
print()
print(suma_de_filas(matriz))
print()
print()
print(suma_de_columnas(matriz))