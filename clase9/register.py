from ..clase8.auth.connection import get_connection

def agregar_usuario(usuario, contraseña,correoe):
    conn, cur = get_connection()

    consulta = f"INSERT INTO usuarios (id,username,password,email,estatus) VALUES (102,\'{usuario}\',\'{contraseña}\',\'{correoe}\',1) ;"
    #print(consulta)

    cur.execute(consulta)
    conn.commit()
    
    print("Registro guardado con éxito...")

    conn.close
    cur.close
