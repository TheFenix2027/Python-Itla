password="1234"
intentos=3
passwordInsert = input(" Ingrese su contraseña: ")
while (passwordInsert!=password and intentos>1):
    intentos-=1
    passwordInsert=input("Tienes "+str(intentos)+" intentos disponibles. Ingresa la contraseña correcta: " )
if (passwordInsert==password):
    print("contraseña correcta")
else:
    print("contraseña incorrecta")