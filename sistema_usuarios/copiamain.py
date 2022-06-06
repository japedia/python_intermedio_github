import os
os.system('cls')

def valid():
    while True:
        non_alfanum = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
                       '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\ ', ']', '^',
                       '_', '`', '{', '|', '}', '~', '"']
        a = input("ingrese nombre de usuario: ")
        if len(a) < 6:
            print("El nombre de usuario debe contener al menos 6 caracteres")
        elif len(a) > 12:
            print("El nombre de usuario no puede contener más de 12 caracteres")
        elif set(non_alfanum).intersection(a):
            print("El nombre de usuario puede contener solo letras y números")
        else:
            print("usuario correcto.")
            break



def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Ingresar")
	print ("\t2 - Registrar Usuario")
	print ("\t3 - Salir")
    print ("\t4 - Otra opción")
	
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

print("el usuario no debe tener mas de 12 caracteres, "
        "ni menos de 6, debe poseer solo letras y numeros.")



#menú1
mensaje = """
Bienvenid@ al sistema CRUD de usuarios
Selecciona una opcion
1 - Login
2 - Registro
3 - Salir
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
3 - Salir
-> """
opcion = input(mensaje)

mensaje = "Para iniciar sesion ingreas tu usuario y contraseña"
print(mensaje)

usuario = input("Usuario: ")
password = input("Contraseña: ")


#menú2
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

#menú2
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