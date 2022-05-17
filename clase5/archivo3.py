#ejemplo de lectura de files

with open("texto2.txt") as archivo:
    print(archivo.read())


#leer archivos multilinea

with open("texto.txt") as archivo:
    print(archivo.readline())
    print(archivo.readline())


print("=" * 50)

with open("carpetas.txt") as archivo:
    for linea in archivo.readlines():
        print(linea)

