#Ejemplo nde conexion a base de datos
#utilizando psycopg2

import psycopg2

conn = psycopg2.connect("dbname=dbpython_intermedio user=postgres password=12345")
print("conectado")
cur=conn.cursor()

cur.execute("SELECT * FROM usuarios WHERE id=50;")

print(cur.fetchone())

cur.close
conn.close