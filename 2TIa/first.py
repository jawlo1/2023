x="Ala ma kota"
y=x
y=y+"!!"
print (x is y)
print( id(x), id(y) )
print(y)
y=y[:-2] #obcięcie dwóch ostatnich znaków
print(y)
