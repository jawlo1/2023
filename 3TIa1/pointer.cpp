#include <iostream>

using namespace std;

int main(){

string food = "Pizza";  // zmienna
string* ptr = &food;    // wskaŸnik (adres pamiêci)

cout << food << "\n";

cout << &food << "\n";  // &food - adres pamiêci

cout << ptr << "\n";    // adres pamiêci
}
