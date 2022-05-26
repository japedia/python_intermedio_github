archivo = open("texto.txt","w")

archivo.write("Hola\n")
archivo.write("mundo")

xlsx = open("libro.xlsx", 'w')
xlsx.close()

archivo.close()

print("End file managing")
