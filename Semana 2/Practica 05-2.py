#Numeros amigos
try:
    numero1=int(input("Ingrese el primer numero "))
    numero2=int(input("Ingrese el segundo numero "))
    x=2
    suma=0

    while x<=numero1:
        if numero1 % x==0:
            suma += numero1//x
        x+=1

    if suma==numero2:
        print("Estos numeros son amigos")
    else:
        print("Estos numeros NO son amigos")
except Exception as error:
    print(f"Ha ocurrido un error! {error}")