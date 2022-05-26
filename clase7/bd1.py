#Ejemplo nde conexion a base de datos
#utilizando psycopg2

import psycopg2

conn = psycopg2.connect("dbname=python_intermedio user=postgres password=12345")
cur=conn.cursor()

cur.execute("SELECT * FROM usuarios WHERE id=50;")

print(cur.fetchone())

cur.close
conn.close