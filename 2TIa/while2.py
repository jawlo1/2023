komunikat = "\nPowiedz mi coś o sobie a wyświetlę to na ekranie: "
komunikat += "\n napisz  'koniec', aby zakończyć"
active = True
while active:
    message = input( komunikat )
    if message == 'koniec':
        active = False
    else:
        print( message )
print( "Pętla zakończona")