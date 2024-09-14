from os import system
import json
from datetime import datetime

juegos = []
idSec = 1

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
            5.Sair
            """
        )
        opc = input("Elige una de las opciones: ")
        if opc == "1":
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            insertar_juegos( nombre, cantidad, juegos)
        elif opc == "2":
            listar_juegos(juegos)
        elif opc == "3":
            print("Actualizando juegos... \nSi no desea actualizar juegos")
            id = input("ID: ")
            nombre = input("nombre:")
            cantidad = "cantidad: "
            result = actualizar_juegos(id, nombre, cantidad)
            if result == 0:
                print("El juegos no existe")
            else:
                print("Actualizacion exitosa")
        elif opc == "4":
            print("Eliminando juego")
            id = input("ID: ")
            result = eliminar_juego(id, juegos)

def insertar_juegos(nombre, cantidad, juegos):
    global idSec
    idSec+=1
    juegos.append({"id":idSec, "nombre":nombre, "cantidad":cantidad})
    # Aregando nuevos juegos al archivo json
    with open("libros.json", "w") as archivo:
        json.dump(juegos, archivo, indent=4)

def listar_juegos(juegos):
    if len(juegos)!=0:
        for juego in juegos:
            print("-----------------------")
            print("ID: ", juego["id"])
            print("Nombre: ", juego["nombre"])
            print("Cantidad: ", juego["cantidad"])
            print("-----------------------")
    else:
        print("No hay juegos para listar")
    input("Presione ENTER para continuar ")
    system("cls")

def actualizar_juegos(id, nombre, cantidad):
    juego=buscar_juego(id, juegos)
    if juego!=None:
        if nombre!="":
            juego["nombre"]=nombre
        if cantidad!="":
            juego["cantidad"]=int(cantidad)
    else:
        return 0

def buscar_juego(id, juegos):
    for juego in juegos:
        if juego["id"]==int(id):
            return juego
        return None

def eliminar_juego(id, juegos):
    juego=buscar_juego(id,juegos)
    if juego!=None:
        juegos.remove(juego)
        return 1 #Eliminacion exitosa
    else:
        return 0 

def guardar_juegos(libros):
    with open("libros.json", "w") as archivo:
        json.dump(libros, archivo, indent=4)

def abrir_juegos(juegos):
    with open("juegos.json", "r") as archivo:
        juegos=json.load(archivo)

for row in login:
    usuario = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    if (
        usuario == login[0][1]
        and password == login[0][2]
        or usuario == login[1][1]
        and password == login[1][2]
    ):
        print("Usuario correcto y contraseña correctos")
        print(menu(juegos))
    else:
        print("Acceso denegado")
    break