#The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
edades = [17, 18, 16, 20, 21, 10, 13, 25]

def funcion(x):
    if x < 18:
        return False
    else:
        return True

adultos = filter(funcion, edades)

for x in adultos:
    print(x)