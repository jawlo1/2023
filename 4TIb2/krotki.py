krotka1=("jeden","dwa","trzy")

#krotka[1]="two"   # błąd

krotka2=(1,2,3)
krotka=krotka1+krotka2
print(krotka)

krokaPowielona=krotka1*3
print(krokaPowielona)
print( len(krokaPowielona) )
print( krotka1.index("dwa") )
print( krokaPowielona.count(("dwa")))
print( "cztery" in krotka1 )
