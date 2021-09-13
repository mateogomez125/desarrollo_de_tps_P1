'''

4. Definir un array para contener 40 elementos.
a. Cargar el vector con 40 números entre -10 y 10
b. Mostrar por pantalla el vector.
c. Escribir una función que acepte como parámetro el vector y a cada número
negativo le sume 15 y reemplace el negativo por ese valor.
d. Mostrar por pantalla el vector modificado.
e. Escribir una función que reciba el vector anterior, sin negativos y que ante la
repetición de un número reemplace cada repetición por -1 (menos uno). El
procedimiento debe retornar el vector modificado y la cantidad de veces que
fue modificado.



'''
import random 
Elementos=[0]*40

def cargar_de_cosas(array):
    for i in range(len(array)):
        array[i]=random.randrange(-10,10)
def mostrar_vector(array):
    for i in range(len(array)):
        print(array[i])
def suma_15 (array):
    for i in range(len(array)):
        if array[i]<0:
            array[i]+=15

def repeticion_1(array):
    
    for i in range(len(array)):
        comparacion=array[i]
        veces_modificado=0
        for ii in range (len(array)):
            if comparacion==array[ii]:
                if array[ii]!=-1:
                    array[i]=-1
                    veces_modificado+=1
    maximo_modificado=veces_modificado
    return array,maximo_modificado




cargar_de_cosas(Elementos)
mostrar_vector(Elementos)
suma_15(Elementos)
print()
mostrar_vector(Elementos)
print(repeticion_1(Elementos))