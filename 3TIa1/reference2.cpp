#include <iostream>

using namespace std;

int main(){

   string food = "Pizza";  // zmienna
   string &meal = food;    // referencja

   meal="sushi";

   cout << food << endl;
   cout << meal << endl;
}
