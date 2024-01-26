x=3
moja_lista=[ 1,'dwa',3.45, x ]
pusta_lista=[]
print( moja_lista[1] )  #drugi element
#print( moja_lista[10] ) #error
print( moja_lista[-1] ) #ostatni
print( moja_lista[1:] ) # od drugiego do końca
print( moja_lista[1:3] ) #od drugiego do trzeciego
print( len(moja_lista) ) #długość listy
moja_lista.append( "pięć" ) #dodanie na koniec
print( moja_lista )
moja_lista.insert( 1, 'drugi element')
print(moja_lista)

lista=['a','b','c','a']
element=lista.pop() #usuwa ostatni element
lista.pop(1) #usuwa 2 element