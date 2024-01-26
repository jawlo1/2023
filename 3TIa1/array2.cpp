#include <iostream>

using namespace std;

int main(){

   string cars[4]={"audi","volvo","toyota","fiat"};

   for( int i=3; i>=0; i--){
        cout << i+1 << ". "<< cars[i]<< endl;
   }
}
