#Actividad de excepciones
#Replicar el comportamiento de creación de carpetas con el SO

#Crear unDirectorio, si ya existe agregarle entre parentesis el consecutivo
#carpeta
#carpeta(1)

import os

contenido = os.listdir('C:\\python_intermedio_github')
for archivo in contenido :
    print(archivo)

#C:\python_intermedio_github
"""
salir = False
i=1

while not salir :
    
    try:
        os.mkdir("Fotos")
        print("se creo la carpeta")
        
    except FileExistsError as ex:
        os.mkdir("Fotos("+str(i)+")")
        i+=1
            
    
    opcion = input("Crear mas copias? (s/n): ")
    
    if opcion=="n" :
        salir = True
"""
