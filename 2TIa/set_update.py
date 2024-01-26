setData={1,2,3}
lista=[5,6]
krotka=(1,7)
slownik={'klucz1':'wartość1', 'klucz2':'wartość2'}
setData.update( lista, krotka, slownik )
print( setData ) # {1, 2, 3, 'klucz2', 5, 6, 7, 'klucz1'}