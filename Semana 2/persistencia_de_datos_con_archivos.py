datos=[1,2,3,4,5]
with open("datos.txt", "w") as archivo:
    for numero in datos:
        archivo.write(str(numero)+"\n")

datosLeidos=[]
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        datosLeidos.append(int(linea))

print(datosLeidos)