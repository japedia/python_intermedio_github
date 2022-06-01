from auth.login import is_authenticated
import os
os.system('cls')


#print(is_authenticated("usuari", "contrase"))
#print(is_authenticated("raughtonm", "rSIoQQYc"))

if is_authenticated("apydcock0", "N9RyghmCZIA"):
    print("bienvenido usuario")
else:
    print("credenciales incorrectas")


if  not is_authenticated("raughtonm", "rSIoQQYcx"):
    print("credenciales invalidas")