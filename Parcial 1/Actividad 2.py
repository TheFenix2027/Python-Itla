numeros = [1122, 4567, 2233, 7632, 9900, 9268, 3355,7652]

def numero_tartamudo(numeros):
    #Convertimos el arreglo a str
    numeroStr = str(numeros)
    return any(numeroStr[i] == numeroStr[i+1] for i in range(len(numeroStr)-1))
#range(len(numeroStr)-1) genera indices desde 0 hasta range(len(numeroStr)-2), permitiendo comparar cada digito con el siguiente
#numeroStr[i] == numeroStr[i+1] compara si el digito actual es igual al siguiente
#"any" devuelve True si al menos una de las comparaciones resulta en True, lo que indica que el numero es tartamudo

def filtrar_tartamudos(numeros):
    return list(filter(lambda x: numero_tartamudo(x), numeros))

tartamudos = filtrar_tartamudos(numeros)
print(tartamudos)
