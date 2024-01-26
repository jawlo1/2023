# modyfikowanie listy w funkcji

modelDoWydrukowania=["gwizdek","czołg","samolot"]
wydrukowane = []
def drukuj( pelna, pusta ):
    while pelna:
        biezacyWydruk=pelna.pop()
        print( f"Drukuje {biezacyWydruk}" )
        pusta.append( biezacyWydruk )
drukuj( modelDoWydrukowania, wydrukowane )
print( modelDoWydrukowania )
print( wydrukowane )