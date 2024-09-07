class Almacenes:
    altura = 0
    anchura = 0
    largura = 0
    id = 0
    nombre = "Default"
    def __init__(self, altura, anchura, largura, id, nombre):
        self.altura = altura
        self.anchura = anchura
        self.largura = largura
        self.id = id
        self.nombre = nombre

class Empleado:
    nombre = "Default"
    apellido = "Defaut"
    edad = 0
    identificacion = 0
    def __init__(self,nombre,edad,apellido,identificacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.identificacion = identificacion

almacen_A = Almacenes(2.40, 2.36, 4.42, 123, "Almacen A")
almacen_B = Almacenes(2.40, 2.36, 4.42, 456, "Almacen B")
almacen_C = Almacenes(2.40, 2.36, 4.42, 789, "Almacen C")
almacen_D = Almacenes(2.40, 2.36, 4.42, 147, "Almacen D")

empleado1 = Empleado("David","Tejada", 21, 2027)

print("El nombre del Almacen es", almacen_A.nombre, "y su id es", almacen_A.id)
print("El empleado es", empleado1.nombre, "y su identificacion es", empleado1.identificacion)