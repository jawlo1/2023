#include <iostream>

using namespace std;

int main(){

string food = "Pizza";  // zmienna
string* ptr = &food;    // wska�nik (adres pami�ci)

cout << food << "\n";

cout << &food << "\n";  // &food - adres pami�ci

cout << ptr << "\n";    // adres pami�ci
}
