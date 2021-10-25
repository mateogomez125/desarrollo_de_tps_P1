'''
Se tienen 3 arreglos que guardan Descripción(DP), Precio Unitario (PU) y Cantidad Comprada (CC) de n productos. Se pide:
Crear un arreglo (TG)con el total gastado en compras  por cada producto (TG=PU X CC).
Calcular el total general de la compra.
Ordenar el arreglo obtenido de menor a mayor.
Mostrar Descripción y Monto Total del producto que obtuvo mayor gasto.
 '''



dp=[0]*3
pu=[0]*3
cc=[0]*3
tg=[0]*3
dp=['carne','papa','harina']
pu=[100,20,12]
cc=[10,20,15]
total=0

for i in range(3):
    tg[i]=cc[i]*pu[i]
    total=tg[i]+total


def bubble_sort_maM(vector):
    
    fin_del_orden=False
    while not(fin_del_orden):
        fin_del_orden=True
        for i in range(len(vector)-1):
            
            if vector[i]>vector[i+1]:
                valor_a_guardar=vector[i]
                vector[i]=vector[i+1]
                vector[i+1]=valor_a_guardar
                fin_del_orden=False

bubble_sort_maM(tg)
mayor=tg[(len(tg)-1)]
print(mayor)
print(tg)
print(f'eltotal de la compra es {total}')
