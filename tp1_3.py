import random

'''

3. Definir un array para contener 5000 elementos.
a. Cargar el array con 5000 edades (18 a 80) (random)
b. Realizar una función que indique cual es la edad de mayor frecuencia y su
frecuencia (la que más se repite y cuántas veces está).
'''

elementos=[0]*5000
def carga_randoms (array):
    for i in range (len(array)):
        array[i]= random.randrange(18,80)
def frecuencia(array):
    comparacion=0
    edad_de_mayor_frecuencia=0
    frecuencia=0
    Maximo_coincidenias=0
    for i in range(len(array)):
        comparacion= array[i]
        coincidencias=0
        for ii in range(len(array)):
            if comparacion==array[ii]:
                coincidencias+=1
                if coincidencias>Maximo_coincidenias:
                    edad_de_mayor_frecuencia=array[i]
                    frecuencia=coincidencias
    return edad_de_mayor_frecuencia, frecuencia

carga_randoms(elementos)
edad_mas_frecuente,Frecuencia=frecuencia(elementos)
print(f'la edad de mayor frecuencia es {edad_mas_frecuente} y en una frecuencia de {Frecuencia} cada 5000 edades')



   
            
            


