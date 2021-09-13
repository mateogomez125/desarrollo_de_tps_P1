'''
2. Definir un array para contener 10 elementos.
a. Cargar el array con los apellidos de 10 alumnos.
b. Escribir una función que reciba el vector y un apellido ingresado por teclado y
retorne True si se encuentra en el vector y False en caso contrario.
c. Mostrar por pantalla la información indicando si el apellido está o no dentro
del vector
'''
alumnos=[0]*10

def carga_de_alumnos(array):
    for i in range (10):
        array[i]= input('ingrese el apellido del alumno: ')
def busqueda_de_apellido(array,apellido):
    respuesta=False
    for i in range(len(array)):
        if array[i]==apellido:
            respuesta=True
        
    return respuesta


carga_de_alumnos(alumnos)
apellido= input('ingrese el apellido a buscar: ')
busqueda_de_apellido(alumnos,apellido)
if busqueda_de_apellido(alumnos,apellido):
    print('El alumno esta en la lista')
else: 
    print('El alumno no esta en la lista')






