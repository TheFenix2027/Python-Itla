#Cadena de fibonacci
n=int(input("Ingrese un numero para la sucesion de Fibonacci "))
a=0
b=1
c=1

while c<=n:
    if c % 2==1:
        print(a, end=",")
        a+=b
    else:
        print(b, end=",")
        b+=a
    c+=1