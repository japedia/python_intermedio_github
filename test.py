from clase9.register import agregar_usuario
import os
os.system('cls')

print("-------- INGRESE LO SIGUIENTE -----------")
usuario = input("Nombre de usuario: ")
contraseña = input("Contraseña: ")
correo = input("Correo electrónico: ")


# al registrarse retorne si se pudo o no registrar el usario
agregar_usuario(usuario,contraseña,correo)