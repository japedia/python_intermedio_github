from .connection import get_connection

def modifica_user(id):
    conn, cur = get_connection()
    
    #Se ejecuta la modificación
    query = f"UPDATE usuarios SET email=\'micorreo.com\' WHERE id={id}"
    cur.execute(query)
    conn.commit()
        
    cur.close()
    conn.close()