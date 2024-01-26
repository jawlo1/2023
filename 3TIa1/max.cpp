#include <iostream>
#include <string>
using namespace std;

int main(){
    int liczba1, liczba2;

    cout << "Podaj pierwsza liczbe: ";
    cin >> liczba1;
    cout << "Podaj druga liczbe: ";
    cin >> liczba2;
    cout << "liczba wieksza to: " << max(liczba1,liczba2);
    cout << "\nliczba mniejsza to: " << min( liczba1,liczba2);
    return 0;
}
