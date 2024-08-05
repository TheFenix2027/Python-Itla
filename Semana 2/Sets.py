set1={"manzana", "naranja", "sandia"}
set1.add("uva")
print(set1)
print(len(set1))
print(type(set1))
print("naranja" in set1)

set2=set(("carro","pasola","motor"))
print(set2)

#unir sets
set1.update(set2)
print(set1)

#eliminar un item random del set
x=set1.pop()
print(x)
print(set1)

#limpiar un set
set1.clear()
print(set1)