from urllib import response
import requests
import os

os.system('cls')

respuesta = requests.get("https://jsonplaceholder.typicode.com/posts/1")

resp_diccionario = respuesta.json()

"""
print("*" * 50)
print(respuesta.text)
print(type(respuesta.text))
print("\n")

print(respuesta.json)
#print(type(respuesta))
"""