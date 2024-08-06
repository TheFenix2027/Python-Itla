#Cadena de fibonacci
try:
    n=int(input("Ingrese un numero para la sucesion de Fibonacci "))
    a=0
    b=1
    c=1

    while c<=n+1:
        if c % 2==1:
            print(a, end=",")
            a+=b
        else:
            print(b, end=",")
            b+=a
        c+=1
except Exception as error:
    print(f"Ha ocurrido un error! {error}")