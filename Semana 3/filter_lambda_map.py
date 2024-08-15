nombres = ['Willy','David', 'Rigoberto', 'Randy', 'Pedro', 'Carlos']

nombres_termina_o = filter(lambda nombre:nombre[-1]=='o', nombres)
print(list(nombres_termina_o))

nombres_mayusculas = map(lambda nombre:nombre.upper(), nombres)
print(list(nombres_mayusculas))