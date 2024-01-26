#include <iostream>

using namespace std;

int main(){

   struct uczen{
        string name;
        int age;
   };

   uczen uczen1,uczen2,uczen3;
   uczen1.name="John";
   uczen1.age=18;
   uczen2.name="Anna";
   uczen2.age=17;

   cout << uczen1.name << endl;
   cout << uczen1.age << endl;
   cout << uczen2.name << endl;
   cout << uczen2.age;
}
