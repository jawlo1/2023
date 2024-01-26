lista1=[1,2,3,4]
lista2=lista1
print(id(lista1))
print(id(lista2))
lista2.append(5)
print( lista1 )
print( lista2 )

lista3=lista1.copy()
lista3.append(6)
print(lista1)
print(lista3)