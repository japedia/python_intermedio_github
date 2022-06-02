from .connection import get_connection

def delete_user(id):
    conn, cur = get_connection()
    query = f"DELETE FROM usuarios WHERE id={id}"
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()