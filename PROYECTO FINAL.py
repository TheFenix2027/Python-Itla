from os import system
import json
from datetime import datetime

juegos = []
idSec = 1
carrito = {}

login = [[1, "david", "123"], [1, "willy", "456"]]

# print(f"Matriz {login[0][1]}")

def menu(juegos):
    opc = ""
    while opc != "5":
        print(
            """
            ---Menu---
            1.Insertar juegos
            2.Listar juegos
            3.Actualizar juegos
            4.Eliminar juegos
            5.Salir
            """
        )
        opc = input("Elige una de las opciones: ")
        if opc == "1":
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = int(input("Precio: "))
            insertar_juegos( nombre, cantidad, juegos, precio)
        elif opc == "2":
            listar_juegos(juegos)
        elif opc == "3":
            print("Actualizando juegos... \nSi no desea actualizar juegos")
            id = input("ID: ")
            nombre = input("nombre:")
            cantidad = input("cantidad: ")
            precio=input("precio: ")
            result = actualizar_juegos(id, nombre, cantidad, precio)
            if result == 0:
                print("El juegos no existe")
            else:
                print("Actualizacion exitosa")
        elif opc == "4":
            print("Eliminando juego")
            id = input("ID: ")
            result = eliminar_juego(id, juegos)

def insertar_juegos(nombre, cantidad, juegos, precio):
    global idSec
    idSec+=1
    juegos.append({"id":idSec, "nombre":nombre, "cantidad":cantidad, "precio":precio})
    # Aregando nuevos juegos al archivo json
    with open("juegos.json", "w") as archivo:
        json.dump(juegos, archivo, indent=4)

def listar_juegos(juegos):
    if len(juegos)!=0:
        for juego in juegos:
            print("-----------------------")
            print("ID: ", juego["id"])
            print("Nombre: ", juego["nombre"])
            print("Cantidad: ", juego["cantidad"])
            print("Precio: ", juego["precio"])
            print("-----------------------")
    else:
        print("No hay juegos para listar")
    input("Presione ENTER para continuar ")
    system("cls")

def actualizar_juegos(id, nombre, cantidad, precio):
    juego=buscar_juegos(id, juegos)
    if juego!=None:
        if nombre!="":
            juego["nombre"]=nombre
        if cantidad!="":
            juego["cantidad"]=int(cantidad)
        if precio!="":
            juego["precio"]=int(precio)
    else:
        return 0

def buscar_juegos(id, juegos):
    for juego in juegos:
        if juego["id"]==int(id):
            return juego
        return None

def eliminar_juego(id, juegos):
    juego=buscar_juegos(id,juegos)
    if juego!=None:
        juegos.remove(juego)
        return 1 #Eliminacion exitosa
    else:
        return 0 

def guardar_juegos(juegos):
    with open("juegos.json", "w") as archivo:
        json.dump(juegos, archivo, indent=4)

def abrir_juegos(juegos):
    with open("juegos.json", "r") as archivo:
        juegos=json.load(archivo)

def administrador(login):
    for row in login:
        usuario = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        if (
            usuario == login[0][1]
            and password == login[0][2]
            or usuario == login[1][1]
            and password == login[1][2]
        ):
            print("Usuario y contraseña correctos")
            print(menu(juegos))
        else:
            print("Acceso denegado")
        break
administrador(login)