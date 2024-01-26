#include <iostream>

using namespace std;

int main(){
    int day=4;

    switch( day ){
        case 1:
            cout << "Poniedzia³ek";
            break;
        case 2:
            cout << "Wtorekk";
            break;
        case 3:
            cout << "Œroda";
            break;
        case 4:
            cout << "Czwartek";
            break;
        case 5:
            cout << "Pi¹tek";
            break;
        default:
            cout << "weekend";
    }
}
