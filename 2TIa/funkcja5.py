# przekazywanie listy do funkcji

imiona=["Kacper","Barbara","Jusytna"]

def powitaj( lista ):
    for imie in lista:
        print( f"Witaj {imie}")

powitaj( imiona )