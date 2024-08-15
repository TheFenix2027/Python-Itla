#The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
def funcion(n):
    return len(n)

x = map(funcion, ('Manzana', 'Pera', 'Fresa'))

numeros = [2,4,6,8,10,12]
cuadrados = map(lambda x:x**2,numeros)
print(list(cuadrados))

numeros2 = [1,2,3,4,5,6,7,8,9,10]
numeros_impares=filter(lambda x:x%2!=0, numeros2)
print(list(numeros_impares))
