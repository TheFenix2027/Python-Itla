for i in range(1,5):
    print(i, end=" ")

n=int(input("Ingrese un numero: "))
divisores=0
for i in range(1,n+1):
    if n%i==0:
        divisores+=1
if divisores==2:
    print("El numero" , n, "es primo")
else:
    print("El numero" , n, "no es primo")  








