import json
from os import system
from setting  import Settings
#{"id":1, isbn":"ghjkhg23476j6", "nombre":"nombreLibro", "cantidad":4}
libros=[]
idSec=1
tareasJson = Settings("libros.json")

def menu(libros):
    opc=""
    while opc!="6":
        print('''
            ---Menu---
            1.Insertar libro
            2.Listar libro
            3.Buscar Libro 
            4.Actualizar libro
            5.Eliminar libro
            6.Salir
            ''')
        opc=input("Elige una de las opciones: ")
        if opc=="1":
            isbn=input("ISBN: ")
            nombre=input("Nombre: ")
            cantidad=int(input("Cantidad: "))
            # insertarLibro(isbn, nombre, cantidad, libros)
            idSec = tareasJson.agregarLibro(isbn, nombre, cantidad) 
            print(f"Nuevo Registro {idSec} agregado!!")  
        elif opc=="2":
            listarLibros(libros)
        elif opc=="3":
             id = int(input("Ingrese el ID del libro a buscar: "))             
             buscarLibro(id)
        elif opc=="4":
            print("Actualizando libro... \nSi no desea actualizar libro")
            id=int(input("ID: "))
            isbn=input("isbn: ")
            nombre=input("nombre:" )
            cantidad=int(input("cantidad: "))
            result= tareasJson.actualizarLibro(id,isbn,nombre,cantidad)
            if result==0:
                print(f"El libro con ID {id} no existe")
            else:
                print("Actualizacion exitosa")
        elif opc=="5":
            print('Eliminando libros')
            id=int(input("ID: "))
            result=tareasJson.eliminarLibro(id)
        else:
            print("Gracias por Participar!!")
            break
# Proceso para insertar libros en la biblioteca
def insertarLibro(isbn, nombre, cantidad, libros):    
    # Se proceso agregar nuevos libros
    global idSec   
    idSec = tareasJson.agregarLibro(isbn, nombre, cantidad) 
    print(f"Nuevo Registro {idSec} agregado!!")        
    
def listarLibros(libros):
    librosJson = tareasJson.cargarLibros()
    if len(librosJson)!=0:
        for libro in librosJson:
            print("-----------------------")
            print("ID: ", libro["id"])
            print("ISBN: ", libro["isbn"])
            print("Nombre: ", libro["nombre"])
            print("Cantidad: ", libro["cantidad"])
            print("-----------------------")
    else:
        print("No hay libros para listar")
    input("Presione ENTER para continuar ")

def buscarLibro(id):
    librosJson = tareasJson.cargarLibros()
    libroEncontrado = False
    if len(librosJson)!=0:
        for libro in librosJson:
            if libro["id"] == id: 
                print("-----------------------")
                print("ID: ", libro["id"])
                print("ISBN: ", libro["isbn"])
                print("Nombre: ", libro["nombre"])
                print("Cantidad: ", libro["cantidad"])
                print("-----------------------")
                libroEncontrado = True
                break
        if libroEncontrado:
            print("Fin de la Busqueda ")    
        else:
            print("Libro no Encontrado")
    else:
        print("No hay libros para listar")
    input("Presione ENTER para continuar ")        

menu(libros)