import os
os.system('cls')

mensaje = """
Bienvenid@ al sistema CRUD de usuarios
Selecciona una opcion
1 - Login
2 - Registro
-> """ 

opcion = input(mensaje)

mensaje = """
Par registrar un usuario necesistas proporcionar
- Nombre de usuario
- Contraseña
- Correo electronico
"""

print(mensaje)

usuario = input("Usuario: ")
password = input("Contraseña: ")
email = input("Email: ")

mensaje = "\nRegistrando el usuario, espere por favor..."
print(mensaje)

mensaje = f"\nUsuario {usuario} registrado con exito"
print(mensaje)

mensaje= """
1 - Login
2 - Registro
-> """
opcion = input(mensaje)

mensaje = "Para iniciar sesion ingreas tu usuario y contraseña"
print(mensaje)

usuario = input("Usuario: ")
password = input("Contraseña: ")

mensaje = f"""\nBienvid@ {usuario} al CRUD de usuarios elige una opcion
1- Mostrar informacion del usuario
2- Modificar usuario
3- Borrar usuario
"""
print(mensaje)

opcion = input("->")

mensaje = """\nTu informacion es la siguiente:
Usuario: tavo
Contraseña: 1234
Email: tavo@tavo.com
Status: Activo
"""

print(mensaje)

mensaje = """
1- Mostrar informacion del usuario
2- Modificar usuario
3- Borrar usuario
"""
print(mensaje)

opcion = input("->")

mensaje= """
Elige un dato a modicar 
1- Usuario
2- Contraseña
3- Email
4- Status
"""
print(mensaje)

opcion = input("->")

opcion = input("Ingresa el nuevo valor para USUARIO: ")


# ejemplo de funciones

# funcion tradicional
def login(username, password):
    pass


# parametro opcional
def login(username, password, email=None):
    pass

# N parametros
def register(**kwargs):
    username = kwargs['username']

# N parametros
def register(*args, **kwargs):
    username = kwargs['username']

# formas de invocar una funcion |  argumentos posicionales
login("tavo", "1234")

# formas de invocar una funcion |  argumentos clave o nombrados
login(password="124", username="asdasd")

# formas de invocar una funcion |  argumentos variables
register(username="tavo", password="123", email="algo@algo.com")

register(1, username="tavo", password="123", email="algo@algo.com")