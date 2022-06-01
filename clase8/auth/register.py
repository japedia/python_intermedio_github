from .connection import get_connection

def register_user(usuario, contraseña,correoe):
    conn, cur = get_connection()

    consulta = f"INSERT INTO usuarios (id,username,password,email,estatus) VALUES (101,\'{usuario}\',\'{contraseña}\',\'{correoe}\',1) ;"
    print(consulta)

    cur.execute(consulta)
    conn.commit()
    
    print("Registro guardado con éxito...")

    conn.close
    cur.close
