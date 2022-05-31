# TIENEN QUE HACER QUE CUANDO SE INTENTE 3 VECES LA contraseña
# MANDE UN MENSAJE DE NUMEROS DE INTENTO MAXIMOS ALCANZADOS
# Y SALIRSE DEL CLICO

from ast import Break
import psycopg2

#def logeo(usuario, contraseña) :


print(
"""
+==================================+
| Inicio de sesion en la MATRIX    |
| Ingresa tu usuario y tu          |
| contraseña por favor             |
+==================================+
""")
conn = psycopg2.connect("name=dbpython_intermedio user=postgres password=12345")

user = input("usuario = ")
password = input("contraseña = ")

#Busca el usuario en la BD
cur=conn.cursor()
consulta = f"SELECT username, password FROM usuarios WHERE username=\'{user}\';"

cur.execute(consulta)

usuario_pwd = cur.fetchone()

print(usuario_pwd)


#Hasta aqui la busqueda del usuario

# Usuario de prueba: apydcock0
#Password de prueba: N9RyghmCZIA

is_login = False
intentos = 1

while  not is_login and intentos < 3 : 

    if user == usuario_pwd[0] and password == usuario_pwd[1]:
        is_login = True
        print(f"Bienvenido {usuario_pwd[0]}")
        Break

    else:
        print("Usuario o contraseña incorrectos por favor intenta de nuevo")
        
        intentos = intentos + 1
        
        user = input("usuario = ")
        password = input("contraseña = ")

if intentos == 3 : print(f'\nUsuario o contraseña incorrectos número de intentos máximos alcanzados\n')

cur.close
conn.close