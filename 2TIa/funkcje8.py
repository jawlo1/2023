#przekazywanie dowolnej liczby argumentów

def przyklad( **kwargs ):
    print(kwargs)
    for el in kwargs.values():
        print(el)

przyklad( imie="Jan", wiek=30 )
