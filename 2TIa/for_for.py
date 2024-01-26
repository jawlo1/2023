tabliczka = ""
for i in range( 1,11 ):
    for j in range( 1,11):
        tabliczka += str( i*j )+ "\t"
    tabliczka += "\n"
print( tabliczka )