import json
clientes=[{"id":1, "nombre":"David Tejada", "totalGastado":25000, "descuento":0.05},
        {"id":2, "nombre":"Willy Ortega", "totalGastado":20000, "descuento":0.05},
        {"id":3, "nombre":"Rayhan Nunez", "totalGastado":30000, "descuento":0.05}]

with open("cliente.json", "w") as archivo:
    json.dump(clientes, archivo, indent=4)

clientesLeidos=[]
with open("cliente.json", "r") as archivo:
    clientesLeidos=json.load(archivo)

print(clientesLeidos)