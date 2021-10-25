#Escribir una función que reciba un arreglo de strings e indique si se encuentran
#ordenados de menor a mayor o no


array=['casa','perro','auto','bote','dado']
print(array)
def saber_si_esta_ordenado(array):
    salida=True
    respuesta=True
    contador=0
    while contador<((len(array))-1)and salida:
        salida=True
        if array[contador]>array[contador+1]:
                salida=False
                respuesta=False
        
        contador=contador+1
    return respuesta

def ordenar_string(array):
    for x in range(len(array)):
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                ax=array[i]
                array[i]=array[i+1]
                array[i+1]=ax
    return  array 
print(saber_si_esta_ordenado(array))
print(ordenar_string(array))      
print(saber_si_esta_ordenado(array))
