#include <iostream>

using namespace std;

int main(){
    int i=0;

    while( i<=10 ){
        if( !(i%2) ){
            cout << "liczba i=" << i << endl;
        }
        i++;
    }
}
