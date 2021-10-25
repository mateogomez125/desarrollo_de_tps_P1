def bubble_sort_Mam(vector):
    
    fin_del_orden=False
    while not(fin_del_orden):
        fin_del_orden=True
        for i in range(len(vector)-1):
            
            if vector[i]<vector[i+1]:
                valor_a_guardar=vector[i+1]
                vector[i+1]=vector[i]
                vector[i]=valor_a_guardar
                fin_del_orden=False


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

