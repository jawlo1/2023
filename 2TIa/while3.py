komunikat = "\nPowiedz mi coś o sobie a wyświetlę to na ekranie: "
komunikat += "\n napisz  'koniec', aby zakończyć"
message = ""
while message != 'koniec':
    message = input( komunikat )
    print( message )
print( "Pętla zakończona")