#include <iostream>

using namespace std;

int main(){

    int i=0;
    int suma=0;

    while( i<=10 ){
        suma+=i;
        cout << "liczba i=" << i++ << endl;
    }
    cout << "\n suma wynosi=" << suma;
}
