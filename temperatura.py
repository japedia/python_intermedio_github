#Mi primer code con Github
"""
Hacer un programa que te pida a cuantos grados centigrados estamos
Dependiendo el dato ingresado realizar las siguientes validaciones

si es mas de 35 grados mostrar: "ta juerte la calor"

si esta entre 25 a 30 grados mostrar: "se antoja un pozol"

si la temperatura es menor a 25 grados mostrar: "es hora de sacar el sueter cucarachiento"


utilizar el menor lineas de codigo posible

se evaluara:
legibilidad de codigo

"Simple es mejor que complejo"

-----------------------------------------
adjuntar el enlace de su repositorio en github
"""

temperatura = float(input("Introduzca la temperatura: \n"))

if temperatura > 35 :
    print("Ta juerte la calor")

elif temperatura in range(25,30) :
    print("Se antoja un pozol")

elif temperatura < 25 :
    print("es hora de sacar el sueter cucarachiento")

else:
    print("valor no considerado")