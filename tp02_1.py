
import numpy as np
import random 
'''

Dada una matriz de 3 filas por 4 columnas, calcular la sumatoria de sus elementos:  ΣM(i,j)


'''
matriz=np.array([[0]*4]*3)

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
            matriz[f,c]=random.randint(1,30)
    return matriz
def suma_de_todo(matriz):
    sumas=0
    datos=matriz.shape
    filas=datos[0]
    columnas=datos[1]
    for f in range(filas):
        for c in range(columnas):
            sumas=sumas+matriz[f,c]
    return sumas



mostrar_matriz(matriz)
print()
carga_de_matriz_random(matriz)
print()
mostrar_matriz(matriz)
print(suma_de_todo(matriz))

