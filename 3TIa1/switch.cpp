#include <iostream>

using namespace std;

int main(){
    int day=4;

    switch( day ){
        case 1:
            cout << "Poniedzia�ek";
            break;
        case 2:
            cout << "Wtorekk";
            break;
        case 3:
            cout << "�roda";
            break;
        case 4:
            cout << "Czwartek";
            break;
        case 5:
            cout << "Pi�tek";
            break;
        default:
            cout << "weekend";
    }
}
