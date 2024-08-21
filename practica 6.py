from os import system
system("cls")

# Creando el Diccionario con los Datos
productos = {'1': {'prod': 'Arroz', 'prec': 50},
             '2': {'prod': 'Habichuela', 'prec': 80},
             '3': {'prod': 'Aceite', 'prec': 300},
             '4': {'prod': 'Pollo', 'prec': 85},
             '5': {'prod': 'Lechuga', 'prec': 80}
             }
# carrito de compra
carrito = {}

def imprimir_menu(menu):
    tammax=0
    for item in menu:
        tamactual=len(str(item['id']))+len(item['nombre'])+len(str(item['precio']))
        if  tamactual>tammax:
            tammax=tamactual
    print('-'*(int(tammax/2+2))+'Menú'+'-'*(int(tammax/2+2)))
    for item in menu:
        print(f"{item['id']}. {item['nombre']} -> RD${item['precio']}")

def imprimirfactura(carrito):
    tamid=1
    tamnombre=1
    tamprecio=1
    for item in carrito:
        tamidact=len(str(item['id']))
        tamnombreact=len(item['nombre'])
        tamprecioact=len(str(item['precio']))
        if tamidact>tamid:
            tamid=tamidact
        if tamnombreact>tamnombre:
            tamnombre=tamnombreact
        if tamprecioact>tamprecio:
            tamprecio=tamprecioact
    if tamid-2<0:
        tamid=1
    else:
        tamid-=2
    if tamnombre-6<0:
        tamnombre=1
    else:
        tamnombre-=6
    if tamprecio-6<0:
        tamprecio=1
    else:
        tamprecio-=6
    print('ID'+' '*(tamid+2)+'Nombre'+' '*(tamnombre+1)+'Precio'+' '*(tamprecio))
    for item in carrito:
        print(str(item['id'])+' '*(tamid+4-len(str(item['id'])))+item['nombre']+' '*(tamnombre+7-len(item['nombre']))+str(item['precio']))

def fImprimirLists(pprodocutos):
    print("Productos Existentes en la Tienda")
    print("----------------------------------")
    for item in pprodocutos:
        producto = pprodocutos[item] 
        print(f"ID: {item} - Producto: {producto['prod']} - Precio: RD${producto['prec']}")
    print("----------------------------------")

def fBuscarLists(pprodocutos, id):
    resultado = False
    print("Productos Existentes en la Tienda")
    print("----------------------------------")
    for item in pprodocutos:    
        if str(id) == item:
            producto = pprodocutos[item] 
            print(f"Producto con ID: {id} encontrado")    
            print(f"Producto: {producto['prod']} - Precio: RD${producto['prec']}")   
            resultado = True
    print("----------------------------------")  
    return(resultado)   
