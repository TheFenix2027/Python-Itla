matrizA = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

matrizB  = [[2, 4, 6],
            [1, 3, 5],
            [5, 7, 9]]

# print(f"datos de matriz {matrizA}")
# print(f"datos de matriz {matrizB[1][0]}")

#Transponer matriz
def transponer_matriz(matriz):
    n = len(matriz)
    m = len(matriz[0])
    matriz_transpuesta = [[matriz[j][i] for j in range(n)] for i in range(m)]
    return matriz_transpuesta

transpuesta = transponer_matriz(matrizB)
#print(transpuesta)

#Sumar las matrices
def sumaMatrices (matrizA, matrizB):
    x = len(matrizA)
    y = len(matrizA[0])
    matriz_resultado = [[matrizA[c][f] + matrizB[c][f] for f in range(y)] for c in range(x)]
    return matriz_resultado

resultado = sumaMatrices(matrizA, transpuesta)
print(f"La suma de las matrices es: {resultado}")