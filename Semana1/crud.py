import json
import os
#{"id":1, isbn":"ghjkhg23476j6", "nombre":"nombreLibro", "cantidad":4}
libros=[]
idSec=1

def menu(libros):
    opc=""
    while opc!="5":
        print('''
            ---Menu---
            1.Insertar libro
            2.Listar libro
            3.Actualizar libro
            4.Eliminar libro
            5.Sair
            ''')
        opc=input("Elige una de las opciones: ")
        if opc=="1":
            isbn=input("ISBN: ")
            nombre=input("Nombre: ")
            cantidad=int(input("Cantidad: "))
            insertarLibro(isbn, nombre, cantidad, libros)
        elif opc=="2":
            listarLibros(libros)
        elif opc=="3":
            print("Actualizando libro... \nSi no desea actualizar libro")
            id=input("ID: ")
            isbn=input("isbn: ")
            nombre=input("nombre:" )
            cantidad=("cantidad: ")
            result=actualizarLibro(id,isbn,nombre,cantidad)
            if result==0:
                print("El libro no existe")
            else:
                print("Actualizacion exitosa")
        elif opc=="4":
            print('Eliminando libros')
            id=input("ID: ")
            result=eliminarLibro(id, libros)

def insertarLibro(isbn, nombre, cantidad, libros):
    global idSec
    idSec+=1
    libros.append({"id":idSec, "isbn":isbn, "nombre":nombre, "cantidad":cantidad})


def listarLibros(libros):
    if len(libros)!=0:
        for libro in libros:
            print("-----------------------")
            print("ID: ", libro["id"])
            print("ISBN: ", libro["isbn"])
            print("Nombre: ", libro["nombre"])
            print("Cantidad: ", libro["cantidad"])
            print("-----------------------")
    else:
        print("No hay libros para listar")
    input("Presione ENTER para continuar")

def actualizarLibro(id, isbn, nombre, cantidad):
    libro=buscarLibro(id, libros)
    if libro!=None:
        if isbn!="":
            libro["isbn"]=isbn
        if nombre!="":
            libro["nombre"]=nombre
        if cantidad!="":
            libro["cantidad"]=int(cantidad)
    else:
        return 0

def buscarLibro(id, libros):
    for libro in libros:
        if libro["id"]==int(id):
            return libro
        return None

def eliminarLibro(id, libros):
    libro=buscarLibro(id,libros)
    if libro!=None:
        libros.remove(libro)
        return 1 #Eliminacion exitosa
    else:
        return 0 

def fuardarLibros(libros):
    with open("libros.json", "w"):
        json.dump(libros, archivo, indent=4)

with open("libros.json", "r") as archivo:
    libros=json.load(archivo)
menu(libros)