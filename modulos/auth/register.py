# Modulo registro de usuarios clase 9 - 01-06-2022
from .connection import get_connection


def register_user(username, password, email, status=None):
    conn, cur = get_connection()
    """
    Maneras de concatenar cadenas
    query = "INSERT INTO public.usuarios(username, password, email, status)VALUES ({}, {}, {}, {}, {});".format(
        username, password, email, status
    )
    query = "INSERT INTO public.usuarios(username, password, email, status)VALUES ('"+ username+"','"+password+"','', '', '');"
    query = "INSERT INTO public.usuarios(username, password, email, status)VALUES ('%s','%s','%s','%i');" % (password, username, email, status)
    """
    query = f"INSERT INTO public.usuarios(username, password, email, status)VALUES ('{username}', '{password}', '{email}', {status});"
     
    #cur.execute("SELECT * FROM usuaruis WHERE id=%s",(1))
    result = cur.execute(query)
    print(result)
    conn.commit()

    cur.close()
    conn.close()