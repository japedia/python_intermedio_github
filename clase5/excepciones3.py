#Actividad de excepciones
#Replicar el comportamiento de creación de carpetas con el SO

#Crear unDirectorio, si ya existe agregarle entre parentesis el consecutivo
#carpeta
#carpeta(1)

import os

#contenido = os.listdir('C:\\Users\\Admin\\Documents\\GitHub\\python_intermedio_github')

#print(contenido)

repetida = False
while not repetida :
    i=1
    try:
        os.mkdir("Fotos")
        print("se creo la carpeta")
        break
    except FileExistsError as ex:
        os.mkdir("carpeta_prueba"{i})


def crear_carpetas(nombre_de_la_carpeta, consecutivo = 0):
    try:
        if consecutivo < 1:
            os.mkdir(nombre_de_la_carpeta)
        else:
            os.mkdir(nombre_de_la_carpeta + f'({consecutivo})')

    except FileExistsError as ex:
        crear_carpetas(nombre_de_la_carpeta, consecutivo + 1)


crear_carpetas("funcion_recursiva")

    
