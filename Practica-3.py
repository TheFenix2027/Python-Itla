#Primer programa
numero=int(input("Ingrese cualquier numero: "))
def suma(n):
    sumaTotal=0
    for i in range(1, n+1):
        sumaTotal=sumaTotal + i
    print(sumaTotal)
suma(numero)

#Segundo programa
nombreCompleto=["David" , "Tejada"]
nombreCompleto.reverse()
print(nombreCompleto)
