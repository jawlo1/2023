#include <iostream>

using namespace std;

int main(){

    cout << (char)218 << (char)196 << (char)194<< (char)196<< (char)191 << endl;
    for( int i=0; i<255; i++){

        cout<< "│ "<<  i<< " │ " << (char)i << " │\n";
        cout<< "├──────┼──────┤\n";

    }
    cout<< "za pêtl¹";
}
