#przekazywanie dowolnej liczby argumentów

def suma( *arg ):
    wynik = 0
    print( type(arg) )
    for el in arg:
        wynik += el
    return wynik

print( suma(1,2,3,4) )