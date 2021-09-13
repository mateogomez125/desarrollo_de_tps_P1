'''
1. Definir un vector que pueda contener 250 elementos.
a. Cargar el vector con 250 números enteros entre -100 y 100.(utilizar random).
b. Calcular la cantidad de números negativos, positivos y ceros que se
encuentran en el vector.
c. Mostrar por pantalla la información anterior, fuera de la función.
d. Realizar un programa que encuentre el mayor de los valores cargados en el
problema anterior.
e. Mostrar por pantalla la información anterior, fuera de la función.
f. Mostrar los elementos que ocupan las posiciones impares del vector y su
suma dentro de la misma función
'''
import random
array= [0]*250 

#funcion de carga random 
def carga_random (array,carga):
    for i in range (carga):
        array[i]= random.randint(-100,100)
#funcion de busqueda de numeros
def busqueda_de_numeros(array,amplitud):
    numeros_negativos=0
    numero_positivos=0
    cantidad_de_0=0
    for i in range(amplitud):
        if array[i]<0:
            numeros_negativos+=1
        elif array[i]>0:
            numero_positivos+=1
        elif array[i]==0:
            cantidad_de_0+=1    
    return numero_positivos,numeros_negativos,cantidad_de_0
#funcion para encontrar el mayor
def busqueda_del_mayor(array,amplitud):
    el_mayor=-10000000000
    for i in range(amplitud):
        
        if array[i]>el_mayor:
            el_mayor=array[i]
    return el_mayor
#funcion de muestra y suma de posiciones impares 
def busqueda_y_suma(array,amplitud):
    suma=0
    print('Elementos:')
    for i in range(amplitud):
        if array[i]%2==1:
            print(array[i])
            suma+=array[i]
    print(f'Resultado de la suma:{suma}')


#programa principal 
carga_random(array,250)
print(f'La cantidad de numeros (positivos,negativos, ceros)dentro del array: {busqueda_de_numeros(array,250)}')
print(f'El numero mas grande del array es: {busqueda_del_mayor(array,250)}')
busqueda_y_suma(array,250)
