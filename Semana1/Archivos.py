with open("ejemplo.txt", "r") as archivo:
    contenido=archivo.read()
    print(contenido)
archivo.close()

with open("ejemplo2.txt", "w") as archivo:
        archivo.write("Hola Mundo ")

with open("ejemplo2.txt", "a") as archivo:
    archivo.write("Bienvenidos a Python")
