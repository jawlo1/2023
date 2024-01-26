#include <iostream>

using namespace std;

int main(){

   int liczby[5]={ 4, 5, 7, 9, 3};
    int suma=0;

   for( int i=0; i<5; i++){
        suma+=liczby[i];
   }
   cout << "suma= "<< suma;
}
