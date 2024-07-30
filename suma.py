x=int(input("ingresa el primer numero: "))
y=int(input("ingresa el segundo numero: "))
operacion=input("ingresa la operacion: ")

if(operacion== "+"):
    print(x+y)
elif(operacion=="*"):
    print(x*y)
elif(operacion=="/"):
    print(x/y)
elif(operacion=="%"):
    print(x%y)

edad=int(input("ingrese su edad: "))
if(edad>=18):
    print("eres mayor de edad")
elif(edad>=13):
    print("eres un adolescente")
else:
    print("eres un niño")