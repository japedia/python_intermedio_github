from clase8.auth.register import register_user
import os
os.system('cls')

print("-------- INGRESE LO SIGUIENTE -----------")
usuario = input("Nombre de usuario: ")
contraseña = input("Contraseña: ")
correo = input("Correo electrónico: ")


# al registrarse retorne si se pudo o no registrar el usario
register_user(usuario,contraseña,correo)