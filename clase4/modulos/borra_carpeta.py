import os

micarpeta = "C:\python_intermedio_github\prueba_carpeta0"

## If file exists, delete it ##
if os.path.isfile(micarpeta):
    os.remove(micarpeta)
else:    ## Show an error ##
    print("Error: %s file not found" % micarpeta)