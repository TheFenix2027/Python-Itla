import os 

menu=[{'id':1, 'nombre':'Arroz', 'precio':50},
    {'id':2, 'nombre':'Habichuelas', 'precio':80},
    {'id':3, 'nombre':'Aceite', 'precio':300},
    {'id':4, 'nombre':'Pollo', 'precio':85},
    {'id':5, 'nombre':'Lechuga', 'precio':80},]

carrito=[]

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

# LImpiar pantalla
os.system("cls")
imprimirfactura(menu)

#trabajando con menu de opciones
while True:
    print(f"Opciones del Menu")
    print(f"1- Buscar Productos")
    print(f"0- Para Salir del Sistema")
    vTarea = int(input("Ingresa la Opcion a Trabajar: "))
    if vTarea == 0:
        print("Gracias por Utilizar Nuestros Servicios")
        break
    elif vTarea == 1:
        print("Vamos a buscar un producto")
    else:    
        print("Opcion no registrada, intente de nuevo")