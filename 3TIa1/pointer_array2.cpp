#include <iostream>

using namespace std;

int main(){

    int liczby[5];  // tablica
    int *wskaznik;

    liczby[0]=1;
    liczby[1]=2;
    liczby[2]=3;
    wskaznik = &liczby[2];
    cout << *wskaznik << "\n"; // wartość pod adresem

}
