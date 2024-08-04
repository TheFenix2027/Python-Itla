import json
from os import system

class Settings():
    
  # defini variables de la clase
  def __init__(self, archivo):
        self.archivo = archivo

  # Funcion para carga los libros almacenados
  def cargarLibros(self):
      try:
          with open("libros.json", "r") as archivo:
              libros = json.load(archivo)
      except FileNotFoundError:
          libros = []      
      return libros
  
  # Funcio Guardar Libros
  def guardarLibros(self, libros):
        with open(self.archivo, "w") as archivo:
            json.dump(libros, archivo, indent=4)

  # Función para obtener el siguiente valor de idSec
  def obtenerSiguienteId(self):
      libros = self.cargarLibros()
      if not libros:
          return 1
      ultimo_libro = libros[-1]
      return ultimo_libro["id"] + 1
  
  # Función para AgregrLibros
  def agregarLibro(self, isbn, nombre, cantidad):
        libros = self.cargarLibros()
        idSec = self.obtenerSiguienteId()
        libros.append({"id": idSec, "isbn": isbn, "nombre": nombre, "cantidad": cantidad})
        self.guardarLibros(libros)
        return idSec
  
  # ActualizarLibro
  def actualizarLibro(self, idSec, isbn, nombre, cantidad):
        libros = self.cargarLibros()
        libroEncontrado = False
        # print(f"Libros antes de la actualización: {libros}")
        for libro in libros:
            if libro["id"] == idSec:
                # print(f"Libro encontrado: {libro['nombre']} (ID: {libro['id']})")
                libro["isbn"] = isbn
                libro["nombre"] = nombre
                libro["cantidad"] = cantidad
                libroEncontrado = True
                break
        # print(libroEncontrado)
        if libroEncontrado:
          self.guardarLibros(libros)
          print(f"Libro con ID: {idSec} actualizado exitosamente.")
          return 1
        else:
          print(f"No se encontró un libro con ID: {idSec}")                  
          return 0
  
  # Proceso de Eliminar Registro
  def eliminarLibro(self, idSec):
        libros = self.cargarLibros()
        libroEncontrado = False
        librosActualizados = []
        for libro in libros:
            if libro["id"] != idSec:
                librosActualizados.append(libro)
            else:
                libroEncontrado = True
        if libroEncontrado:
            self.guardarLibros(librosActualizados)
            print(f"Libro con ID: {idSec} eliminado exitosamente.")
            return 1
        else:
            print(f"No se encontró un libro con ID: {idSec}")
            return 0
        