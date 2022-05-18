#Actividad de excepciones
#Replicar el comportamiento de creación de carpetas con el SO

#Crear unDirectorio, si ya existe agregarle entre parentesis el consecutivo
#carpeta
#carpeta(1)

import os

#contenido = os.listdir('C:\\python_intermedio_github')
#for archivo in contenido :
#    print(archivo)

#C:\python_intermedio_github

salir = False
i=0
folder = "Fotos"

while not salir :
    
    try:
        os.mkdir(folder)
        print("se creo la carpeta")
        i+=1
        print(i)
        
    except FileExistsError as ex:
        #folder = folder+"("+str(i)+")"
        os.mkdir(f'{folder}({i})')
        i+=1
        print(i)
            
    
    opcion = input("Crear mas copias? (s/n): ")
    
    if opcion=="n" :
        salir = True

