def wyswietlOsobe(imie,nazwisko,drugieImie='')
    if drugieImie:
        return f"{imie} {drugieImie} {nazwisko}"
    else:
        return f"{imie}  {nazwisko}"
print( wyswietlOsobe( "Jan", "Nowak") )
print( wyswietlOsobe( "Adam", "Karol", "Kowalski") )