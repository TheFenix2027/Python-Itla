#Numeros perfectos
numero=int(input("Ingrese un numero "))
x=2
suma=0

while x<=numero:
    if numero % x==0:
        suma += numero//x
    x+=1
if suma==numero:
    print("El numero es perfecto")
else:
    print("El numero no es perfecto")