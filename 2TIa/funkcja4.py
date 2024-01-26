# Sumowanie pozycji słownika

koszyk={
    "telwizor":2000,
    "konsola":1500,
    "komputer":3000
}
def obliczKoszyk( listaZakupow ):
    suma=0
    for element in listaZakupow:
        suma+=listaZakupow[element]
    return suma

print( obliczKoszyk(koszyk) )
