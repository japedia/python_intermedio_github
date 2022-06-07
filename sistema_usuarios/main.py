import os

#os.system('cls')

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
    return

def menu1():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	#os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Ingresar")
	print ("\t2 - Registrar Usuario")
	print ("\t3 - Salir")
	print ("\t4 - otra opcion")

seleccion = False

while not seleccion:
	# Mostramos el menu
	menu1()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
    
    print(opcionMenu)

    if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		break
	else:
		print ("FALLÓ TODO")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")      