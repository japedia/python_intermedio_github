from ast import Break
import psycopg2


print(
"""
+==================================+
| Inicio de sesion en el Metaverso    |
| Ingresa tu usuario y contraseña     |
| Por favor..............             |
+==================================+
""")
conn = psycopg2.connect("dbname=python_intermedio user=postgres password=12345")

user = input("usuario = ")
password = input("contraseña = ")

#Busca el usuario en la BD
cur=conn.cursor()

consulta = f"SELECT username, password FROM usuarios WHERE username=\'{user}\';"

print(consulta)

cur.execute(consulta)

usuario_pwd = cur.fetchone()

# Usuario de prueba: achristophe0
#Password de prueba: jHB27PBh0f

print(usuario_pwd)

if user == usuario_pwd[0] and password == usuario_pwd[1]:

    print(f"Bienvenido {usuario_pwd[0]}")

else:

    print("Usuario o contraseña incorrectos por favor intenta de nuevo")

    user = input("usuario = ")

    password = input("contraseña = ")

cur.close
conn.close