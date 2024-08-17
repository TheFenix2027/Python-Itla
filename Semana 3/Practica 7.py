#Resolucion de problemas utilizando las funciones map(), lambda() y filter().
print("----Primer problema----")
#Primer problema
vlista = [1,2,3,4,5,6,7,8,9,10]

def double_numbers(vlista):
    for item in vlista:
        print(int(item*2))

double_numbers(vlista)

print("----Segundo problema----")
#Segundo problema
def filter_even_numbers(x):
    if x%2 ==0:
        return True
    else:
        return False

vnumerosPares = filter(filter_even_numbers, vlista)

for x in vnumerosPares:
    print(x)

print("----Tercer problema----")
#Tercer problema
vcadenas = ["carro", "motor", "pasola", "avion", "barco"]

def uppercase_strings(vcadenas):
    while True:
        vcadenasMayuscula = [x.upper() for x in vcadenas]
        print(vcadenasMayuscula)
        break

uppercase_strings(vcadenas)

print("----Cuarto problema----")
#Cuarto problema
vpalabras = ["David", "Harold", "Arisleyda", "Willy", "Rayhan", "Josue", "Ambar"]

def filter_long_words(vpalabras):
    vpalabrasFiltradas = []
    for item in range(len(vpalabras)):
        if len(vpalabras[item]) > 5:
            vpalabrasFiltradas.append(vpalabras[item])
            # print(len(vpalabras[item]))
    return vpalabrasFiltradas
resultado = filter_long_words(vpalabras)
print(resultado)

print("----Quinto problema----")
#Quinto problema
def square_positive_numbers(vlista):
    for item in vlista:
        print(int(item**2))

square_positive_numbers(vlista)

print("----Sexto problema----")
#Sexto problema
def filter_names_starting_with_a(vpalabras):
    vpalabrasFiltradas = []
    for item in vpalabras:
        #print(item[0])
        if item[0].upper()=="A":
            vpalabrasFiltradas.append(item)
    return vpalabrasFiltradas
resultado = filter_names_starting_with_a(vpalabras)
print(resultado)