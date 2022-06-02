from .connection import get_connection

def selecciona_user(id):
    conn, cur = get_connection()
    query = f"SELECT * FROM usuarios WHERE id={id}"
    cur.execute(query)
    encontrado =cur.fetchone()
    print(encontrado)
    #conn.commit()
    cur.close()
    conn.close()