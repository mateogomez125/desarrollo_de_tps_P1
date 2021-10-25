'''
Realizar un programa que, dado una matriz cuadrada con valores enteros entre 1 y 50 (al azar),
la muestra y luego realice las permutaciones de filas y columnas, 
utilizando un procedimiento que permuta dos elementos, y vuelva a mostrarla.
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
    pass
def carga_de_matriz_random(matriz):
    datos=matriz.shape
    filas=datos[0]
    columnas=datos[1]
    for f in range(filas):
        for c in range(columnas):
            matriz[f,c]=random.randint(1,50)
    return matriz

def permutacion(matriz):
    datos=matriz.shape
    filas=datos[0]
    columnas=datos[1]
    for i in range(filas):
        for j in range(i+1,columnas):
            aux=matriz[i,j]
            matriz[i,j]=matriz[j,i]
            matriz[j,i]=aux
            print('cambio:')
            mostrar_matriz(matriz)
            print()
    return matriz

carga_de_matriz_random(matriz)
print()
mostrar_matriz(matriz)
print()
permutacion(matriz)
print()
mostrar_matriz(matriz)