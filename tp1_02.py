'''
Dados dos arreglos ordenados: A(n) y B(m), 
construir un nuevo arreglo C que contenga los elementos de A y de B de tal forma que quede
también ordenado. Si existen elementos repetidos en los arreglos originales, en C deberán aparecer
solamente una vez.

'''
import random
n=6
m=5
arrayn=[0]*n
arraym=[0]*m
def carga_random (array):
    for i in range (len(array)):
        array[i]= random.randint(1,20)
    return array
def bubble_sort_Mam(vector):
    
    fin_del_orden=False
    while not(fin_del_orden):
        fin_del_orden=True
        for i in range(len(vector)-1):
            if vector[i]==vector[i+1]:
                vector[i+1]=0
                fin_del_orden=False


            if vector[i]<vector[i+1]:
                valor_a_guardar=vector[i+1]
                vector[i+1]=vector[i]
                vector[i]=valor_a_guardar
                fin_del_orden=False
            
    return vector
def Encadenado_de_arrays(array1,array2):
    array3=[0]*(len(array1)+len(array2))
    array3= array1+array2
    return array3

print(carga_random(arrayn))
print()
print(carga_random(arraym))
print()
print(bubble_sort_Mam(arraym))
print()
print(bubble_sort_Mam(arrayn))

array3=(Encadenado_de_arrays(arrayn,arraym))
print(array3)
print(bubble_sort_Mam(array3))



    
