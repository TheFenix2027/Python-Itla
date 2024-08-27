from os import system
system("cls")

# Creando el Diccionario con los Datos
productos = {'1': {'prod': 'Refresco', 'cant': 50, 'prec': 50, 'itb':18},
             '2': {'prod': 'Repollo', 'cant': 50, 'prec': 80, 'itb':18},
             '3': {'prod': 'Vinagre', 'cant': 50, 'prec': 300, 'itb':18},
             '4': {'prod': 'Cerdo', 'cant':50, 'prec': 85, 'itb':18},
             '5': {'prod': 'Remolacha', 'cant':50, 'prec': 80, 'itb':18}
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
        print(f"ID: {item} - Producto: {producto['prod']} - Cantidad: {producto['cant']} - Precio: RD${producto['prec']} - Itebis: {producto['itb']}")
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

def fImprimirFactura(pcarrito, pprodocutos):
    vsubTotal = 0
    vImpuestos = 0
    vTotal = 0
    vItebis = .18
    
    # Trabajando con el ancho de las columnas
    anchoId = 5
    anchoProducto = 15
    anchoPrecioUnidad = 15
    anchoCantidad = 10
    anchoPrecioTotal = 15
    anchoCliente = 10
    anchoIdCliente = 4
    anchoTotal = anchoId + anchoProducto + anchoPrecioUnidad + anchoCantidad + anchoPrecioTotal + anchoCliente + anchoIdCliente
    #
    print("Productos Facturados en la Tienda")
    print("Cliente: " + datosCliente)
    print("ID: " + idCliente)
    print("-" * anchoTotal)
    print(
        "ID".ljust(anchoId) +
        "Producto".ljust(anchoProducto) +
        "Precio Unidad".ljust(anchoPrecioUnidad) +
        "Cantidad".ljust(anchoCantidad) +
        "Precio Total".ljust(anchoPrecioTotal)
)

    # Línea separadora
    print("-" * anchoTotal)

    for x in pcarrito:
        for y in pprodocutos:
            if str(x) == y:
                cantidadCompra = pcarrito[x]        
                producto = pprodocutos[y]
                print(str(x).ljust(anchoId) + str(producto['prod']).ljust(anchoProducto) + ("RD$" + str(producto['prec'])).ljust(anchoPrecioUnidad) + str(cantidadCompra).ljust(anchoCantidad) + ("RD$"+str(producto['prec'] * cantidadCompra)).ljust(anchoPrecioTotal))
                vsubTotal = vsubTotal + producto['prec'] * cantidadCompra
    
    if vsubTotal > 0:
        vImpuestos = vsubTotal * vItebis
        vTotal = vsubTotal + vImpuestos
        print((f"SubTotal      : RD$%.2f" % vsubTotal).rjust(anchoTotal))
        print((f"Impuestos     : RD$%.2f" % vImpuestos).rjust(anchoTotal))
        print((f"Total a Pagar : RD$%.2f" % vTotal).rjust(anchoTotal))
    print("-" * anchoTotal)

# Creando Menu
while True:
    # system("cls")
    print("Punto de Venta Surtidora ITLA Santiago SRL")
    fImprimirLists(productos)  
    print("0- Para Salir | 1- Buscar Productos | 2- Imprimir Factura")
    condition = int(input("Ingresar la Opcion a Trabajar: "))  
    if condition == 0:   
        print("Gracias por Su Compra!!!") 
        break
    elif condition == 1:
        while True:
            id = int(input("Ingresar el ID del Producto a Comprar: "))  
            # Buscar Productos
            vresultado = fBuscarLists(productos, id)
            if vresultado == True:      
                    cantidad = -1
                    while cantidad < 0:
                        cantidad = int(input("Ingresar la cantidad que desea del producto elegido (debe ser mayor que 1): "))    
                        if cantidad > 0:
                            if id in carrito:
                                print(f"Articulo ya se encuentra en el carrito, se sumara la cantidad indicada")
                                carrito[id] = carrito[id] + cantidad
                            else:
                                carrito[id] = cantidad  
                    # Imprimiendo reultados
                    print(f"Cantidad a comprar {cantidad}")
                    # print(f"Articulos registrados {carrito}")
            else:
                print("El producto indicado no esta en el sistema")
                #  ---------------------------------------------
            continuar = input("Desea Continuar Agregando Articulos S/N : ")
            if continuar.upper() == "N":
                teclado = input("Enter para continuar")
                system("cls")
                break
    elif condition == 2:
        if len(carrito) == 0:
            print(f"El Carrito de Compra esta vacio {len(carrito)}, debe comprar elementos en la tienda")
            teclado = input("Enter para continuar")
            system("cls")
        else:
                datosCliente = input("Ingrese su nombre: ")
                idCliente = input("Ingrese su ID: ")
                fImprimirFactura(carrito, productos)
                teclado = input("Enter para continuar")
                system("cls")   
    else:
        print("Opcion de Menu Incorrecta")
        teclado = input("Enter para volver al menu principal") 