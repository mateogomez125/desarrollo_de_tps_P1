'''
Realizar un programa que permita ingresar las temperaturas mínimas y máximas correspondientes a los  30 días de un mes. Calcular y mostrar:
Promedio de temperaturas en el mes.
Día de máxima temperatura con su correspondiente temperatura.
Día de mínima temperatura con su correspondiente temperatura.
'''
import numpy as np
import random

temperaturas=np.array([[0]*30]*2)

def carga_de_temperaturas(matriz):
    temperatura_maxima_del_dia=0
    temperatura_minima_del_dia=0
    
    
    datos=matriz.shape
    filas=datos[0]
    columnas=datos[1]
    
    for c in range(columnas):
        temperatura_maxima_del_dia=random.randint(1,30)
        temperatura_minima_del_dia=random.randint(1,30)
        matriz[0,c]=temperatura_maxima_del_dia
        matriz[1,c]=temperatura_minima_del_dia
        
    
    return matriz
def sacar_promedios(matriz):
    datos=matriz.shape
    filas=datos[0]
    columnas=datos[1]
    max=0
    minima=0
    
    for f in range(filas):
        for c in range(columnas):
            if f<=0:
                max=matriz[f,c]+max
            elif f>0:
                minima=matriz[f,c]+minima
    promediom=minima//columnas
    promedioM=max//columnas
    promedios=[0]*2
    promedios[0]=promedioM
    promedios[1]=promediom
    
    return promedios
def mostrar_matriz(matriz):
    datos=matriz.shape
    filas=datos[0]
    columnas=datos[1]
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f,c],end=' ')
        print()
    pass
def busqueda_lineal(matriz):
    temperaturaM=0
    temperaturam=999999999
    dia_c=0
    dia_f=0
    datos=matriz.shape
    filas=datos[0]
    columnas=datos[1]
    Respuestas=[0]*4

    for f in range(filas):
        for c in range(columnas):
            if f<=0:
                if matriz[f,c]>temperaturaM:
                    temperaturaM=matriz[f,c]
                    dia_c=c
            elif f>0:
                if matriz[f,c]<temperaturam:
                    temperaturam=matriz[f,c]    
                    dia_f=c
    Respuestas[0]=dia_c
    Respuestas[1]=temperaturaM
    Respuestas[2]=dia_f
    Respuestas[3]=temperaturam
    return Respuestas



mostrar_matriz(temperaturas)
print()
carga_de_temperaturas(temperaturas)
print()
mostrar_matriz(temperaturas)
print()
print(sacar_promedios(temperaturas))
print()
respuestas=busqueda_lineal(temperaturas)

print(f'El dia mas caluroso fue el{respuestas[0]+1} con una temperatura de {respuestas[1]} grados ')
print(f'el dia mas frio fue el {respuestas[2]+1} con unas temperatura de {respuestas[3]} grados')