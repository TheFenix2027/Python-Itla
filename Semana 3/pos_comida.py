menu=[{'id':1, 'nombre':'Arroz', 'precio':50},
    {'id':2, 'nombre':'Habichuela', 'precio':80},
    {'id':3, 'nombre':'Aceite', 'precio':300},
    {'id':4, 'nombre':'Pollo', 'precio':85},
    {'id':5, 'nombre':'Lechuga', 'precio':80}]

carrito=[]

def imprimir_menu(menu):
    tam_max = 0
    for item in menu:
        tam_actual = len(str(item['id']))+len(item['nombre'])+len(str(item['precio']))>tam_max
        if tam_actual>tam_max:
            tam_max=tam_actual
    print('-'*(int(tam_max/2+2))+'Menu'+'-'*(int(tam_max/2+2)))
    for item in menu:
        print(f"{item['id']}. {item['nombre']} -> RD${item['precio']}")

def imprimir_factura(carrito):
    tam_id=1
    tam_nombre=1
    tam_precio=1
    for item in menu:
        tam_idact=len(str(item['id']))
        tam_nombre_act=len(item['nombre'])
        tam_precio_act=len(str(item['precio']))
        if tam_idact>tam_id:
            tam_id=tam_idact
        if tam_nombre_act>tam_nombre:
            tam_nombre=tam_idact
        if tam_precio_act>tam_precio:
            tam_precio=tam_precio_act
    if tam_id-2<0:
        tam_id=1
    else:
        tam_id-=2
    if tam_nombre-6<0:
        tam_nombre=1
    else:
        tam_nombre-=6
    if tam_precio-6<0:
        tam_precio=1
    else:
        tam_precio-=6
    print('ID'+' '*(tam_id+2)+'Nombre'+' '*(tam_nombre+1)+'Precio'+' '*tam_precio)
    for item in carrito:
        print(str(item['id'])+' '*(tam_id+4-len(str(item['id'])))+item['nombre'].ljust(20)+' '*(tam_nombre+7-len(item['nombre']))+str(item['precio']))

imprimir_factura(menu)