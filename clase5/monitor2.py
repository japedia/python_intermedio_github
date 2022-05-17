# pasar todo lo del monitor 1 a un archivo de texto
# crear una carpeta donde se almacenaran los logs 
# crear un archivo con X nombre 
# insertar la informacion recabada en el archivo
import psutil
import os

#get information
cpu_nucleos = psutil.cpu_count()
cpu_frecuencia = psutil.cpu_freq()
cpu_memvirtual = psutil.virtual_memory()
disco_uso = psutil.disk_usage('/')


os.system('cls')
print("=" * 50)

os.mkdir("LOGS_SYSTEM")

#create file and write
with open("LOGS_SYSTEM\monitor2.txt","w") as archivo:
    archivo.write(f"Nucleos del CPU : {cpu_nucleos}\n")
    archivo.write(f"Frecuencia del CPU : {cpu_frecuencia}\n")
    archivo.write(f"Memoria Virtual : {cpu_memvirtual}\n")
    archivo.write(f"Uso del Disco Duro : {disco_uso}\n")