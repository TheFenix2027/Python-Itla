import csv

productos=[[1, "arroz", 43],[2, "habichuelas", 70],[3, "azucar", 40]]

with open("productos.csv", "w", newline="") as archivo:
    escritor=csv.writer(archivo)
    escritor.writerows(productos)

productosLeidos=[]
with open("productos.csv", "r") as archivo:
    lector=csv.reader(archivo)
    for fila in lector:
        productosLeidos.append([int(fila[0]),fila[1],float(fila[2])])
print(productosLeidos)