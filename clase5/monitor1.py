#paq python 
#psutil
#https://psutil.readthedocs.io/en/latest/

import psutil
import os

cpu_nucleos = psutil.cpu_count()

cpu_frecuencia = psutil.cpu_freq()

cpu_memvirtual = psutil.virtual_memory()

disco_uso = psutil.disk_usage('/')


os.system('cls')
print("=" * 50)
print("System Information")
print("=" * 50)
print("Nucleos =>", cpu_nucleos)
print("Frecuencia => ",cpu_frecuencia)
print("Memoria Virtual => ",cpu_memvirtual)
print("Uso del disco => ",disco_uso)